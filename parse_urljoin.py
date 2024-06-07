# coding:utf-8
# 将新链接补全

from urllib.parse import urljoin

url1 = 'http://www.baidu.com'
url2 = 'index.html'

result = urljoin(url1,url2)  #用url1补全url2
print(result)