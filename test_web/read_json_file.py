# _*_　coding:utf-8 _*_
import json

with open('build.json', 'r', encoding='utf-8') as f:
	data = json.load(f)
	if '2018-11-12 00:00:00' in data['2018'].keys():
		print ('存在')
	else:
		print ('bucunzai不存在')
