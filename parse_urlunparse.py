# coding:utf-8
# 逆向解析,6参数

from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'id=6', 'comment']

print(urlunparse(data))