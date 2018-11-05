# _*_ coding:utf-8 _*_
import os, json

djson = {'d':dict(name="hello"), 'str1':'hello'}
JStr = json.dumps(djson, ensure_ascii=False)
print (JStr)

with open('build.json', 'w', encoding='utf-8') as f:
	f.write(JStr)