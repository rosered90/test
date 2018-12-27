# coding:utf-8
import time
import hashlib
import traceback

import requests
from PIL import Image

URL = "http://ap.api.wmwbeautysalon.com/service/v1"
# URL = "http://aapi.dev.wmwbeautysalon.com/service/v1"
APPID = "d101f389410376df"
APPSECRET = "c338a12ff500c397e888a05cb2188988"
# APPID = "d101f389410376df"
# APPSECRET = "c338a12ff500c397e888a05cb2188988"


def auth():
	now = str(int(time.time()))
	raw_string = "appId=%stimeStamp=%s%s" % (APPID, now, APPSECRET)
	auth_sign = hashlib.md5(raw_string.encode('utf8')).hexdigest()
	return auth_sign, now


def trans_img(img_path):
	file_name = None
	try:
		img = Image.open(img_path)
		# Image.ANTIALIAS表示缩放的是高质量 参考：https://www.jb51.net/article/91492.htm
		img = img.resize((960, 1280), Image.ANTIALIAS)
		file_name = '%s.png' % int(time.time())
		img.save('%s' % file_name)
	except Exception as e:
		exc_str = traceback.format_exc()
		print(exc_str)
	return file_name


def call():
	auth_sign, now = auth()
	# img = trans_img("c.png")
	if True:
		url = URL + "/philab/4d/uploadImage?appId=%s" % (APPID)
		files = {"image": open('c.png', 'rb')}
		data = {
			"appId": APPID, "timeStamp": now, "authSign": auth_sign,
		}
		try:
			r = requests.post(url, data=data, files=files)
			if r.ok:
				print(r.text)
			else:
				print(r.status_code)
		except Exception as e:
			exc_str = traceback.format_exc()
			print(exc_str)
	else:
		print('error')


if __name__ == '__main__':
	# trans_img('a.jpg')
	call()
