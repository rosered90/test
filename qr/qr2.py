# _*_ coding:utf-8 _*_

import qrcode

img = qrcode.make("亲爱的辉哥哥，宝宝爱你，芳！")
img.save("hui.png")

import os


def print_directory(path):

	for child_path in os.listdir(path):
		ChildPath = os.path.join(path, child_path)
		if os.path.isdir(child_path):
			print_directory(child_path)
		else:
			print ChildPath