# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:14:17 2020

@author: ChenXiaolong
"""
# PPT 168

import pandas as pd
import scipy.stats as ss	
dta_friedman=pd.read_csv("/Users/35865/Desktop/经济软件应用/friedman.csv")

x1=dta_friedman["Manager 1"]
x2=dta_friedman["Manager 2"]
x3=dta_friedman["Manager 3"]
x4=dta_friedman["Manager 4"]
#args = list(map(np.asarray,(x1,x2,x3,x4)))
chisq,p_value=ss.friedmanchisquare(x1,x2,x3,x4)
print (chisq,p_value)
#12.863636363636344 0.0049409744275277

#############################################################################

#python爬虫
#第一步：获取网页的两种方法
import requests
url1 = "http://www.pythonscraping.com/pages/page1.html"
proxy='0.0.0.0'#请求头构造的方法见124 125行
headers='User'
response1 = requests.get(url1, proxies = proxy, headers=headers)
#proxy为IP地址，headers为头部信息

#################
import requests
from urllib.request import urlopen
url1 = "http://www.pythonscraping.com/pages/page1.html"
html1=urlopen(url1)

##################
#含有中文的路径的读取方式

url2 = "https://baike.baidu.com/item/支付宝/496859"
from urllib.request import urlopen
from urllib.parse import quote
import string
stg = quote(url2,safe=string.printable)
#https://baike.baidu.com/item/%E6%94%AF%E4%BB%98%E5%AE%9D/496859
html2=urlopen(stg)#**********

#第二步：分析网址获取内容
from urllib.request import urlopen
url1 = "http://www.pythonscraping.com/pages/page1.html"
html1=urlopen(url1)
html1.read() #开头有个‘b’，说明是二进制的

import requests
url1 = "http://www.pythonscraping.com/pages/page1.html"
response1 = requests.get(url1)
response1.text  #开头没有‘b’，说明不是二进制的

import requests
url1 = "http://www.pythonscraping.com/pages/page1.html"
response1 = requests.get(url1)
response1.content 

#text返回的是Unicode型的数据 
#content返回的是二进制的数据

import requests
url3 = "http://www.baidu.com"
response2 = requests.get(url3)
response2.content.decode('utf-8')#输出中文
############################################################
#P214 Test
url1 = "https://baike.baidu.com/item/牡丹"
url2 = "https://baike.baidu.com/item/芍药"
url3 = "https://baike.baidu.com/item/蔷薇"
url4 = "https://baike.baidu.com/item/玫瑰"

from urllib.request import urlopen
from urllib.parse import quote #解析中文的模块
import string

stg1 = quote(url1,safe=string.printable)
stg2 = quote(url2,safe=string.printable)
stg3 = quote(url3,safe=string.printable)
stg4 = quote(url4,safe=string.printable)

html_mudan = urlopen(stg1)
html_shaoyao = urlopen(stg2)
html_qiangwei = urlopen(stg3)
html_meigui = urlopen(stg4)

html_mudan.read().decode('utf-8')
html_shaoyao.read().decode('utf-8')
html_qiangwei.read().decode('utf-8')
html_meigui.read().decode('utf-8')

########

from urllib.request import urlopen
from urllib.parse import quote #解析中文的模块
import string
list=["牡丹","玫瑰","芍药","牡丹"]
for i in list:
    url="https://baike.baidu.com/item/" +i
    stg = quote(url,safe=string.printable)
    html = urlopen(stg)
    html.read().decode('utf-8')
    print("Succed in ",i)

##########################################
#保存数据
from urllib.request import urlopen
url1 = "http://www.pythonscraping.com/pages/page1.html"
html1 = urlopen(url1)
html1 = html1.read()
html1 = html1.decode('utf-8')
fileOb = open('/Users/35865/Desktop/LOC_DATA/req.txt','w',encoding='utf-8')
fileOb.write(html1)
fileOb.close()
print("OK")

#################################################
#突破反爬虫
#构造请求头
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}   
proxy = { "http": "http://119.28.152.208:80" }

#Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
#AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36









