#题目#
请使用已下发的“smokers.csv”文件，以就餐时间（“time”）为分组依据，
求：哪一组给的小费（“tip”）的平均值最大。
具体要求：
（1）使用groupby+apply一步到位求分组结果；
（2）使用def定义一个函数来求组内平均值。
（加分项：同时以就餐时间“time”和就餐人数“size”为分组依据，分别考察不同人数和不同就餐时间里，哪一组给的小费“tip”的平均值最大）

---

#代码#
    ```
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
Result

time
Dinner    3.102670
Lunch     2.728088
Name: tip, dtype: float64


According to output data,taking "time" as the grouping basis, 
the average tip given by the "Dinner" group is the most than "Lunch".

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
the average tip given by the "Lunch" group, size 1 is the most.

'''

    ```
