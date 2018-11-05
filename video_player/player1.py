# _*_ coding:utf-8 _*_
import cv2
import cv2 as cv
import tkinter
import sys


win = tkinter.Tk()
# 获得设备的宽高
win_width = win.winfo_screenwidth()
win_height = win.winfo_screenheight()

wnd = 'OpenCV Video'

# cap = cv2.VideoCapture('C:\\Users\\Administrator\\Desktop\\video.mp4')
cap = cv2.VideoCapture(sys.argv[1])

while(cap.isOpened()):
    ret, frame = cap.read()
    # 全屏播放, flags=0视频的大小会根据跟随屏幕的大小而改变
    cv2.namedWindow(wnd,  flags=0)
    cv2.resizeWindow(wnd,win_width, win_height)
    # 视频总帧数
    frame_count= cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # capture frame-by-frame
    cv2.imshow(wnd, frame)
    k = cv2.waitKey(50)

    # 循环视频播放，到达最后一帧时，再返回第一帧
    # if cap.get(cv2.CAP_PROP_POS_FRAMES) == (frame_count - 3):
    #     cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    #q键退出
    if (k & 0xff == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()