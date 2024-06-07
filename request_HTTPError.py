# coding:utf-8
# HTTPError属于URLError的子类

from urllib.error import HTTPError, URLError
from urllib import request

try:
    response = request.urlopen('http://www.python.org',timeout=0.1)
except HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except URLError as e:
    print(e.reason)
else:
    print('Request successfully')
    