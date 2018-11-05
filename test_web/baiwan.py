# -*- coding: utf-8 -*-

import MySQLdb
import csv

class Handle:
	def __init__db(self):
		self.__mysql_db = MySQLdb.connect(host="127.0.0.1", user="root", db="smart_shelf_orc", passwd="password", port=3306)
		self.mysql_cur = self.__mysql_db.cursor()
		self.seq = 0

	def __init__(self):
		self.__init__db()

	def _release_db(self):
		self.mysql_cur.close()
		self.__mysql_db.close()

	def _do(self):
		self.mysql_cur.arraysize = 50
		select_sql = "SELECT event_type_code,customer_code,event_content AS event_type_code FROM smart_shelf_orc.api2_eventlog"
		print select_sql
		self.mysql_cur.execute(select_sql)
		count = 0
		csvfile = file('all_user.csv', 'wb')
		print dir(csv)
		writers = csv.writer(csvfile)
		writers.writerow(['event_id', 'customer_id', 'event_content'])
		while 1:
			lines = self.mysql_cur.fetchmany(50)
			if len(lines) == 0:
				break
			for i in lines:
				print i
				writers.writerows([i])
		csvfile.close()

def main():
	p = Handle()
	p._do()
	p._release_db()

if __name__ == "__main__":
	main()
