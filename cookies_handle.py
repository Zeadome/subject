# coding:utf-8
# 处理cookies

import http.cookiejar, urllib.request

cookies = http.cookiejar.CookieJar()  #声明cookiejar对象
for item in cookies:
    print(item.name + '=' + item.value)  #cookies是一个字典

cookies_handler = urllib.request.HTTPCookieProcessor(cookies)  #将cookies打包成处理器
opener = urllib.request.bulid_opener(cookies_handler)  #打包成opener

response = opener.open('***url')  #打开网页
result = response.read().decode('utf-8')  #解码
print(result)