import random
from datetime import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler


def job_func(text):
	number = random.randint(0, 9)
	print(text + str(number))

scheduler = BackgroundScheduler()
# 在 2018-12-25 14:00:00 时刻运行一次 job_func 方法

scheduler.add_job(job_func, 'interval', seconds=10, start_date=datetime(2018, 12, 25, 17, 13, 0), end_date=datetime(2018, 12, 25, 18, 13, 0), args=['I love Job'])
# 在 2018-12-25 14:00:01 时刻运行一次 job_func 方法
scheduler.add_job(job_func, 'date', run_date='2018-12-25 14:00:01', args=['text'])

scheduler.start()