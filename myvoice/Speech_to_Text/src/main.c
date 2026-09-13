#include <errno.h>
#include <getopt.h>
#include <limits.h>
#include <pthread.h>
#include <signal.h>
#include <stdatomic.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <time.h>
#include <unistd.h>

#include "msp_cmn.h"
#include "msp_errors.h"
#include "qisr.h"
#include "speech_recognizer.h"

#define APP_ID "6159904a"
#define SAMPLE_RATE 16000
#define AUDIO_CHUNK_BYTES 6400
#define DEFAULT_DEVICE "plughw:CARD=XFMDPV0018,DEV=0"

typedef enum {
	INPUT_NONE,
	INPUT_FILE,
	INPUT_MIC
} input_mode_t;

typedef struct {
	input_mode_t mode;
	const char *audio_file;
	const char *device;
	const char *grammar;
	int threshold;
	int timeout_seconds;
	int json;
	int verbose;
} options_t;

typedef struct {
	char root[PATH_MAX];
	char jet[PATH_MAX];
	char grammar[PATH_MAX];
	char grammar_build[PATH_MAX];
	char work[PATH_MAX];
} paths_t;

typedef struct {
	atomic_int done;
	int error;
	char grammar_id[64];
} grammar_build_t;

typedef struct {
	pthread_mutex_t lock;
	char *xml;
	size_t length;
	size_t capacity;
	atomic_int done;
	atomic_int end_reason;
} recognition_result_t;

typedef struct {
	FILE *file;
	uint64_t bytes_left;
} audio_stream_t;

static recognition_result_t *active_result;
static volatile sig_atomic_t stop_requested;
static int verbose_output;

static void print_usage(const char *program)
{
	printf("用法:\n");
	printf("  %s --record [选项]\n", program);
	printf("  %s --file AUDIO.pcm|AUDIO.wav [选项]\n\n", program);
	printf("选项:\n");
	printf("  -r, --record             从 M260C 实时录音\n");
	printf("  -f, --file PATH          识别 16kHz/单声道/16位 PCM 或 WAV\n");
	printf("  -d, --device NAME        ALSA 设备，默认 %s\n", DEFAULT_DEVICE);
	printf("  -g, --grammar PATH       BNF 语法文件\n");
	printf("  -t, --threshold N        置信度阈值，默认 40\n");
	printf("  -T, --timeout SEC        实时录音最长时间，默认 10 秒\n");
	printf("  -j, --json               输出 JSON\n");
	printf("  -v, --verbose            输出原始识别结果\n");
	printf("  -h, --help               显示帮助\n");
}

static int parse_integer(const char *text, int minimum, int maximum, int *value)
{
	char *end = NULL;
	long parsed;

	errno = 0;
	parsed = strtol(text, &end, 10);
	if (errno || !end || *end != '\0' || parsed < minimum || parsed > maximum)
		return -1;
	*value = (int)parsed;
	return 0;
}

static int parse_options(int argc, char **argv, options_t *options)
{
	static const struct option long_options[] = {
		{"record", no_argument, NULL, 'r'},
		{"file", required_argument, NULL, 'f'},
		{"device", required_argument, NULL, 'd'},
		{"grammar", required_argument, NULL, 'g'},
		{"threshold", required_argument, NULL, 't'},
		{"timeout", required_argument, NULL, 'T'},
		{"json", no_argument, NULL, 'j'},
		{"verbose", no_argument, NULL, 'v'},
		{"help", no_argument, NULL, 'h'},
		{NULL, 0, NULL, 0}
	};
	int option;

	memset(options, 0, sizeof(*options));
	options->device = DEFAULT_DEVICE;
	options->threshold = 40;
	options->timeout_seconds = 10;

	while ((option = getopt_long(argc, argv, "rf:d:g:t:T:jvh", long_options, NULL)) != -1) {
		switch (option) {
		case 'r':
			if (options->mode != INPUT_NONE)
				return -1;
			options->mode = INPUT_MIC;
			break;
		case 'f':
			if (options->mode != INPUT_NONE)
				return -1;
			options->mode = INPUT_FILE;
			options->audio_file = optarg;
			break;
		case 'd':
			options->device = optarg;
			break;
		case 'g':
			options->grammar = optarg;
			break;
		case 't':
			if (parse_integer(optarg, 0, 100, &options->threshold))
				return -1;
			break;
		case 'T':
			if (parse_integer(optarg, 1, 120, &options->timeout_seconds))
				return -1;
			break;
		case 'j':
			options->json = 1;
			break;
		case 'v':
			options->verbose = 1;
			break;
		case 'h':
			print_usage(argv[0]);
			exit(0);
		default:
			return -1;
		}
	}

	if (options->mode == INPUT_NONE || optind != argc)
		return -1;
	return 0;
}

