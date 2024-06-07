# coding:utf-8
# 组合链接，5参数

from urllib.parse import urlunsplit

data = ['http', 'www.baidu.com', 'index.html;user', 'id=5', 'comment']

result = urlunsplit(data)
print(result)
