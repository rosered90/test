# -*- coding: utf-8 -*-
import datetime
from dateutil.rrule import *
import json

import requests


def work_day(start_time, end_time):
	res = []
	# 求今天
	# today_str = datetime.datetime.now().strftime('%Y%m%d')
	# 求每个月的工作日
	# 求月初和月末
	# monthday = calendar.monthrange(int(today_str[:4]), int(int(today_str[4:6])))[1]
	# start_time = datetime.date(int(today_str[:4]), int(int(today_str[4:6])), 1)
	# end_time = datetime.date(int(today_str[:4]), int(int(today_str[4:6])), monthday)
	start_time_date = datetime.datetime(int(start_time[0:4]), int(start_time[5:7]), int(start_time[8:10]))
	end_time_date = datetime.datetime(int(end_time[0:4]), int(end_time[5:7]), int(end_time[8:10]))
	start_time1 = start_time_date
	while start_time_date <= end_time_date:
		start_time_str = start_time_date.strftime('%Y%m%d')
		res.append(start_time_date)
		start_time_date += datetime.timedelta(days=1)
	print res

work_day('2018-09-12', '2018-10-07')


def get_date_among_two_date(start_time_srt, end_time_str):
	start_time = datetime.datetime(int(start_time_srt[0:4]), int(start_time_srt[5:7]), int(start_time_srt[8:10]))
	end_time = datetime.datetime(int(end_time_str[0:4]), int(end_time_str[5:7]), int(end_time_str[8:10]))
	print list(rrule(DAILY, dtstart=start_time, until=end_time))

get_date_among_two_date('2018-09-12', '2018-10-07')