static int copy_path(char *destination, size_t size, const char *source)
{
	int written = snprintf(destination, size, "%s", source);
	return written < 0 || (size_t)written >= size ? -1 : 0;
}

static int join_path(char *destination, size_t size, const char *base, const char *suffix)
{
	int written = snprintf(destination, size, "%s/%s", base, suffix);
	return written < 0 || (size_t)written >= size ? -1 : 0;
}

static int resolve_paths(paths_t *paths, const char *custom_grammar)
{
	char executable[PATH_MAX];
	char *slash;
	char *directory_name;
	ssize_t length;

	length = readlink("/proc/self/exe", executable, sizeof(executable) - 1);
	if (length < 0 || (size_t)length >= sizeof(executable) - 1)
		return -1;
	executable[length] = '\0';

	slash = strrchr(executable, '/');
	if (!slash)
		return -1;
	*slash = '\0';
	directory_name = strrchr(executable, '/');
	directory_name = directory_name ? directory_name + 1 : executable;
	if (!strcmp(directory_name, "bin")) {
		slash = strrchr(executable, '/');
		if (!slash)
			return -1;
		*slash = '\0';
	}

	if (copy_path(paths->root, sizeof(paths->root), executable) ||
		join_path(paths->jet, sizeof(paths->jet), paths->root, "config/common.jet") ||
		join_path(paths->grammar_build, sizeof(paths->grammar_build), paths->root, "runtime/grammar") ||
		join_path(paths->work, sizeof(paths->work), paths->root, "runtime"))
		return -1;

	if (custom_grammar) {
		if (!realpath(custom_grammar, paths->grammar))
			return -1;
	} else if (join_path(paths->grammar, sizeof(paths->grammar), paths->root, "config/call.bnf")) {
		return -1;
	}
	return 0;
}

static int mkdir_recursive(const char *path)
{
	char buffer[PATH_MAX];
	char *cursor;

	if (copy_path(buffer, sizeof(buffer), path))
		return -1;
	for (cursor = buffer + 1; *cursor; ++cursor) {
		if (*cursor != '/')
			continue;
		*cursor = '\0';
		if (mkdir(buffer, 0755) && errno != EEXIST)
			return -1;
		*cursor = '/';
	}
	if (mkdir(buffer, 0755) && errno != EEXIST)
		return -1;
	return 0;
}

static int read_entire_file(const char *path, char **content, unsigned int *length)
{
	FILE *file;
	long size;
	char *buffer;

	file = fopen(path, "rb");
	if (!file)
		return -1;
	if (fseek(file, 0, SEEK_END) || (size = ftell(file)) <= 0 ||
		(unsigned long)size > UINT32_MAX || fseek(file, 0, SEEK_SET)) {
		fclose(file);
		return -1;
	}
	buffer = malloc((size_t)size + 1);
	if (!buffer) {
		fclose(file);
		return -1;
	}
	if (fread(buffer, 1, (size_t)size, file) != (size_t)size) {
		free(buffer);
		fclose(file);
		return -1;
	}
	buffer[size] = '\0';
	fclose(file);
	*content = buffer;
	*length = (unsigned int)size;
	return 0;
}

static int grammar_callback(int error, const char *info, void *user_data)
{
	grammar_build_t *build = user_data;

	build->error = error;
	if (error == MSP_SUCCESS && info)
		copy_path(build->grammar_id, sizeof(build->grammar_id), info);
	atomic_store(&build->done, 1);
	return 0;
}

