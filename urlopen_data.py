# coding:utf-8
# data传参

import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
respose = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(respose.read())