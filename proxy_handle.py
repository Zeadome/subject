# coding:utf-8
# 添加代理

from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError

url = 'url'

proxy_handler = ProxyHandler({
    'http':'***',
    'https':'***'
})   #参数是字典，键名是协议类型，键值是地址

opener = build_opener(proxy_handler)  #将代理打包称opener

try:
    response = opener.open(url)  #打开网址
    result = response.read().decode('utf-8')  #解码
    print(result)
except URLError as e:  #异常处理
    print(e.reason)