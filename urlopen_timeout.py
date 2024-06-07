# coding:utf-8
# 设置超时timeout，超过则报错

#报错尝试,报错属于urllib.error模块
# import urllib.request

# response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(response.read())

# try expcet处理异常，控制响应时间，超过则不抓取
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):  #判断异常e的原因是否是socket.timeout类型
        print('TIME OUT')
