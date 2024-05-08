from moviepy.editor import *
import cv2
import os

# 创建一个函数，允许传递额外参数
def create_subtitle_function(text, font_size, x_position, y_position):
    def add_subtitle(frame):
        # 将 MoviePy 的帧转换为 OpenCV 的图像格式
        cv_image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # 在 OpenCV 图像上添加字幕
        font = cv2.FONT_HERSHEY_SIMPLEX
        textsize = cv2.getTextSize(text, font, font_size, 2)[0]
        # textX = (cv_image.shape[1] - textsize[0]) // 2
        textX = x_position
        textY = y_position
        
        # 首先用黑色文字绘制轮廓，增加字幕的清晰度
        cv2.putText(cv_image, text, (textX, textY), font, font_size, (0, 0, 0), 2, lineType=cv2.LINE_AA)
        # 再用白色文字绘制上层
        # cv2.putText(cv_image, text, (textX, textY), font, font_size, (255, 255, 255), 2, lineType=cv2.LINE_AA)
        
        # 将 OpenCV 图像转换回 MoviePy 兼容的 RGB 格式
        return cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    
    return add_subtitle

def concat(video_file_lst, output_path, time=None):
    clip_lst = []
    for i, video_path in enumerate(video_file_lst):
        if i > 0:
            clip = VideoFileClip(video_path)
            if time is not None:
                clip.subclip(time[i])
            clip = clip.crossfadein(0.5)
            clip = clip.crossfadeout(0.5)
            clip_lst.append(clip)
        else:
            clip = VideoFileClip(video_path)
            if time is not None:
                clip.subclip(time[i])
            clip = clip.crossfadeout(0.5)
            clip_lst.append(clip)
    final_clip = concatenate_videoclips(clip_lst, method="compose")
    final_clip.write_videofile(os.path.join(output_path, 'concat.mp4'), audio_codec='aac')
    
    
def concat_v2(video_file_lst, output_path):
    clip_lst = []
    for video_path in video_file_lst:
        clip = VideoFileClip(video_path)
        clip_lst.append(clip)
    final_clip = clips_array([clip_lst])
    final_clip = final_clip.set_audio(clip.audio)
    # final_clip = final_clip.subclip(0, 9.96)
    final_clip.write_videofile(os.path.join(output_path, 'concat.mp4'), audio_codec='aac')

    


def concat_v1(root_path):
    top = 0
    bottom = 0
    height = 320
    save_path = root_path
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        
    # source_video_path = 'static/videos/HDTF_Demo/WRA_RoyBlunt/select/target.mp4'
    source_video_path = os.path.join(root_path, 'target.mp4')
    swap_video_path_lst = [os.path.join(root_path, item) for item in os.listdir(root_path) if 'target' not in item and '.mp4' in item and 'concat' not in item]
    
    assert len(swap_video_path_lst) == 9
    
    
    swap_sample1 = swap_video_path_lst[0]
    swap_sample2 = swap_video_path_lst[1]
    swap_sample3 = swap_video_path_lst[2]
    swap_sample4 = swap_video_path_lst[3]
    swap_sample5 = swap_video_path_lst[4]
    swap_sample6 = swap_video_path_lst[5]
    swap_sample7 = swap_video_path_lst[6]
    swap_sample8 = swap_video_path_lst[7]
    swap_sample9 = swap_video_path_lst[8]
    
    
    
    
    # custom_subtitle = create_subtitle_function("Source ID", 0.6, 15)
    # source_video = source_video.fl_image(custom_subtitle)
    
    
    swap_sample1_video = VideoFileClip(swap_sample1).resize(height=height)
    # custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    # swap_sample1_video = swap_sample1_video.fl_image(custom_subtitle)
    
    source_video = VideoFileClip(source_video_path).resize(height=height)
    # 重塑 source video只保留第一帧
    first_frame = source_video.get_frame(0)
    image_clip = ImageClip(first_frame)
    source_video = image_clip.set_duration(swap_sample1_video.duration)
    
    swap_sample2_video = VideoFileClip(swap_sample2).resize(height=height)
    # custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    # swap_sample2_video = swap_sample2_video.fl_image(custom_subtitle)
    
    swap_sample3_video = VideoFileClip(swap_sample3).resize(height=height)
    # custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    # swap_sample3_video = swap_sample3_video.fl_image(custom_subtitle)
    
    swap_sample4_video = VideoFileClip(swap_sample4).resize(height=height)
    # custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    # swap_sample4_video = swap_sample4_video.fl_image(custom_subtitle)
    
    swap_sample5_video = VideoFileClip(swap_sample5).resize(height=height)
    # custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    # swap_sample5_video = swap_sample5_video.fl_image(custom_subtitle)
    
    swap_sample6_video = VideoFileClip(swap_sample6).resize(height=height)
    # custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    # swap_sample6_video = swap_sample6_video.fl_image(custom_subtitle)
    
    swap_sample7_video = VideoFileClip(swap_sample7).resize(height=height)
    # custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    # swap_sample7_video = swap_sample7_video.fl_image(custom_subtitle)
    
    
    swap_sample8_video = VideoFileClip(swap_sample8).resize(height=height)
    # custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    # swap_sample8_video = swap_sample8_video.fl_image(custom_subtitle)
    
    
    swap_sample9_video = VideoFileClip(swap_sample9).resize(height=height)
    # custom_subtitle = create_subtitle_function("SwapTalk", 0.6, 15)
    # swap_sample9_video = swap_sample9_video.fl_image(custom_subtitle)
    
    
    
    final_clip = clips_array([[source_video, swap_sample1_video, swap_sample2_video, swap_sample3_video, swap_sample4_video],
                              [swap_sample5_video, swap_sample6_video, swap_sample7_video, swap_sample8_video, swap_sample9_video]])
    final_clip = final_clip.set_audio(swap_sample1_video.audio)
    final_clip = final_clip.subclip(0, 10)
    final_clip.write_videofile(os.path.join(save_path, 'concat.mp4'), audio_codec='aac')




