# _*_ coding:utf-8 _*_

import qrcode

ipa="www.baidu.com"
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10,
                   border=2,
                   )  # 设置图片格式
qr.add_data(ipa)
qr.make(fit=True)
img=qr.make_image()
img.save('baidu.png')

# img = qrcode.make("亲爱的辉哥哥，宝宝爱你，芳！")
# img.save("hui.png")

# import os
#
#
# def print_directory(path):
#
# 	for child_path in os.listdir(path):
# 		ChildPath = os.path.join(path, child_path)
# 		if os.path.isdir(child_path):
# 			print_directory(child_path)
# 		else:
# 			print ChildPath