# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:15:44 2020

@author: 陈小龙 20184035237
"""
def average(x):
    sum=0
    for num in x:
        sum=sum+num
    average=sum/len(x)
    return average

import pandas as pd
dta_smokers=pd.read_csv("/Users/35865/Desktop/经济软件应用/smokers.csv")	
dta_smokers_1 = dta_smokers['tip'].groupby(dta_smokers['time']).apply(average)
print(dta_smokers_1)

'''
Result：

time
Dinner    3.102670
Lunch     2.728088
Name: tip, dtype: float64


According to output data,taking "time" as the grouping basis, 
the average tip given by the "Dinner" group is the most.

'''

dta_smokers_2 = dta_smokers['tip'].groupby([dta_smokers['time'],dta_smokers['size']]).apply(average)
print(dta_smokers_2)
'''
Result

time    size
Dinner  1       1.000000
        2       2.661923
        3       3.490000
        4       4.122500
        5       3.785000
        6       5.000000
Lunch   1       1.875000
        2       2.423077
        3       2.754000
        4       4.218000
        5       5.000000
        6       5.300000
Name: tip, dtype: float64

According to output data, taking "time" and "size" as the grouping basis, 
the average tip given by the "Lunch" group, size 6 is the most.

'''