static int build_grammar(const paths_t *paths, char *grammar_id, size_t grammar_id_size)
{
	grammar_build_t build;
	char *grammar_content = NULL;
	char *parameters = NULL;
	unsigned int grammar_length = 0;
	int call_result;
	int waited_ms = 0;

	memset(&build, 0, sizeof(build));
	atomic_init(&build.done, 0);
	if (read_entire_file(paths->grammar, &grammar_content, &grammar_length)) {
		fprintf(stderr, "无法读取语法文件: %s\n", paths->grammar);
		return -1;
	}
	if (asprintf(&parameters,
			"engine_type = local, asr_res_path = fo|%s, sample_rate = %d, grm_build_path = %s",
			paths->jet, SAMPLE_RATE, paths->grammar_build) < 0) {
		free(grammar_content);
		return -1;
	}

	call_result = QISRBuildGrammar("bnf", grammar_content, grammar_length,
		parameters, grammar_callback, &build);
	free(parameters);
	free(grammar_content);
	if (call_result != MSP_SUCCESS) {
		fprintf(stderr, "语法构建调用失败: %d\n", call_result);
		return call_result;
	}

	while (!atomic_load(&build.done) && waited_ms < 30000) {
		usleep(100000);
		waited_ms += 100;
	}
	if (!atomic_load(&build.done)) {
		fprintf(stderr, "语法构建超时\n");
		return -1;
	}
	if (build.error != MSP_SUCCESS || !build.grammar_id[0]) {
		return build.error ? build.error : -1;
	}
	return copy_path(grammar_id, grammar_id_size, build.grammar_id);
}

static void result_init(recognition_result_t *result)
{
	memset(result, 0, sizeof(*result));
	pthread_mutex_init(&result->lock, NULL);
	atomic_init(&result->done, 0);
	atomic_init(&result->end_reason, 0);
}

static void result_reset(recognition_result_t *result)
{
	pthread_mutex_lock(&result->lock);
	result->length = 0;
	if (result->xml)
		result->xml[0] = '\0';
	pthread_mutex_unlock(&result->lock);
	atomic_store(&result->done, 0);
	atomic_store(&result->end_reason, 0);
}

static void result_destroy(recognition_result_t *result)
{
	free(result->xml);
	pthread_mutex_destroy(&result->lock);
}

static void on_result(const char *fragment, char is_last)
{
	recognition_result_t *result = active_result;
	size_t fragment_length;
	size_t required;
	char *resized;

	(void)is_last;
	if (!result || !fragment)
		return;
	fragment_length = strlen(fragment);
	pthread_mutex_lock(&result->lock);
	required = result->length + fragment_length + 1;
	if (required > result->capacity) {
		size_t new_capacity = result->capacity ? result->capacity : 4096;
		while (new_capacity < required)
			new_capacity *= 2;
		resized = realloc(result->xml, new_capacity);
		if (!resized) {
			pthread_mutex_unlock(&result->lock);
			return;
		}
		result->xml = resized;
		result->capacity = new_capacity;
	}
	memcpy(result->xml + result->length, fragment, fragment_length + 1);
	result->length += fragment_length;
	pthread_mutex_unlock(&result->lock);
}

static void on_speech_begin(void)
{
	if (active_result)
		result_reset(active_result);
}

static void on_speech_end(int reason)
{
	if (!active_result)
		return;
	atomic_store(&active_result->end_reason, reason);
	atomic_store(&active_result->done, 1);
}

static char *make_session_parameters(const paths_t *paths, const char *grammar_id)
{
	char *parameters = NULL;

	if (asprintf(&parameters,
			"engine_type = local, asr_res_path = fo|%s, sample_rate = %d, "
			"grm_build_path = %s, local_grammar = %s, result_type = xml, "
			"result_encoding = UTF-8, vad_enable = 1, vad_eos = 900, asr_denoise = 1",
			paths->jet, SAMPLE_RATE, paths->grammar_build, grammar_id) < 0)
		return NULL;
	return parameters;
}

static uint16_t read_u16_le(const unsigned char *bytes)
{
	return (uint16_t)bytes[0] | ((uint16_t)bytes[1] << 8);
}

static uint32_t read_u32_le(const unsigned char *bytes)
{
	return (uint32_t)bytes[0] | ((uint32_t)bytes[1] << 8) |
		((uint32_t)bytes[2] << 16) | ((uint32_t)bytes[3] << 24);
}

