import uiautomator2 as u2

d = u2.connect('192.168.0.163')  # alias for u2.connect_wifi('192.168.5.4')
print(d.info)
