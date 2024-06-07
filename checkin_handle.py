# coding；utf-8
# 用于验证登录

from urllib.request import HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'url'

p = HTTPPasswordMgrWithDefaultRealm()  #实例化
p.add_password(None,username,password)  #添加username和password
auth_hander = HTTPBasicAuthHandler(p)  #管理认证
opener = build_opener(auth_hander)  #将认证信息打包建立opener

try:
    response = opener.open(url)  #打开网页，获取响应
    result = response.read().decode('utf-8')  #解码
    print(result)
except URLError as e:  #异常处理
    print(e.reason)