static int open_audio_stream(const char *path, audio_stream_t *stream)
{
	unsigned char header[12];
	unsigned char chunk_header[8];
	int format_found = 0;
	uint16_t audio_format = 0;
	uint16_t channels = 0;
	uint16_t bits = 0;
	uint32_t rate = 0;

	memset(stream, 0, sizeof(*stream));
	stream->file = fopen(path, "rb");
	if (!stream->file) {
		fprintf(stderr, "无法打开音频文件: %s\n", path);
		return -1;
	}
	if (fread(header, 1, sizeof(header), stream->file) != sizeof(header)) {
		fprintf(stderr, "音频文件为空或过短: %s\n", path);
		goto fail;
	}
	if (memcmp(header, "RIFF", 4) || memcmp(header + 8, "WAVE", 4)) {
		long size;
		if (fseek(stream->file, 0, SEEK_END))
			goto fail;
		size = ftell(stream->file);
		if (size <= 0 || fseek(stream->file, 0, SEEK_SET))
			goto fail;
		stream->bytes_left = (uint64_t)size;
		return 0;
	}

	while (fread(chunk_header, 1, sizeof(chunk_header), stream->file) == sizeof(chunk_header)) {
		uint32_t chunk_size = read_u32_le(chunk_header + 4);
		if (!memcmp(chunk_header, "fmt ", 4)) {
			unsigned char format[16];
			if (chunk_size < sizeof(format) || fread(format, 1, sizeof(format), stream->file) != sizeof(format))
				goto fail;
			audio_format = read_u16_le(format);
			channels = read_u16_le(format + 2);
			rate = read_u32_le(format + 4);
			bits = read_u16_le(format + 14);
			if (fseek(stream->file, (long)(chunk_size - sizeof(format) + (chunk_size & 1U)), SEEK_CUR))
				goto fail;
			format_found = 1;
		} else if (!memcmp(chunk_header, "data", 4)) {
			if (!format_found)
				goto fail;
			stream->bytes_left = chunk_size;
			break;
		} else if (fseek(stream->file, (long)(chunk_size + (chunk_size & 1U)), SEEK_CUR)) {
			goto fail;
		}
	}

	if (!format_found || !stream->bytes_left) {
		fprintf(stderr, "WAV 文件缺少音频数据\n");
		goto fail;
	}
	if (audio_format != 1 || channels != 1 || rate != SAMPLE_RATE || bits != 16) {
		fprintf(stderr, "WAV 必须是 16kHz、单声道、16位 PCM\n");
		goto fail;
	}
	return 0;

fail:
	fclose(stream->file);
	stream->file = NULL;
	return -1;
}

static int recognize_file(const char *path, const char *parameters,
		recognition_result_t *result)
{
	audio_stream_t stream;
	struct speech_rec recognizer;
	struct speech_rec_notifier notifier = {on_result, on_speech_begin, on_speech_end};
	unsigned char buffer[AUDIO_CHUNK_BYTES];
	int initialized = 0;
	int started = 0;
	int status = -1;
	int error;

	if (open_audio_stream(path, &stream))
		return -1;
	active_result = result;
	error = sr_init(&recognizer, parameters, SR_USER, &notifier);
	if (error) {
		fprintf(stderr, "识别引擎初始化失败: %d\n", error);
		goto cleanup;
	}
	initialized = 1;
	error = sr_start_listening(&recognizer);
	if (error) {
		fprintf(stderr, "识别引擎启动失败: %d\n", error);
		goto cleanup;
	}
	started = 1;

	while (stream.bytes_left && !atomic_load(&result->done)) {
		size_t wanted = stream.bytes_left < sizeof(buffer) ? (size_t)stream.bytes_left : sizeof(buffer);
		size_t count = fread(buffer, 1, wanted, stream.file);
		if (!count)
			break;
		stream.bytes_left -= count;
		error = sr_write_audio_data(&recognizer, (char *)buffer, (unsigned int)count);
		if (error) {
			fprintf(stderr, "写入音频失败: %d\n", error);
			goto cleanup;
		}
	}

	if (started) {
		error = sr_stop_listening(&recognizer);
		started = 0;
		if (error) {
			fprintf(stderr, "结束识别失败: %d\n", error);
			goto cleanup;
		}
	}
	status = 0;

cleanup:
	if (started)
		sr_stop_listening(&recognizer);
	if (initialized)
		sr_uninit(&recognizer);
	active_result = NULL;
	fclose(stream.file);
	return status;
}

