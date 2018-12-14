# _*_ coding:utf-8 _*_
import json
import random

import requests
import time
from bs4 import BeautifulSoup


def get_detail():
	# url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=557642631412&spuId=1006326018&sellerId=3399871558&order=3&currentPage=1&append=0&content=1&callback=jsonp133'
	# url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=577861243471&spuId=1064001268&sellerId=3399871558&order=3&currentPage=1&append=0&content=1&callback=jsonp458'
	# url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=557534409377&spuId=1006326018&sellerId=3399871558&order=3&currentPage=1&append=0&content=1&callback=jsonp1204'
	url = 'https://drcilabohzp.tmall.com/category.htm?spm=a1z10.1-b-s.w5001-16986592042.5.114b5175hQRaYX&search=y&scene=taobao_shop'
	# 浏览器伪装
	headers = {'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'zh-CN,zh;q=0.9',
	'cookie': 'cna=Qm6fDr1qxBUCAXrrVMDwN+zT; lid=%E9%92%A4%E7%BB%AB%E5%B0%8F%E8%BD%A9; hng=CN%7Czh-CN%7CCNY%7C156; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; UM_distinctid=16530f039d87c0-0118b4024786c4-323b5b03-1fa400-16530f039d9a33; enc=0PgNaQFTnH%2BlTBeeoYyTfq8rnx3A8nrYa3aGRSXK0lxdHKvJEsO3ak7OpeVV1VyZ%2FnGhuuhrk3yNzm1ncVihhg%3D%3D; x=__ll%3D-1%26_ato%3D0; uss=""; sm4=330100; t=f028dd88d3907bd690b9ea1ab534e34e; uc3=vt3=F8dByR1RmP%2FZE0Wj7Ec%3D&id2=UUwVYeEjK6JzgQ%3D%3D&nk2=jdRHB6VVAgg%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; tracknick=%5Cu94A4%5Cu7EEB%5Cu5C0F%5Cu8F69; lgc=%5Cu94A4%5Cu7EEB%5Cu5C0F%5Cu8F69; _tb_token_=5b47b1ed7b4d3; cookie2=126f8589aa92e040bb2a68c9c2d2890d; _m_h5_tk=7839d3225186eeca0c6237fd908c8bba_1544709151498; _m_h5_tk_enc=07a620a8548f8f244e8268a80cd0cdfb; isg=BEhILiAigHlwu-ky34GgRr2XGbaaWazVQ6v4HgL5lEO23ehHqgF8i97bUfUIbWTT',
	'referer': 'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16986360983.68.584a5e78Zei6kW&id=574745946207&rn=d76e34969d2e2ed171a2a5a5fc193cfe&abbucket=16&skuId=3762342132655',
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
	proxys = ['61.135.217.7	80',
	'58.56.108.226	43296',
	'58.240.232.126	57505',
	'182.111.64.7	41766',
	'59.32.37.118	8010',
	'114.225.169.36	53128',
	'59.173.74.169	8010',
	'121.31.155.184	8123',
	'121.31.192.215	8123',
	'175.175.216.210	1133',
	'13.121.242.49	808',
	'115.219.109.1	8010']
	print(random.choice(proxys))
	p = random.choice(proxys)
	ip = p.strip('\n').split('\t')
	proxy = 'http:\\' + ip[0] + ':' + ip[1]
	proxies = {'proxy': proxy}
	try:
		r = requests.get(url, headers=headers, proxies=proxies)
		text = r.text[12:-1]
		total_json = json.loads(text)
		# 总条目
		total_items = total_json["rateDetail"]["paginator"]["items"]
		rate_list = total_json["rateDetail"]["rateList"]
		i = 0
		for rate in rate_list:
			# 抓取买的什么：auctionSku
			product = rate['auctionSku']
			# 评论的时间： rateDate
			date = rate['rateDate']
			# 评论的内容：rateContent
			content = rate['rateContent']
			# 如果 有图片，抓取图片的路径： pics
			if 'pics' in rate:
				# 可能不止一张图片
				image = rate['pics']
			print('第%s个评论' % i)
			print(product)
			print(date)
			print(content)
			i +=1
			time.sleep(1)

		print('查询成功！')
	except Exception as e:
		print('爬取网页失败！')


get_detail()
