# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 10:13:14 2020

@author: ChenXiaolong
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import random
import pandas as pd
import scipy.stats as ss

iplist = ['115.32.41.100:80','58.30.231.36:80','123.56.90.175:3128'] 
#iplist=['49.77.22.1:8118','58.134.102.3:12696','120.26.213.55:9999']
#iplist=['112.64.233.130:9991','116.231.96.146:8118','112.64.233.130:9991']
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')] 
urllib.request.install_opener(opener)

#《坏小孩》书评爬取
data_badkid=[]

for i in range(4):
    x=i*10
    url="https://book.douban.com/subject/25955474/reviews?start="+ str(x)
    #stg = quote(url,safe=string.printable)

    html = urlopen(url)
    bs1 = BeautifulSoup(html,"lxml")
    print("网址读取成功:",url)
    for bs in bs1.findAll('div',class_='main review-item'):
        datalist={'用户名':bs.find("a",class_ ='name').get_text(),
                  '评分':str(bs.span.get("class")).replace("allstar","").replace("main-title-rating",'').replace(",",'').replace("[",'').replace("]",'').replace("\'","").replace(" ",""),
                  '内容':bs.find("div",class_ ='short-content').get_text().replace("\n","").replace('\xa0(展开)','') }
        data_badkid.append(datalist)

data_badkid_new=pd.DataFrame(data_badkid, columns=['用户名','评分','内容'])
data_datakid_clean=data_badkid_new[ ~ data_badkid_new['评分'].str.contains('main-meta')]
data_datakid_clean.to_csv('/Users/35865/Desktop/LOC_DATA/badkid.csv', index=False,encoding='utf_8_sig')

#《无证之罪》书评爬取
data_The_Untourched_Crime=[]

for count in range(4):
    url_1="https://book.douban.com/subject/25799686/comments/?start="+str(count*10)+"&limit=20&status=P&sort=new_score"
    #stg = quote(url,safe=string.printable)

    html_1 = urlopen(url_1)
    bs1 = BeautifulSoup(html_1,"lxml")
    print("网址读取成功:",url_1)
    for bs in bs1.findAll('li',class_='comment-item'):
        datalist_1={'用户名':bs.find('span',class_='comment-info').get_text().strip()[:-12],
                  '评分':str(bs.find('span',class_='comment-info').span.get("class")).replace("user-stars","").replace("allstar",'').replace(",",'').replace("[",'').replace("]",'').replace("\'","").replace(" ","").replace("rating",""),
                  '内容':bs.find('span', class_="short").get_text().replace("\n","")}
        data_The_Untourched_Crime.append(datalist_1)        

data_The_Untourched_Crime_new=pd.DataFrame(data_The_Untourched_Crime, columns=['用户名','评分','内容'])
data_The_Untourched_Crime_clean=data_The_Untourched_Crime_new[ ~ data_The_Untourched_Crime_new['评分'].str.contains('comment-time')]
pd.DataFrame(data_The_Untourched_Crime_clean, columns=['用户名','评分','内容']).to_csv('/Users/35865/Desktop/LOC_DATA/The_Untourched_Crime.csv', index=False,encoding='utf_8_sig')

##################################
#合并评分 形成新csv
df_badkid=pd.read_csv("/Users/35865/Desktop/LOC_DATA/badkid.csv")
df_The_Untourched_Crime=pd.read_csv('/Users/35865/Desktop/LOC_DATA/The_Untourched_Crime.csv')

df1=pd.DataFrame()
df1["badkid"]=df_badkid["评分"]
df1["Crime"]=df_The_Untourched_Crime["评分"]
df3=pd.merge(df1["badkid"],df1["Crime"],left_index=True,right_index=True,how="outer")
df3.to_csv('/Users/35865/Desktop/LOC_DATA/Fix.csv', index=False,encoding='utf_8_sig')

####################################
#非参数检验 
#W-M-W检验
df4=pd.read_csv("/Users/35865/Desktop/LOC_DATA/Fix.csv")

X=df4["badkid"]
y=df4["Crime"]
statistic,p_value=ss.wilcoxon(x=X, y=y,zero_method="wilcox",correction=False)
statistic,p_value

#(753.0, 0.708107313326723)
#p=0.71>0.05,有显著差异
