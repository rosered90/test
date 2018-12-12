from json import dump, dumps

import requests
import json

URL = 'XXXXXX'
image_path = 'D:\\fang\\images\\XX'
file_open = open(image_path, 'rb')
suffix = image_path.split('.')[-1]
files = {"image": file_open}
data = {
	'app_id': 'test',
	'app_key': 'test',
	'user_uid': 'test',
	'own': True,
	'machine_id': 'default',
}
r = requests.post(URL, data=data, files=files)
if r.ok:
	skin_json = r.json()
	with open('skin_test1.txt', 'w') as f:
		f.write(str(json.dumps(skin_json)))
	print(skin_json)





# byte_stream = io.BytesIO(image)  # 把请求到的数据转换为Bytes字节流(这样解释不知道对不对，可以参照[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431918785710e86a1a120ce04925bae155012c7fc71e000)的教程看一下)
#
# roiImg = Image.open(byte_stream)  # Image打开二进制流Byte字节流数据
#
# imgByteArr = io.BytesIO()  # 创建一个空的Bytes对象
#
# roiImg.save(imgByteArr, format='PNG')  # PNG就是图片格式，我试过换成JPG/jpg都不行
#
# imgByteArr = imgByteArr.getvalue()  # 这个就是保存的二进制流
#
#
# files = {"image_file": imgByteArr}