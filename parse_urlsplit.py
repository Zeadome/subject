# coding:utf-8
# 分割链接，5参数

from urllib.parse import urlsplit

url = 'http://www.baidu.com/index.html;user?id=5#comment'

result = urlsplit(url)
print(result)
