# coding:utf-8
# 反序列化，可以处理GET请求参数，生成的是元组组成的列表

from urllib.parse import parse_qsl

query = 'name=ginery&age=18'
print(parse_qsl(query))