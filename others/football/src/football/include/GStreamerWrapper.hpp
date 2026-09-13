
#include <gst/gst.h>
#include <gst/app/gstappsink.h>

class GStreamerWrapper{
public:
    GStreamerWrapper(){
        gst_init(nullptr, nullptr);
        std::string gstreamer_cmd = "rtspsrc location=rtsp://192.168.1.120:8554/test ! rtph264depay ! h264parse config-interval=1 ! nvv4l2decoder ! video/x-raw(memory:NVMM) ! nvvidconv ! video/x-raw,format=BGRx ! videoscale ! video/x-raw,width=640,height=360 ! videoconvert ! video/x-raw,format=BGR ! queue max-size-buffers=5 max-size-bytes=0 max-size-time=50000000 leaky=downstream ! appsink name=appsink sync=false max-buffers=1 drop=1";
        pipeline_ = gst_parse_launch(gstreamer_cmd.c_str(), NULL);
        if(pipeline_==nullptr) std::cout << "gst_parse_launch failed" << std::endl;
        std::cout << "pipeline_: " << pipeline_ << std::endl;

        appsink_ = gst_bin_get_by_name(GST_BIN(pipeline_), "appsink");
        std::cout << "appsink_: " << appsink_ << std::endl;

        gst_app_sink_set_emit_signals(GST_APP_SINK(appsink_), true);
        gst_app_sink_set_drop(GST_APP_SINK(appsink_), true);
        gst_app_sink_set_max_buffers(GST_APP_SINK(appsink_), 1);
        gst_element_set_state(pipeline_, GST_STATE_PLAYING);

        std::cout << "gst_app_sink_pull_sample!" << std::endl;
        GstSample *sample = gst_app_sink_pull_sample(GST_APP_SINK(appsink_));
        if(!sample){
            std::cout << "empty sample in construction" << std::endl;
        }
        else{
            std::cout << "gst_sample_get_caps!" << std::endl;
            GstCaps *caps = gst_sample_get_caps(sample);
            if(!caps) std::cout << "cap is empty" << std::endl;
            std::cout << "gst_caps_get_structure!" << std::endl;
            GstStructure *structure = gst_caps_get_structure(caps, 0);
            std::cout << "gst_structure_get_int!" << std::endl;
            gst_structure_get_int(structure, "width", &width_);
            gst_structure_get_int(structure, "height", &hetght_);
            std::cout << "wh: " << width_ << " " << hetght_ << std::endl;
            gst_sample_unref(sample);
        }
    }

    ~GStreamerWrapper(){
        gst_element_set_state(pipeline_, GST_STATE_NULL);
        gst_object_unref(pipeline_);
    }

    std::tuple<int,int> GetFrameSize(){
        return std::make_tuple(width_, hetght_);
    }

    bool GetFrame(cv::Mat &frame){
        GstSample *sample = gst_app_sink_pull_sample(GST_APP_SINK(appsink_));
        if(!sample){
            std::cout << "empty sample" << std::endl;
            return false;
        }
        else{
            GstBuffer *buffer = gst_sample_get_buffer(sample);
            GstMapInfo map;
            gst_buffer_map(buffer, &map, GST_MAP_READ);
            memcpy(frame.data, map.data, frame.total() * frame.elemSize());
            gst_buffer_unmap(buffer, &map);
            gst_sample_unref(sample);
            return true;
        }
    }

private:
    GstElement *pipeline_ = nullptr;
    GstElement *appsink_ = nullptr;
    int width_ = 0;
    int hetght_ = 0;
};
