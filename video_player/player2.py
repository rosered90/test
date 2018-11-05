# -*- coding: utf-8 -*- 
# 使用OpenCV播放视频
import cv2

wnd = 'OpenCV Video'

# 获得视频的格式
videoCapture = cv2.VideoCapture('C:\\Users\\Administrator\\Desktop\\video.mp4')

# 获得码率及尺寸
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

cv2.namedWindow(wnd, flags=0)
cv2.resizeWindow(wnd, size[0] / 2, size[1] / 2)

# 读帧
success, frame = videoCapture.read()

while success:
	cv2.imshow(wnd, frame)  # 显示
	cv2.waitKey(1000 / int(fps))  # 延迟
	success, frame = videoCapture.read()  # 获取下一帧