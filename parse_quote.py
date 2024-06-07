# coding：utf-8
# 将中文转化为url编码的格式

from urllib.parse import quote

keyword = '哈萨克'
url = 'https://www.baidu.com/s?kw='

print(url+quote(keyword))   #https://www.baidu.com/s?kw=%E5%93%88%E8%90%A8%E5%85%8B