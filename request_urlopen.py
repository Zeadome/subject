# coding:utf-8
# request打开url

import urllib.request

response = urllib.request.urlopen('http://www.python.org')
# print(response.read().decode('utf-8'))  #先读取源代码，再以utf-8形式解码

# print(type(response))  #查看数据类型

# print(response.status)  #查看状态

# print(response.getheaders())  #获取头信息

# print(response.getheader('Server'))  #获取指定头信息
