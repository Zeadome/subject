# coding:utf-8
# 将cookies以文件形式保存

from http.cookiejar import LWPCookieJar as l
from urllib import request, error

filename = 'lwpcookies.txt'
cookies = l(filename)
cookies_handler = request.HTTPCookieProcessor(cookies)
opener = request.build_opener(cookies_handler)

try:
    response = opener.open('http://www.baidu.com')
    cookies.save(ignore_discard=True,ignore_expires=True)
except error.URLError as e:
    print(e.reason)