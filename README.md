# 测试文档
    此文档是为了记录在平时工作时需要测试功能的文档，也可以用来查看部分功能
## 爬虫
## 二维码的生成
## 人脸识别
## 基于树莓派的python环境下视频播放
### 技术简要<hr/>
#### 采用的是python的opencv，在windows安装问题不大，放在服务上安装可能会遇到点问题<br/>
        pip install opencv-python
#### 对于屏幕的适配问题我采用的tkiner
```
import tkinter
    win = tkinter.Tk()
    # 获得设备的宽高
    win_width = win.winfo_screenwidth()
    win_height = win.winfo_screenheight()
```

## python自动化测试 - pytest
### 安装pytest
        pip install -U pytest
### 安装好后验证安装的版本
        py.test --version
### 如何编写pytest测试样例
需要按照下面的规则：
* 测试文件以test_开头（以_test结尾也是可以的）
* 测试类以Test开头，并且不能带有__init__方法
* 测试函数以test__开头
### 简单实例

```#content of test_sample.py
 
def func(x):
    return x+1
 
def test_func():
    assert fun(2) = 4
```
#### 运行测试案例
在当前目录下执行命令：
        py.test   
#### 如果有多个需要测试的类可以采用知名方法运行
```
py.test               # run all tests below current dir
py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test -k stringexpr # only run tests with names that match the
                      # the "string expression", e.g. "MyClass and not method"
                      # will select TestMyClass.test_something
                      # but not TestMyClass.test_method_simple
py.test test_mod.py::test_func # only run tests that match the "node ID",
			       # e.g "test_mod.py::test_func" will select
                               # only test_func in test_mod.py
```
