# coding:utf-8
# LWP格式的本地cookies，通过load加载

from urllib import request
from http.cookiejar import LWPCookieJar as l

cookies = l()
cookies.load('lwpcookies.txt',ignore_discard=True,ignore_expires=True)
handler = request.HTTPCookieProcessor(cookies)
opener = request.build_opener(handler)

response = opener.open('http://www.baidu.com')
result = response.read().decode('utf-8')
print(result)