def add_external_subtitle_to_video(subtitle_text, input_video_path, output_video_path, fontsize=24, font='Arial'):
    """
    将字幕添加在视频画面下方的扩展区域。

    :param subtitle_text: 字幕内容字符串
    :param input_video_path: 输入视频文件的路径
    :param output_video_path: 输出视频文件的路径
    :param fontsize: 字体大小 (默认24)
    :param font: 字体类型 (默认Arial)
    """
    # 加载原始视频
    video = VideoFileClip(input_video_path)
    original_width, original_height = video.size

    # 创建一个 TextClip 来表示字幕
    txt_clip = TextClip(
        subtitle_text,
        fontsize=fontsize,
        color='white',
        font=font,
        stroke_color='white',
        stroke_width=2
    ).set_duration(video.duration)

    # 计算字幕的高度，并扩展视频的高度来放置字幕
    subtitle_height = txt_clip.h
    new_height = original_height + subtitle_height

    # 将字幕移动到扩展画布的底部
    txt_clip = txt_clip.set_position(("center", original_height))

    # 扩展画布并将原视频和字幕合成
    extended_video = video.margin(bottom=subtitle_height, color=(0, 0, 0))
    result = CompositeVideoClip([extended_video, txt_clip])


    # 导出带字幕的视频
    result.write_videofile(output_video_path, audio_codec='aac')
        

if __name__ == '__main__':
    '''
    lst = ['static/videos/HDTF_New/RD_Radio11_001_select',
           'static/videos/HDTF_New/WDA_DebHaaland_select',
           'static/videos/HDTF_New/WDA_KatieHill_select',
           'static/videos/HDTF_New/WDA_MichaelBennet_select',
           'static/videos/HDTF_New/WRA_RoyBlunt_select']
    for item in lst:
        concat_v1(item)
    
    
    
    
    '''
    video_file_lst = ['static/videos/HDTF_New/WDA_DebbieStabenow_target_select/concat_add_subs.mp4',
                      'static/videos/HDTF_New/WDA_MichaelBennet_target_select/concat_add_subs.mp4',
                      'static/videos/HDTF_New/WDA_KatieHill_target_select/concat_add_subs.mp4',
                      'static/videos/HDTF_New/WRA_RoyBlunt_target_select/concat_add_subs.mp4',
                    'static/videos/HDTF_New/WDA_KatieHill_select/concat_add_subs.mp4',
                      'static/videos/HDTF_New/WDA_MichaelBennet_select/concat_add_subs.mp4',
                      'static/videos/HDTF_New/RD_Radio11_001_select/concat_add_subs.mp4',
                      'static/videos/HDTF_New/WRA_RoyBlunt_select/concat_add_subs.mp4',
                      'static/videos/HDTF_New/WDA_DebHaaland_select/concat_add_subs.mp4']
    output_path = './static/videos/HDTF_New'
    
    concat(video_file_lst, output_path)
    
    # subtitle_text = 'Same Source Different Target'
    # input_video_path = 'static/videos/HDTF_New/WRA_RoyBlunt_select/concat.mp4'
    # output_video_path = 'static/videos/HDTF_New/WRA_RoyBlunt_select/concat_add_subs.mp4'
    
    # add_external_subtitle_to_video(subtitle_text, input_video_path, output_video_path, fontsize=30)
    
    
    
    

    
    
    

