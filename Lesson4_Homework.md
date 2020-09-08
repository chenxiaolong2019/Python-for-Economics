#题目#

请使用已下发的“smokers.csv”文件，以就餐时间（“time”）为分组依据，求：哪一组给的小费（“tip”）的平均值最大。

具体要求：

1. 使用groupby+apply一步到位求分组结果；
2. 使用def定义一个函数来求组内平均值。
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


    dta_smokers_2 = dta_smokers['tip'].groupby([dta_smokers['time'],dta_smokers['size']]).apply(average)
    print(dta_smokers_2)

   ```
#结果

