# coding:utf-8
# 解析链接，6参数

from urllib.parse import urlparse

url = 'http://www.baidu.com/index.htm;user?id=5#comment'
result = urlparse(url)
print(result)  #返回元组