# _*_ coding _*_
import datetime
import requests
import json

def work_day(start_time, end_time):
	# 工作日
	work_day_all = 0
	# 休息日
	rest_day = 0
	# 节假日
	holiday_day = 0
	# 放置字典
	not_work_day_dict = {}
	# 求今天
	# today_str = datetime.datetime.now().strftime('%Y%m%d')
	# 求每个月的工作日
	# 求月初和月末
	# monthday = calendar.monthrange(int(today_str[:4]), int(int(today_str[4:6])))[1]
	# start_time = datetime.date(int(today_str[:4]), int(int(today_str[4:6])), 1)
	# end_time = datetime.date(int(today_str[:4]), int(int(today_str[4:6])), monthday)
	start_time_date = datetime.datetime(int(start_time[0:4]), int(start_time[5:7]), int(start_time[8:10]))

	end_time_date = datetime.datetime(int(end_time[0:4]), int(end_time[5:7]), int(end_time[8:10]))
	n = 0
	while start_time_date <= end_time_date:
		year = datetime.datetime.strftime(start_time_date, '%Y')
		start_time_str = start_time_date.strftime('%Y%m%d')
		# 放入字典的时间
		start_time_dict_str = start_time_date.strftime('%Y-%m-%d 00:00:00')
		start_time_date += datetime.timedelta(days=1)
		# server_url = "http://www.easybots.cn/api/holiday.php?d=" # 截至到2017年，需要授权码
		server_url = "http://api.goseek.cn/Tools/holiday?date="
		vop_response = requests.get(server_url + start_time_str)
		vop_data = json.loads(vop_response.text)
		if vop_data['data'] == 1:
			not_work_day_dict.setdefault(year, {})[start_time_dict_str] = 1
			n += 1
		elif vop_data['data'] == 2:
			not_work_day_dict.setdefault(year, {})[start_time_dict_str] = 1
			n += 1
		else:
			work_day_all = 'error'
		print (n)

	print (work_day_all)
	return work_day_all, not_work_day_dict

work_day_all, not_work_day_dict = work_day('2018-01-01', '2022-12-31')
JStr = json.dumps(not_work_day_dict, ensure_ascii=False)
print (JStr)

with open('build.json', 'a', encoding='utf-8') as f:
	f.write(JStr)