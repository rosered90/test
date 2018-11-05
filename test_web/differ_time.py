# coding:utf-8
#__author__= 'fang'
#__date__ = '2018/10/17 0017 23:23'

import datetime

now = datetime.datetime.now()
now1 = now + datetime.timedelta(minutes=8)
now2 = now + datetime.timedelta(minutes=14)
now3 = now + datetime.timedelta(minutes=22)
now4 = now + datetime.timedelta(minutes=33)
list = [now, now1, now2, now3, now4]
len = len(list)
time_list = []

def differ_time():
	n = 0
	for i in range(len-1):
		last_time = list[i]
		n += 1
		if i <= len - 1:
			time = list[n]
			if time - last_time <= datetime.timedelta(minutes=10):
				time_list.append(time)
				if last_time not in time_list:
					time_list.append(last_time)
		print (time_list)

differ_time()