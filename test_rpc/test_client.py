from xmlrpc import client
server = client.ServerProxy("http://192.168.0.46:8000/RPC")
# 访问对应server上的RPC方法  
# add()方法是服务端定义好的程序  
rst = server.mynamespace.rpc_add(str(1), 'aini')
print(rst)