static double elapsed_seconds(const struct timespec *start, const struct timespec *now)
{
	return (double)(now->tv_sec - start->tv_sec) +
		(double)(now->tv_nsec - start->tv_nsec) / 1000000000.0;
}

static int recognize_microphone(const char *device, int timeout_seconds,
		const char *parameters, recognition_result_t *result, int json)
{
	struct speech_rec recognizer;
	struct speech_rec_notifier notifier = {on_result, on_speech_begin, on_speech_end};
	record_dev_id device_id;
	struct timespec start;
	struct timespec now;
	int initialized = 0;
	int started = 0;
	int status = -1;
	int error;

	device_id.u.name = (char *)device;
	active_result = result;
	error = sr_init_ex(&recognizer, parameters, SR_MIC, device_id, &notifier);
	if (error) {
		fprintf(stderr, "无法打开录音设备 %s，错误: %d\n", device, error);
		goto cleanup;
	}
	initialized = 1;
	error = sr_start_listening(&recognizer);
	if (error) {
		fprintf(stderr, "录音启动失败: %d\n", error);
		goto cleanup;
	}
	started = 1;
	if (!json)
		fprintf(stderr, "正在监听，请说出 call.bnf 中的命令词……\n");
	clock_gettime(CLOCK_MONOTONIC, &start);

	while (!atomic_load(&result->done) && !stop_requested) {
		usleep(50000);
		clock_gettime(CLOCK_MONOTONIC, &now);
		if (elapsed_seconds(&start, &now) >= timeout_seconds)
			break;
	}

	if (started) {
		error = sr_stop_listening(&recognizer);
		started = 0;
		if (error) {
			fprintf(stderr, "结束录音失败: %d\n", error);
			goto cleanup;
		}
	}
	status = stop_requested ? -1 : 0;

cleanup:
	if (started)
		sr_stop_listening(&recognizer);
	if (initialized)
		sr_uninit(&recognizer);
	active_result = NULL;
	return status;
}

static int extract_tag(const char *xml, const char *tag, char *output, size_t output_size)
{
	char opening[64];
	char closing[64];
	const char *start;
	const char *end;
	size_t length;

	if (!xml || snprintf(opening, sizeof(opening), "<%s>", tag) < 0 ||
		snprintf(closing, sizeof(closing), "</%s>", tag) < 0)
		return -1;
	start = strstr(xml, opening);
	if (!start)
		return -1;
	start += strlen(opening);
	end = strstr(start, closing);
	if (!end)
		return -1;
	length = (size_t)(end - start);
	while (length && (*start == ' ' || *start == '\t' || *start == '\r' || *start == '\n')) {
		++start;
		--length;
	}
	while (length && (start[length - 1] == ' ' || start[length - 1] == '\t' ||
		start[length - 1] == '\r' || start[length - 1] == '\n'))
		--length;
	if (!length || length >= output_size)
		return -1;
	memcpy(output, start, length);
	output[length] = '\0';
	return 0;
}

static int extract_command_id(const char *xml)
{
	const char *position = xml;
	char *end;
	long id;

	while (position && (position = strstr(position, "id=")) != NULL) {
		position += 3;
		if (*position == '\'' || *position == '"')
			++position;
		errno = 0;
		id = strtol(position, &end, 10);
		if (!errno && end != position && id >= 0 && id <= INT_MAX)
			return (int)id;
	}
	return 0;
}

static void print_json_string(const char *text)
{
	const unsigned char *cursor = (const unsigned char *)text;

	putchar('"');
	while (*cursor) {
		switch (*cursor) {
		case '"': fputs("\\\"", stdout); break;
		case '\\': fputs("\\\\", stdout); break;
		case '\b': fputs("\\b", stdout); break;
		case '\f': fputs("\\f", stdout); break;
		case '\n': fputs("\\n", stdout); break;
		case '\r': fputs("\\r", stdout); break;
		case '\t': fputs("\\t", stdout); break;
		default:
			if (*cursor < 0x20)
				printf("\\u%04x", *cursor);
			else
				putchar(*cursor);
		}
		++cursor;
	}
	putchar('"');
}

