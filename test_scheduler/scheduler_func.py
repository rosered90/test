import random
from datetime import datetime
from datetime import date

def job_func(text):
	number = random.randint(0, 9)
	print(text + str(number))