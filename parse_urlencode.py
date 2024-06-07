# coding:utf-8
# urlencode构造GET请求

from urllib.parse import urlencode

params = {
    'name':'xiaoming',
    'age':18
}
url = 'http://www.baidu.com'

result = url + urlencode(params)  #将params序列化，拼接
print(result)