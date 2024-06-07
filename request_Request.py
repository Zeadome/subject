# coding:utf-8
# Request讲请求独立成一个对象

# import urllib.request

# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

from urllib import parse, request

url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
dict ={
    'name': 'Hello'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
rep = request.Request(url=url, headers=headers,data=data,method='POST')
response = request.urlopen(rep)
print(response.read().decode('utf-8'))
