# _*_ coding:utf-8 _*_
import time

a = input('请输入时间字符串')
time_a = time.strptime(a, '%Y-%m-%d %H:%M:%S')
timeStamp = int(time.mktime(time_a))
print timeStamp