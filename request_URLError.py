# coding:utf-8
#该异常属于urllib内的error模块，继承OSError，是error的基类

from urllib.error import URLError
from urllib.request import urlopen

try:
    response = urlopen('http://sjankakiiqo.com/index.htm')
except URLError as e:
    print(e.reason)
    