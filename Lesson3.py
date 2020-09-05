# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:54:04 2020

@author: ChenXiaolong
"""

import numpy as np 

import pandas as pd
dta_iris1=pd.read_csv("/Users/35865/Desktop/经济软件应用/iris.csv")	
dta_iris1.head(6)#显示头部信息 默认显示5行
dta_iris1.head(10)#显示头部信息 显示10行

import pandas as pd
dta_iris1=pd.read_csv("/Users/35865/Desktop/经济软件应用/mtcars.csv")	
dta_iris1.head()#显示头部信息 默认显示5行

dta_cap=pd.read_csv("/Users/35865/Desktop/经济软件应用/cap_dict.txt",header=None,sep=" ")	
#既能读.csv又能读txt
#head=None说明这个文件没有表头
#sep=说明 列与列之间是用什么区分的
dta_cap.head()

dta_stu=pd.read_excel("/Users/35865/Desktop/经济软件应用/StudentsID.xlsx",sheet_name="StudentID2014")
#sheetname 要告诉软件是哪个具体的表单
dta_stu.head()