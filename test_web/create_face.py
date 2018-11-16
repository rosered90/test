# coding:utf-8
import xlwt
import time
import random
import datetime
device_list = []
# 为了保证时间不重复，每生成一个时间就到列表中检查一下
# customer_code = "%s-%s-%s_%s" % (deviceid, up_time, mac, start_time)
# orc一个用户出现平均(1-10次)
# 每次停留时间在2-50s内

# "20181111%s" % random.randint(100000, 999999)


class Customer(object):
	def __init__(self, age, gender, otime, count, stay, date, deviceid, mac):
		self.age = age
		self.gender = gender
		self.otime = otime
		self.count = count
		self.date = date
		self.deviceid = deviceid
		self.mac = mac
		# self.stay = random.randint(2, 50)

	def stay_time(self):
		return random.randint(2, 50)

	def up_time(self):
		return self.date + str(random.randint(100000, 999999))

	def start_time(self):
		d = time.localtime(self.otime)
		return time.strftime("%Y%m%d%H%M%S", d)

	def appear_time(self):
		d = time.localtime(self.otime)
		return time.strftime("%Y-%m-%d %H:%M:%S", d)

	def disappear_time(self):
		d = time.localtime(self.otime + self.stay_time())
		return time.strftime("%Y-%m-%d %H:%M:%S", d)

	def get_customer_code(self):
		return "%s-%s-%s_%s" % (self.deviceid, self.up_time(), self.mac, self.start_time())


def get_age(s=18, e=60):
	return random.randint(s, e)


def get_gender():
	a = random.random()
	if a > 0.8:
		return 1
	else:
		return 0


def get_count():
	return random.randint(1, 10)


def get_stay():
	return random.randint(2, 50)

# s = (2018, 10, 1, 9, 0, 0, 0,0,0)
# e = (2018, 10, 1, 22, 0, 0, 0,0,0)


def get_day_random_time(s, e):
	start = time.mktime(s)
	end = time.mktime(e)
	time_list = []
	for i in range(100):
		t = random.randint(start, end)
		# date_tuple = time.localtime(t)
		# date = time.strftime("%Y-%m-%d %H:%M:%S", date_tuple)
		time_list.append(t)
	time_list.sort()
	date_list = []
	# for t in time_list:
	# 	date_tuple = time.localtime(t)
	# 	date = time.strftime("%Y%m%d%H%M%S", date_tuple)
	# 	date_list.append(date)
	return time_list


# c1 = Customer()

# for i in range(100):
# 	print(get_gender())

# date_list = get_day_random_time(s, e)

last_c = ""

wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet("Sheet1")

adf_list = ['20181001', '20181002', '20181003', '20181004', '20181005', '20181006', '20181007', '20181008', '20181009', '20181010', '20181011', '20181012', '20181013', '20181014', '20181015', '20181016', '20181017', '20181018', '20181019', '20181020', '20181021', '20181022', '20181023', '20181024', '20181025', '20181026', '20181027', '20181028', '20181029', '20181030']
a11_list = ['20181101', '20181102', '20181103', '20181104', '20181105', '20181106', '20181107', '20181108', '20181109', '20181110', '20181111', '20181112', '20181113', '20181114', '20181115']

p = 0
for x in a11_list:

	s = (2018, 11, int(x[-2:]), 9, 0, 0, 0, 0, 0)
	e = (2018, 11, int(x[-2:]), 22, 0, 0, 0, 0, 0)
	date_list = get_day_random_time(s, e)

	for i in range(100):
		# if last_c and last_c.count > 0:
		#
		# 	last_c = c
		# else:
		start_time = date_list[0]
		del date_list[0]
		d_r = random.random()
		if d_r < 0.5:
			deviceid = "orc_00002"
			mac = "22:22:b6:d6:9e:10"
		else:
			deviceid = "olay25"
			mac = "22:22:F5:F2:F6:F3"
		# else:
		# 	deviceid = "orc_00003"
		# 	mac = "22:22:bb:6a:db:15"
		c = Customer(get_age(), get_gender(), start_time, get_count(), get_stay(), x, deviceid, mac)
		print(c.get_customer_code())
		i = i + p
		for b in range(10):
			if b == 0:
				ws.write(i, b, c.get_customer_code())
			elif b == 1:
				ws.write(i, b, c.mac)
			elif b == 2:
				ws.write(i, b, c.appear_time())
			elif b == 3:
				ws.write(i, b, c.disappear_time())
			elif b == 4:
				ws.write(i, b, c.gender)
			elif b == 5:
				ws.write(i, b, c.age)
			elif b == 6:
				ws.write(i, b, "1")
			elif b == 7:
				ws.write(i, b, "186")
			elif b == 8:
				ws.write(i, b, "无表情")
			elif b == 9:
				ws.write(i, b, "7")
	p += 100

wb.save('adf.xls')
