/*
 * @Description: 
 * @version: 
 * @Author: rfge
 * @Date: 2020-10-28 23:32:41
 * @LastEditors: rfge
 * @LastEditTime: 2020-12-29 10:10:30
 */


#include <fstream>
#include <assert.h>
#include <cstring>
#include <atomic>
#include <unistd.h>

#include "aikit_biz_api.h"
#include "aikit_constant.h"
#include "aikit_biz_config.h"

using namespace std;
using namespace AIKIT;

FILE *fin = nullptr;
static const char *ABILITY = "ece9d3c90";
static std::atomic_bool ttsFinished(false);

void OnOutput(AIKIT_HANDLE* handle, const AIKIT_OutputData* output){
    printf("OnOutput abilityID :%s\n",handle->abilityID);
    printf("OnOutput key:%s\n",output->node->key);
    if((output->node->value) && (fin != nullptr))
    {
        fwrite(output->node->value, sizeof(char), output->node->len, fin);
    }
}

void OnEvent(AIKIT_HANDLE* handle, AIKIT_EVENT eventType, const AIKIT_OutputEvent* eventValue){
    printf("OnEvent:%d\n",eventType);
    if(eventType == AIKIT_Event_End){
        ttsFinished = true;
    }
}

void OnError(AIKIT_HANDLE* handle, int32_t err, const char* desc){
    printf("OnError:%d\n",err);
}


void TestAisound(){
    AIKIT_ParamBuilder* paramBuilder = nullptr;
    AIKIT_DataBuilder* dataBuilder = nullptr;
    AIKIT_OutputData* output = nullptr;
    AIKIT_HANDLE* handle = nullptr;
    AiText* aiText_raw = nullptr;
    string text = "这里是科大讯飞合成引擎";
    int ret = 0;
    ttsFinished = false;

    fin = fopen("OutPut.pcm", "w+");
    if (fin == nullptr){
        printf("open output.pcm fail\n");
        goto exit;
    }

    paramBuilder = AIKIT_ParamBuilder::create();
    paramBuilder->param("vcn","xiaoyan",strlen("xiaoyan"));//必选参数，支持中文xiaoyan 英文发音人catherine
    paramBuilder->param("speed",50); //可选参数，默认为50
    paramBuilder->param("pitch",50); //可选参数，默认为50
    paramBuilder->param("volume",50);//可选参数，默认为50
    paramBuilder->param("textEncoding","UTF-8",strlen("UTF-8")); //可选参数，文本编码格式，支持UTF-8 默认为GBK
    ret = AIKIT_Start(ABILITY,AIKIT_Builder::build(paramBuilder),nullptr,&handle);
    printf("AIKIT_Start:%d\n",ret);
    if(ret != 0){
        goto  exit;
    }

    dataBuilder = AIKIT_DataBuilder::create();
    aiText_raw = AiText::get("text")->data(text.c_str(),text.length())->valid();
    dataBuilder->payload(aiText_raw);
    ret = AIKIT_Write(handle,AIKIT_Builder::build(dataBuilder));
    printf("AIKIT_Write:%d\n",ret);
    if(ret != 0){
        goto  exit;
    }

    while(ttsFinished != true){
        usleep(1000);
    }
    //想终止或者重启会话时，才调用AIKIT_End释放此路会话所占资源
    ret = AIKIT_End(handle);

 exit:   
    if(paramBuilder != nullptr){
        delete paramBuilder;
        paramBuilder = nullptr;
    }

    if(dataBuilder != nullptr){
        delete dataBuilder;
        dataBuilder = nullptr;
    }

    if (fin != nullptr){
        fclose(fin);
    }
    //程序真正退出时，才调用AIKIT_UnInit释放所有资源
    
}

void AEE_Init(){
    AIKIT_Configurator::builder()
        .app()
			.appID("")
			.apiSecret("")
            .apiKey("")
			.workDir("./")
        .auth()
            .authType(0)
		.log()
			.logLevel(LOG_LVL_INFO)
			.logPath("./");
    int ret = AIKIT_Init();
    if(ret != 0){
        printf("AIKIT_Init failed:%d\n",ret);
        return;
    }
    AIKIT_Callbacks cbs = {OnOutput,OnEvent,OnError};
    AIKIT_RegisterAbilityCallback(ABILITY,cbs);
    // AIKIT_RegisterCallback(cbs);      
            
}

int main() {
    AEE_Init();
    TestAisound();
    AIKIT_UnInit();
    return 0;
}
