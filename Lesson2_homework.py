# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 23:00:16 2020

@author: 20184035237 陈小龙
"""
num=[]
for x in range(2,101):
    count=0
    for y in range(2,101):
        if x%y==0:
            count+=1
    if count==1:
        num.append(x)
print(num)