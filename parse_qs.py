# coding:utf-8
# 反序列化，可以处理GET请求参数,生成的是字典

from urllib.parse import parse_qs

query = 'name=ginery&age=18'
print(parse_qs(query))