# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 14:47:58 2020

@author: ChenXiaolong
"""


"""
PPT 44

x<=16/4
y<12/4
x+2*y <= 8
x=[0,1,2,3,4]
y=[0.1.2.3]
"""

plan=[]
for x in range(5):
    for y in range(4):
        if x+2*y <= 8:
            product=(x,y)
            plan.append(product)
print(plan)
            
#function
#x为用于生产甲商品的A配件的库存数量，x1为生产一个甲产品所需要的配件数量
#y为用于生产乙商品的B配件的库存数量，y1为生产一个乙产品所需要的配件数量
#h为生产一件甲产品的耗时，h1为生产一件乙产品的耗时
#time为一天工作的时常
def production_plan(x,x1,y,y1,h,h1,time):
    plan=[]
    for i in range(int(x/x1)):
        for j in range(int(y/y1)):
            if h*i+2*j<=time:
                product=(i,j)
                plan.append(product)
    return plan

production_plan(16,4,12,4,1,2,8)
print(plan)


