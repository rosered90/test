import requests
import os
from bs4 import BeautifulSoup

# os.chdir(r'C:\Users\Administrator\Desktop')
# headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
url = 'https://www.baidu.com'
fp = open('host.txt','r')
ips = fp.readlines()
proxys = list()
for p in ips:
    ip =p.strip('\n').split('\t')
    proxy = 'http:\\' +  ip[0] + ':' + ip[1]
    proxies = {'proxy':proxy}
    proxys.append(proxies)
for pro in proxys:
    try :
        s = requests.get(url,proxies = pro)
        print (s)
    except Exception as e:
        print (e)