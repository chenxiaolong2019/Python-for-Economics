# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 14:26:35 2020

@author: ChenXiaolong
"""

import pandas as pd
dta_stu=pd.read_excel("/Users/35865/Desktop/经济软件应用/StudentsID.xlsx",sheet_name="StudentID2014")
#sheetname 要告诉软件是哪个具体的表单
dta_stu.head()

dta_stu["marks"]#提取一列数据的方法，字典名称要和自己取的一样

#####################################################

#构建二维数据的方法
from pandas import DataFrame
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],	
      'year':[2000,2001,2002,2001,2002],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
df4=DataFrame(data=data)
print(df4)  #index从0~4（没有进行重新命名）

from pandas import DataFrame
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],	
      'year':[2000,2001,2002,2001,2002],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
df4=DataFrame(data=data)
print(df4)  #index从0~4（没有进行重新命名）

#添加index
from pandas import DataFrame
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],	
      'year':[2000,2001,2002,2001,2002],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
index=['1','2','3','4','5']
df5=DataFrame(data=data,index=index)
df5.loc[:"3","pop":] #df5.loc[():(),():()]选取特定行与列的方法
print(df5)

from pandas import DataFrame
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],	
      'year':[2000,2001,2002,2001,2002],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
index=['1','2','3','4','5']
df5=DataFrame(data=data,index=index)
df5["pop"]#选取列的一种方法

from pandas import DataFrame
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],	
      'year':[2000,2001,2002,2001,2002],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
index=['1','2','3','4','5']
df5=DataFrame(data=data,index=index)
df5.loc["1"]#选取行的一种方法
#df5.loc["1":"1",:]

dta=DataFrame()
dta["pop"]=[1,2,3,4]
dta["state"]=["","","","",""]
dta_stu["levels"]

##########导入两个表格 合并表格
import pandas as pd
df2013=pd.read_excel("/Users/35865/Desktop/经济软件应用/StudentsID.xlsx",sheet_name="StudentID2013")
df2014=pd.read_excel("/Users/35865/Desktop/经济软件应用/StudentsID.xlsx",sheet_name="StudentID2014")

df2014["marks_2013"]=df2013["marks"]
print(df2014)

###################
#按照gender分类 把marks按从低到高排列
df2014=pd.read_excel("/Users/35865/Desktop/经济软件应用/StudentsID.xlsx",sheet_name="StudentID2014")
sortby=lambda col:col.sort_values(by="marks")
df=df2014.groupby("gender")
df=df2014.groupby("gender").apply(sortby)
print(df)

