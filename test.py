# -*- coding: utf-8 -*-
import time
import json
import hashlib
import urllib2
import re


def formatQueryParaMap(paraMap):
	"""格式化参数，签名验证过程需要使用"""
	slist = sorted(paraMap)
	buff = []
	for k in slist:
		v = paraMap[k]
		buff.append("{0}={1}".format(k, v))
	return "&".join(buff)


def test_call():
	# url = "https://card.haotunet.com/card_api/api/"
	url = "http://127.0.0.1:8999/card_api/api/"
	# key = "meiyangkey"
	key = "42"
	appsecret = "qimensecrect"
	# appsecret = "meiyangsecrect"
	# commodity_code = "cc00209001"  # 本地卡券测试
	# commodity_code = "cc00212001"  # 本地接口测试
	commodity_code = "cc00217001"  # 多接口测试
	timestamp = time.time()
	dict_data = {"key": key, "appsecret": appsecret, "commodity": commodity_code, "timestamp": str(timestamp),
	             "phone": "17078987914", "number": "1", "trade_id": "NO2017091211141018000005", "notify_url": "http://weixin.ahqmrcb.com/interface/call_back/"}
	format_string = formatQueryParaMap(dict_data)
	sign_string = hashlib.md5(format_string).hexdigest()
	del dict_data['appsecret']
	upload_string = formatQueryParaMap(dict_data)
	upload_string += ("&sign=" + sign_string)
	url += ("?" + upload_string)
	data = json.loads(urllib2.urlopen(url).read())
	print(data)

test_call()