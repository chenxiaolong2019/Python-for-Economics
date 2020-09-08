# Code

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
---
   
# Reuslt
1.
> time

> Dinner    3.102670

> Lunch     2.728088

> Name: tip, dtype: float64

> According to output data,taking "time" as the grouping basis, the average tip given by the "Dinner" group is the most than "Lunch".

2.