static int print_recognition(recognition_result_t *result, const options_t *options)
{
	char text[1024] = {0};
	char confidence_text[32] = {0};
	int confidence = 0;
	int command_id = 0;
	int recognized = 0;

	pthread_mutex_lock(&result->lock);
	if (verbose_output && result->xml)
		fprintf(stderr, "原始结果: %s\n", result->xml);
	if (result->xml && !extract_tag(result->xml, "rawtext", text, sizeof(text))) {
		if (!extract_tag(result->xml, "confidence", confidence_text, sizeof(confidence_text)))
			confidence = atoi(confidence_text);
		command_id = extract_command_id(result->xml);
		recognized = confidence >= options->threshold;
	}
	pthread_mutex_unlock(&result->lock);

	if (options->json) {
		if (recognized) {
			fputs("{\"status\":\"ok\",\"text\":", stdout);
			print_json_string(text);
			printf(",\"confidence\":%d,\"command_id\":%d}\n", confidence, command_id);
		} else {
			printf("{\"status\":\"no_match\",\"text\":\"\",\"confidence\":%d,\"command_id\":0}\n",
				confidence);
		}
	} else if (recognized) {
		printf("识别结果: %s\n", text);
		printf("置信度: %d\n", confidence);
		printf("命令 ID: %d\n", command_id);
	} else {
		printf("未识别到有效命令词\n");
	}
	return recognized ? 0 : 2;
}

static void handle_signal(int signal_number)
{
	(void)signal_number;
	stop_requested = 1;
}

int main(int argc, char **argv)
{
	options_t options;
	paths_t paths;
	recognition_result_t result;
	char grammar_id[64];
	char login_parameters[PATH_MAX + 64];
	char *session_parameters = NULL;
	int login_done = 0;
	int recognition_status;
	int exit_status = 1;
	int error;

	if (parse_options(argc, argv, &options)) {
		print_usage(argv[0]);
		return 1;
	}
	verbose_output = options.verbose;
	if (resolve_paths(&paths, options.grammar)) {
		fprintf(stderr, "无法解析程序或语法文件路径\n");
		return 1;
	}
	if (access(paths.jet, R_OK) || access(paths.grammar, R_OK)) {
		fprintf(stderr, "缺少离线识别资源或语法文件\n");
		return 1;
	}
	if (mkdir_recursive(paths.grammar_build) || mkdir_recursive(paths.work)) {
		fprintf(stderr, "无法创建运行目录: %s\n", paths.work);
		return 1;
	}
	if (snprintf(login_parameters, sizeof(login_parameters),
			"appid = %s, work_dir = %s", APP_ID, paths.work) >= (int)sizeof(login_parameters)) {
		fprintf(stderr, "运行路径过长\n");
		return 1;
	}

	error = MSPLogin(NULL, NULL, login_parameters);
	if (error != MSP_SUCCESS) {
		fprintf(stderr, "离线识别登录失败: %d\n", error);
		return 1;
	}
	login_done = 1;
	error = build_grammar(&paths, grammar_id, sizeof(grammar_id));
	if (error == MSP_ERROR_AUTH_TRIAL_EXPIRED) {
		fprintf(stderr, "离线资源已停止支持新建语法，使用 SDK 自带语法。\n");
		if (copy_path(grammar_id, sizeof(grammar_id), "call"))
			goto cleanup;
	} else if (error) {
		fprintf(stderr, "语法构建失败: %d\n", error);
		goto cleanup;
	}
	if (options.verbose)
		fprintf(stderr, "语法 ID: %s\n", grammar_id);

	session_parameters = make_session_parameters(&paths, grammar_id);
	if (!session_parameters)
		goto cleanup;
	result_init(&result);
	signal(SIGINT, handle_signal);
	signal(SIGTERM, handle_signal);

	if (options.mode == INPUT_FILE)
		recognition_status = recognize_file(options.audio_file, session_parameters, &result);
	else
		recognition_status = recognize_microphone(options.device, options.timeout_seconds,
			session_parameters, &result, options.json);
	if (!recognition_status)
		exit_status = print_recognition(&result, &options);
	result_destroy(&result);

cleanup:
	free(session_parameters);
	if (login_done)
		MSPLogout();
	return exit_status;
}
