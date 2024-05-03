from moviepy.editor import *
import cv2

# 创建一个函数，允许传递额外参数
def create_subtitle_function(text, font_size, y_position):
    def add_subtitle(frame):
        # 将 MoviePy 的帧转换为 OpenCV 的图像格式
        cv_image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # 在 OpenCV 图像上添加字幕
        font = cv2.FONT_HERSHEY_SIMPLEX
        textsize = cv2.getTextSize(text, font, font_size, 2)[0]
        textX = (cv_image.shape[1] - textsize[0]) // 2
        textY = y_position
        
        # 首先用黑色文字绘制轮廓，增加字幕的清晰度
        cv2.putText(cv_image, text, (textX, textY), font, font_size, (0, 0, 0), 2, lineType=cv2.LINE_AA)
        # 再用白色文字绘制上层
        # cv2.putText(cv_image, text, (textX, textY), font, font_size, (255, 255, 255), 2, lineType=cv2.LINE_AA)
        
        # 将 OpenCV 图像转换回 MoviePy 兼容的 RGB 格式
        return cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    
    return add_subtitle

def concat(video_file_lst, output_path):
    clip_lst = []
    for video_path in video_file_lst:
        clip = VideoFileClip(video_path)
        clip = clip.crossfadein(0.5)
        clip = clip.crossfadeout(0.5)
        clip_lst.append(clip)
    final_clip = concatenate_videoclips(clip_lst, method="compose")
    final_clip.write_videofile(output_path, audio_codec='aac')


def concat_v1():
    top = 0
    bottom = 0
    height = 320
    save_path = 'static/videos/HDTF_Demo/WRA_RoyBlunt/select/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        
    source_video_path = 'static/videos/HDTF_Demo/WRA_RoyBlunt/select/target.mp4'
    swap_sample1 = 'static/videos/HDTF_Demo/WRA_RoyBlunt/select/WRA_RoyBlunt_000_000_0_10_WDA_JohnSarbanes0_000_010_100_110.mp4'
    swap_sample2 = 'static/videos/HDTF_Demo/WRA_RoyBlunt/select/WRA_RoyBlunt_000_000_0_10_WDA_PatrickLeahy1_000_028_280_290.mp4'
    swap_sample3 = 'static/videos/HDTF_Demo/WRA_RoyBlunt/select/WRA_RoyBlunt_000_000_0_10_WRA_CoryGardner0_000_006_60_70.mp4'
    swap_sample4 = 'static/videos/HDTF_Demo/WRA_RoyBlunt/select/WRA_RoyBlunt_000_001_10_20_WDA_JoeManchin_000_006_60_70.mp4'
    swap_sample5 = 'static/videos/HDTF_Demo/WRA_RoyBlunt/select/WRA_RoyBlunt_000_001_10_20_WDA_TomCarper_000_011_110_120.mp4'
    swap_sample6 = 'static/videos/HDTF_Demo/WRA_RoyBlunt/select/WRA_RoyBlunt_000_002_20_30_WRA_MikeEnzi_000_026_260_270.mp4'
    swap_sample7 = 'static/videos/HDTF_Demo/WRA_RoyBlunt/select/WRA_RoyBlunt_000_003_30_40_WDA_BobbyScott_000_005_50_60.mp4'
    swap_sample8 = 'static/videos/HDTF_Demo/WRA_RoyBlunt/select/WRA_RoyBlunt_000_003_30_40_WDA_SherrodBrown1_000_022_220_230.mp4'
    swap_sample9 = 'static/videos/HDTF_Demo/WRA_RoyBlunt/select/WRA_RoyBlunt_000_004_40_58_WDA_ChrisCoons1_000_014_140_150.mp4'
    
    
    
    source_video = VideoFileClip(source_video_path).resize(height=height)
    # 重塑 source video只保留第一帧
    first_frame = source_video.get_frame(0)
    image_clip = ImageClip(first_frame)
    source_video = image_clip.set_duration(source_video.duration)
    custom_subtitle = create_subtitle_function("Source ID", 0.6, 15)
    source_video = source_video.fl_image(custom_subtitle)
    
    
    swap_sample1_video = VideoFileClip(swap_sample1).resize(height=height)
    custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    swap_sample1_video = swap_sample1_video.fl_image(custom_subtitle)
    
    swap_sample2_video = VideoFileClip(swap_sample2).resize(height=height)
    custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    swap_sample2_video = swap_sample2_video.fl_image(custom_subtitle)
    
    swap_sample3_video = VideoFileClip(swap_sample3).resize(height=height)
    custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    swap_sample3_video = swap_sample3_video.fl_image(custom_subtitle)
    
    swap_sample4_video = VideoFileClip(swap_sample4).resize(height=height)
    custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    swap_sample4_video = swap_sample4_video.fl_image(custom_subtitle)
    
    swap_sample5_video = VideoFileClip(swap_sample5).resize(height=height)
    custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    swap_sample5_video = swap_sample5_video.fl_image(custom_subtitle)
    
    swap_sample6_video = VideoFileClip(swap_sample6).resize(height=height)
    custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    swap_sample6_video = swap_sample6_video.fl_image(custom_subtitle)
    
    swap_sample7_video = VideoFileClip(swap_sample7).resize(height=height)
    custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    swap_sample7_video = swap_sample7_video.fl_image(custom_subtitle)
    
    
    swap_sample8_video = VideoFileClip(swap_sample8).resize(height=height)
    custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    swap_sample8_video = swap_sample8_video.fl_image(custom_subtitle)
    
    
    swap_sample9_video = VideoFileClip(swap_sample9).resize(height=height)
    custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    swap_sample9_video = swap_sample9_video.fl_image(custom_subtitle)
    
    
    
    final_clip = clips_array([[source_video, swap_sample1_video, swap_sample2_video, swap_sample3_video, swap_sample4_video],
                              [swap_sample5_video, swap_sample6_video, swap_sample7_video, swap_sample8_video, swap_sample9_video]])
    final_clip = final_clip.set_audio(swap_sample1_video.audio)
    final_clip = final_clip.subclip(0, 9.96)
    final_clip.write_videofile(os.path.join(save_path, 'concat.mp4'), audio_codec='aac')



if __name__ == '__main__':
    import os
    video_file_lst = ['static/videos/concat_zip_self_construct_vision_compare/RD_Radio21_000_003_30_48_concat.mp4',
                      'static/videos/concat_zip_self_construct_vision_compare/WDA_NancyPelosi0_000_012_120_130_concat.mp4',
                      'static/videos/concat_zip_self_construct_vision_compare/WRA_SamBrownback_000_009_90_100_concat.mp4',
                      'static/videos/concat_zip_self_construct_vision_compare/WRA_SteveDaines0_000_008_80_93_concat.mp4']
    output_path ='static/videos/concat_zip_self_construct_vision_compare/concat.mp4'
    concat(video_file_lst, output_path)
    
    # concat_v1()
    

