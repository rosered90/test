# 测试文档
    此文档是为了记录在平时工作时需要测试功能的文档，也可以用来查看部分功能
## 爬虫
## 二维码的生成
## 人脸识别
## 基于树莓派的python环境下视频播放
### 技术简要<hr/>
#### 采用的是python的opencv，在windows安装问题不大，放在服务上安装可能会遇到点问题<br/>
>pip install opencv-python<br/>
#### 对于屏幕的适配问题我采用的tkiner
>import tkinter
    win = tkinter.Tk()<br/>
    # 获得设备的宽高<br/>
    win_width = win.winfo_screenwidth()<br/>
    win_height = win.winfo_screenheight()<br/>
