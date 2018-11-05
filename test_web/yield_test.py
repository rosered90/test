# _*_ coding:utf-8 _*_
def h():
	a = 'rewtete'
	print a,
	m = yield 5 + 1  # Fighting!
	print m  # 相当于在迭代器末尾加值
	# print m
	# print m
	# d = yield 12
	print 'We are together!'
	d = yield 12
	print 'We are together!'

c =h()
m = c.next()
# print m
# m = 1
# c.send(m)
# c.next()

# c.next()

# print type(h)
# print type(c.next())