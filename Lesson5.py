# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:04:10 2020

@author: ChenXiaolong
"""
import pandas as pd

df11=pd.DataFrame([1.5,4.2,1.1,0.6],		
		index=['Shanxi','Henan','Beijing','Chongqing'],columns=["GDP"])
print(df11)

################################################################
#添加行 添加列
df10=pd.DataFrame([35000,71000,16000,5000],
                  index=['Shanxi','Henan','Beijing','Chongqing'],
                  columns=["Population"])

df10["year"]=["2000","2001","2002","2003"]#添加列
df10.loc["Dalian"]=[1000,"2004"]#添加行
print(df10)


df10=pd.DataFrame([[35000,71000,16000,5000,1000],[2000,2001,2002,2003,2004]],
                  index=['Shanxi','Henan','Beijing','Chongqing','Dalian'],
                  columns=[['Population','years']])
print(df10)

##################################################################

#merge横向合并（越来越宽）
df10=pd.DataFrame([35000,71000,16000,5000],
                  index=['Shanxi','Henan','Beijing','Chongqing'],
                  columns=["Population"])

df10["year"]=["2000","2001","2002","2003"]#添加列
df10.loc["Dalian"]=[1000,"2004"]#添加行
#     df1011=pd.merge(df10,df11,left_index=True,right_index=True)
df1011=pd.merge(df10,df11,left_index=True,right_index=True,how="outer")#填充缺省值
print(df1011)

######################################################################
#纵向合并（越来越长）
df10=pd.DataFrame([35000,71000,16000,5000],
                  index=['Shanxi','Henan','Beijing','Chongqing'],
                  columns=["Population"])

df10["year"]=["2000","2001","2002","2003"]#添加列
df10.loc["Dalian"]=[1000,"2004"]#添加行

df12=pd.DataFrame([15000,71000,11000,6000],		
	              index=['Shenzhen','Henan','Tianjin','Chengdu'],		
                  columns=["Population"])	
df12["year"]=["2000","2001","2002","2003"]

df1012=pd.concat([df10,df12]).drop_duplicates()
print(df1012)

########################################################################
#处理缺失值
df10=pd.DataFrame([35000,71000,16000,5000],
                  index=['Shanxi','Henan','Beijing','Chongqing'],
                  columns=["Population"])

df10["year"]=["2000","2001","2002","2003"]
df10.loc["Dalian"]=[1000,"2004"]
df1011=pd.merge(df10,df11,left_index=True,right_index=True,how="outer")

print(df1011[df1011["GDP"]>1.0])  #输出GDP大于1的行元素

###########
df10=pd.DataFrame([35000,71000,16000,5000],
                  index=['Shanxi','Henan','Beijing','Chongqing'],
                  columns=["Population"])

df10["year"]=["2000","2001","2002","2003"]
df10.loc["Dalian"]=[1000,"2004"]
df1011=pd.merge(df10,df11,left_index=True,right_index=True,how="outer")

print(df1011[['Population','GDP']])  #输出两列

###########################################################################
#python统计量的计算
import pandas as pd
dta_cars=pd.read_csv("/Users/35865/Desktop/经济软件应用/mtcars.csv")	
dta_cars_3=dta_cars[['mpg','disp','hp']]
dta_cars_3.head(6)#显示头部信息 默认显示5行

dta_cars_3.describe()#第一列是描述性统计量
#mean平均数 std标准差 min最小值 25% 50% 75%四分位数 max是最大值
dta_cars_3.mode

#求相关系数    PPT 111
dta_cars_3.corr(method='pearson',min_periods=1)
dta_cars_3.corr()

#agg命令的用法：一次输出多个函数运行的结果
dta_cars=pd.read_csv("/Users/35865/Desktop/经济软件应用/mtcars.csv")
dta_cars_4 = dta_cars.groupby(dta_cars["cyl"]).agg(["mean","median","std"])
print(dta_cars_4)
#cyl气缸
#groupby可以接apply、函数、agg

#数据的规约
#单位不一样的变量，把变量的波动限制在一定的范围里面















