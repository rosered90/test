# _*_* coding: utf-8 _*_
from datetime import datetime,timedelta

def time1(start_time, end_time):
	"""
	根据一段时间求该段时间的每天固定值
	:param start_time:
	:param end_time:
	:return:
	"""
	time_list = []
	while end_time.day - start_time.day >= 1:
		i = 1
		if end_time.day - start_time.day >= 1:
			# 求改天的晚上9点
			this_day_night = datetime.strftime(start_time, '%Y-%m-%d') + str(' 21:00')
			if i == 1:
				time_list.append((datetime.strftime(start_time, '%Y-%m-%d %H:%M'), this_day_night))
			else:
				this_day_morning = start_time + timedelta(hours=9, minutes=0, seconds=0)
				time_list.append((datetime.strftime(this_day_morning, '%Y-%m-%d %H:%M'),
				                  this_day_night))
			start_time_str = datetime.strftime(start_time + timedelta(days=1), '%Y-%m-%d')
			start_time = datetime.strptime(start_time_str, '%Y-%m-%d') + timedelta(hours=9, minutes=0)
			i += 1
		else:
			# 最后一天的开始时间
			this_day_morning = datetime.strftime(start_time, '%Y-%m-%d') + str(' 09:00')
			time_list.append((this_day_morning, datetime.strftime(end_time, '%Y-%m-%d %H:%M')))
	else:
		time_list.append(
			(datetime.strftime(start_time, '%Y-%m-%d %H:%M'), datetime.strftime(end_time, '%Y-%m-%d %H:%M')))
	print (time_list)

start_time = datetime.strptime('2018-12-3 12:00', '%Y-%m-%d %H:%M')
end_time = datetime.strptime('2018-12-5 21:00', '%Y-%m-%d %H:%M')
time1(start_time, end_time)