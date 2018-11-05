# _*_ coding:utf-8 _*_

import requests
import json

url = 'http://127.0.0.1:8000/device/device/'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
content = json.dumps(r.text)
print (content)