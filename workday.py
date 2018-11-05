# _*_ coding:utf-8 _*_

import json,urllib
from urllib import urlencode

url = 'http://api.k780.com:88/'
params = {
  'app' : 'life.workday',
  'date' : '20181002',
  'appkey' : '10003',
  'sign' : 'b59bc3ef6191eb9f747dd4e83c99f2a4',
  'format' : 'json',
}
params = urlencode(params)

f = urllib.urlopen('%s?%s' % (url, params))
nowapi_call = f.read()
#print content
a_result = json.loads(nowapi_call)
if a_result:
  if a_result['success'] != '0':
    print a_result['result']['workmk'] # 1为工作日，2为假日
  else:
    print a_result['msgid']+' '+a_result['msg']
else:
  print 'Request nowapi fail.'


# def gen_dates(b_date, days):
# 	day = datetime.timedelta(days=1)
# 	for i in range(days):
# 		yield b_date + day * i
#
#
# def work_day():
# 	"""
# 	求每个月的工作日
# 	:return:
# 	"""
# 	work_day_all = 0
# 	# 求今天
# 	today_str = datetime.datetime.now().strftime('%Y%m%d')
# 	# 求月初和月末
# 	monthday = calendar.monthrange(int(today_str[:4]), int(int(today_str[4:6])))[1]
# 	start_time = datetime.date(int(today_str[:4]), int(int(today_str[4:6])), 1)
# 	end_time = datetime.date(int(today_str[:4]), int(int(today_str[4:6])), monthday)
# 	url = 'http://api.k780.com:88/?'
# 	for d in gen_dates(start_time, (end_time-start_time).days):
# 		d_str = d.strftime('%Y%m%d')
# 		params = {
# 			'app': 'life.workday',
# 			'date': d_str,
# 			'appkey': '10003',
# 			'sign': 'b59bc3ef6191eb9f747dd4e83c99f2a4',
# 			'format': 'json',
# 		}
# 		f = requests.get(url, params)
# 		nowapi_call = f.text
# 		# print content
# 		a_result = json.loads(nowapi_call)
# 		if a_result:
# 			if a_result['success'] != '0':
# 				is_workday = a_result['result']['workmk']  # 1为工作日，2为假日
# 				if is_workday == '1':
# 					work_day_all += 1
# 			else:
# 				return None
# 		else:
# 			return None
#
# 	# return work_day_all
#
# a = work_day()