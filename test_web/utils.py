def dict2obj(args):
	"""
    将字典转成对象，这样可以字典可以在页面中直接当成对象使用
    :param args:
    :return:
    """


	class Obj(object):
		def __init__(self, d):
			for a, b in d.items():
				if isinstance(b, (list, tuple)):
					setattr(self, a, [Obj(x) if isinstance(x, dict) else x for x in b])
				else:
					setattr(self, a, Obj(b) if isinstance(b, dict) else b)


	return Obj(args)