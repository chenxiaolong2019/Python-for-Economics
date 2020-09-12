# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:45:42 2020

@author: ChenXiaolong
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
import string
import urllib.request
import random
import re
import pandas as pd
import scipy.stats as ss
import time

iplist = ['115.32.41.100:80','58.30.231.36:80','123.56.90.175:3128'] 
#iplist=['112.64.233.130:9991','116.231.96.146:8118','112.64.233.130:9991']
url=['https://www.05jl.com']

def start (url,iplist):
    #iplist = ['115.32.41.100:80','58.30.231.36:80','123.56.90.175:3128'] 
    #iplist = ['49.77.22.1:8118','58.134.102.3:12696','120.26.213.55:9999']
    #iplist = ['112.64.233.130:9991','116.231.96.146:8118','112.64.233.130:9991']
    proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')] 
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    return response

data=[]

bs1=start(url,iplist)

for bs in bs1.findAll("article",{"class":"excerpt"}):
       datalist_2={"影片名":bs.find("a",{'target' : '_blank'}).get("title")}
       data.append(datalist_2)

print(data)

#print(bs1.find("a",{'class':'lnk-movie'}).get("href"))#找具体的内容


