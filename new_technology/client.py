from xmlrpc.client import ServerProxy
s = ServerProxy('http://localhost:15000', allow_none=True)
s.set('foo', 'bar')
s.set('spam', [1, 2, 3])
a = s.keys()
print (a)