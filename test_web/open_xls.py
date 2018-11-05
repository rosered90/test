# _*_ coding:utf-8 _*_

def coff():
	Goods = [
		{u"可乐": 5},
		{u"矿泉水": 3},
		{u"黄鹤楼香烟": 20}
	]
	num = 0
	for item in Goods:
		num += 1
		for i, j in item.items():
			j_j = str(j)
			print(num, i, j_j + "元")
	# while True:
	count = 0
	numaa = True
	while numaa:
		Innum = input("请输入商品序号：")
		if Innum.isdecimal():
			Innum = Innum.strip()
			Innum = int(Innum)

		else:
			print("您的输入有误！请重新输入")
			continue
		if Innum > 0 and Innum <= len(Goods):
			for x, y in Goods[Innum - 1].items():
				y_y = str(y)
				print(x, y_y + "元")
			count += y
			m = input("是否继续购物(Y/N):")
			if m.strip().lower() == "y":
				continue
			else:
				count = str(count)
				print("请付款" + count + "元")
				numaa = False
		else:
			print("您的输入有误！请重新输入：")
			continue
coff()
