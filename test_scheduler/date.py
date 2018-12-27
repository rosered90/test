from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from test_scheduler.scheduler_func import job_func

scheduler = BackgroundScheduler()
# 在 2018-12-25 14:00:00 时刻运行一次 job_func 方法

scheduler.add_job(job_func, 'interval', seconds=10, start_date=datetime(2018, 12, 27, 14, 13, 0), end_date=datetime(2018, 12, 27, 18, 13, 0), args=['I love Job'])
# 在 2018-12-25 14:00:01 时刻运行一次 job_func 方法
scheduler.add_job(job_func, 'date', run_date='2018-12-25 14:00:01', args=['text'])

scheduler.start()