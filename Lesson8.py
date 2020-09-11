# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:02:53 2020

@author: ChenXiaolong
"""
import urllib.request
import random

url0 = "https://book.douban.com/tag/"
iplist = ['115.32.41.100:80','58.30.231.36:80','123.56.90.175:3128'] 
#iplist=['49.77.22.1:8118','58.134.102.3:12696','120.26.213.55:9999']
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

#准备代理IP或者请求头
opener = urllib.request.build_opener(proxy_support)

#利用lurllib.request.build_opener()封装代理IP或请求头
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')] 
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
urllib.request.install_opener(opener)

#利用lurllib.request.instanll_opener()安装成urlopen()使用的全局opener。
response = urllib.request.urlopen(url0)

#筛选图片或者文字
from bs4 import BeautifulSoup
from urllib.request import urlopen
url1 = "https://www.baidu.com/"
html1 = urlopen(url1)
bs1 = BeautifulSoup(html1,"lxml") #lxml是设置默认的解析器
print(bs1.head)#.head找关键词

from bs4 import BeautifulSoup
from urllib.request import urlopen
url1 = "https://www.cnblogs.com/liushengchieh/p/6056900.html"
html1 = urlopen(url1)
bs1 = BeautifulSoup(html1,"lxml") #lxml是设置默认的解析器
print(bs1.findAll("img"))#可以用正则表达式

from bs4 import BeautifulSoup
from urllib.request import urlopen
url1 = "https://www.douban.com"
html1 = urlopen(url1)
bs1 = BeautifulSoup(html1,"lxml") #lxml是设置默认的解析器
print(bs1.findAll("class")) #可以用正则表达式

from bs4 import BeautifulSoup
from urllib.request import urlopen
url1 = "https://www.douban.com"
html1 = urlopen(url1)
bs1 = BeautifulSoup(html1,"lxml") #lxml是设置默认的解析器
print(bs1.div.div.ul) #先找到div ul 再找。。。

from bs4 import BeautifulSoup
from urllib.request import urlopen
url1 = "https://www.douban.com"
html1 = urlopen(url1)
bs1 = BeautifulSoup(html1,"lxml") #lxml是设置默认的解析器
print(bs1.find("div",{'class':'anony-nav-links'}))

'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
url1 = "https://www.douban.com"
html1 = urlopen(url1)
bs1 = BeautifulSoup(html1,"lxml") #lxml是设置默认的解析器
print(bs1.findAll("div",{'li':'a'}))
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
url1 = "https://www.douban.com"
html1 = urlopen(url1)
bs1 = BeautifulSoup(html1,"lxml") #lxml是设置默认的解析器
print(bs1.find("a",{'class':'lnk-movie'}))  #标签逻辑层次
#<a target="_blank" class="lnk-book" href="https://book.douban.com">豆瓣读书</a>

from bs4 import BeautifulSoup
from urllib.request import urlopen
url1 = "https://www.douban.com"
html1 = urlopen(url1)
bs1 = BeautifulSoup(html1,"lxml") #lxml是设置默认的解析器
bs1
print(bs1.find("a",{'class':'lnk-movie'}).get("href"))#找具体的内容

from bs4 import BeautifulSoup
from urllib.request import urlopen
url1 = "https://www.douban.com"
html1 = urlopen(url1)
bs1 = BeautifulSoup(html1,"lxml") #lxml是设置默认的解析器
bs1
print(bs1.find("a",{'class':'lnk-movie'}).get_text())#找具体的文字内容

##########################################################################



