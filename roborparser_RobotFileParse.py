# coding:utf-8
# Robots协议是一个robots.txt文件，RobotFileParse用于判断一个函数是否可以爬取

from urllib.robotparser import RobotFileParser

response = RobotFileParser()    #实例化
response.set_url('http://www.jianshu.com/roboys.txt')   #设置协议网址
response.read() #读取
print(response.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d')) #判断能否爬取