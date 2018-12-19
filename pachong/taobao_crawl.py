# _*_ coding:utf-8 _*_
import random

import requests
from bs4 import BeautifulSoup


def crawl_tb_product():
	"""
	抓取淘宝天猫产品
	:return:
	"""
	# 淘宝天猫产品链接
	url = 'https://www.tmall.com/mlist/cp_bGFibyBsYWJvILPH0rDSvcn6.html'
	# 浏览器伪装
	headers = {
		'Connection': 'keep-alive',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
	}
	# 利用代理
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
		soup = BeautifulSoup(r.text, "lxml")
		all_product = soup.find_all('div', attrs={'class': 'product'})
		name_list = []
		price_list = []
		client_list = []
		image_url_list = []
		for product in all_product:
			# 产品名称列表
			name = product.select('.productTitle a')[0].get_text()
			name_list.append(name)
			# 产品图片
			image_url = product.select('.productImg-wrap a img')[0].attrs['src']
			image_url_list.append('https:' + image_url)
			# 价格列表
			price =product.select('.productPrice em')[0].get_text()
			price_list.append(price)
			# 商家
			client =product.select('.productShop')[0].get_text().strip()
			client_list.append(client)
		# 打印抓取的列表
		print(name_list)
		print(price_list)
		print(client_list)
		print(image_url_list)
		print('查询成功！')
	except Exception as e:
		print(e)
		print('爬取网页失败！')


crawl_tb_product()