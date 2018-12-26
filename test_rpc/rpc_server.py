#  testapp/__init__.py  
from rpc4django import rpcmethod  

@rpcmethod(name='mynamespace.rpc_add',signature = ['int', 'int', 'int'])

def rpc_add(a,b):
    '''''Adds two numbers together 
    add(1, 2)
    3
    '''
    return a + b
