# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:59:35 2020

@author: ChenXiaolong
"""
###########################################################
#正态性检验
from scipy import stats

X=[34,35,43,46,16,26,68,38,61,52,68,13,69,18,53,18,
 41,25,17,26,44,30,19,48,29,24,51,40,26,20,19,42]

#偏度
stats.skew(X)
#0.5054153948547095  往左偏是负数 往右偏是正数

#峰度
stats.kurtosis(X,fisher=True)#费希尔检验
#-0.7608318153873941 (normal ==> 0.0)  0.0是基准值
stats.kurtosis(X,fisher=False)
#2.239168184612606 (normal ==> 3.0)


#Shapiro-Wilk Test（3≤n≤50） 样本数3到50
stats.shapiro(X)  
#(0.9335119724273682, 0.049101389944553375)
#前面这个值是T值 后面这个值的P值 拒绝原假设
#p值小于0.05拒绝原假设
#原假设是这组数据服从正态分布
#所以这组数据不服从正态分布

#############################################################
#T检验两个样本之间有没有差别，T检验只能衡量正态分布的数据，评价"几星"属于定序数据
#考察两个样本总体的均值间的差值

#两总体对比推断 独立样本T检验 PPT 126
import scipy.stats as ss
ss.ttest_ind(x,y,equal_var=True, nan_policy='propagate') 

#
import pandas as pd
import scipy.stats as ss
df=pd.read_csv("/Users/35865/Desktop/经济软件应用/Petrol Price 1.csv")
a1=df["Sydney"]
b1=df["Local"]
ss.ttest_ind(a1,b1,equal_var=True)

'''
Ttest_indResult(statistic=-2.1726379317183482, pvalue=0.043407004570150828)
'''
import scipy.stats as ss
df=pd.read_csv("/Users/35865/Desktop/经济软件应用/Petrol Price 1.csv")
a1=df["Sydney"]
b1=df["Local"]
ss.ttest_ind(a1,b1,equal_var=False)
'''
Ttest_indResult(statistic=-2.1726379317183482, pvalue=0.046296043109082335)
'''
#配对样本T检验 PPT130


########################################################################
#P133练习
#独立样本T检验
import scipy.stats as ss
import pandas as pd
df=pd.read_csv("/Users/35865/Desktop/经济软件应用/MBA.csv")

Finance=df["Finance"]
Marketing=df["Marketing"]

ss.levene(df["Finance"],df["Marketing"])
#pvalue=0.8104845346436915 接受原假设 方差是齐的
ss.ttest_ind(Finance,Marketing,equal_var=True, nan_policy='propagate') 
#Ttest_indResult(statistic=0.8374031365017772, pvalue=0.4065162453297182)
#接受原假设 没有显著差异

#配对样本T检验 
ss.ttest_rel(Finance,Marketing,nan_policy='propagate') 
# Ttest_relResult(statistic=3.80968841351656, pvalue=0.0008510859875589974)
#拒绝原假设 有显著差异

#来自同一样本就是配对样本T检验 来自两个样本就是独立样本T检验
#########################################################################
#方差分析
#单因素方差分析
import scipy.stats as ss
x=[0.84,1.05,1.20,1.20,1.39,1.53,1.67,1.80,1.87,2.07,2.11,1.87]
y=[0.54,0.64,0.64,0.75,0.76,0.81,1.16,1.20,1.34,1.35,1.48,1.56 ]
ss.f_oneway(x,y) 

#
import scipy.stats as ss
data='/Users/35865/Desktop/经济软件应用/multi-temp.csv'
df=pd.read_csv(data,header=None,names=['period','tem','hum'])
df=df.dropna()#去掉整个数据框中的缺失值
x1=df[df['tem']==25]["period"]#为什么不能先写“period”? 不能先写列
x2=df[df['tem']==27]["period"]
x3=df[df['tem']==29]["period"]
x4=df[df['tem']==31]["period"]
ss.f_oneway(x1,x2,x3,x4) 
#F_onewayResult(statistic=49.98079729759776, pvalue=3.198808827457241e-14)

'''
不能先写列
x8=df[df["period"]]["hum"]==100
x9=df[df["period"]]['hum']==80
x10=df[df["period"]]['hum']==40
ss.f_oneway(x8,x9,x10)
'''

x5=df[df['hum']==100]["period"]
x6=df[df['hum']==80]["period"]
x7=df[df['hum']==40]["period"]
ss.f_oneway(x5,x6,x7)
#F_onewayResult(statistic=2.64937674435188, pvalue=0.0817041385002687)

##########
#另外办法
#单因素方差分析
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
data='/Users/35865/Desktop/经济软件应用/multi-temp.csv'
df=pd.read_csv(data,header=None,names=['period','tem','hum'])#header=None没表头
df=df.dropna()#去掉缺失值 删除一整行
formula='period ~ C(tem)' #右边自变量 左边因变量
anova_results=anova_lm(ols(formula,df).fit())#
anova_results
'''
            df       sum_sq      mean_sq          F        PR(>F)
C(tem)     3.0  4726.300625  1575.433542  49.980797  3.198809e-14
Residual  44.0  1386.914167    31.520777        NaN           NaN
'''
#双因素方差分析
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
data='/Users/35865/Desktop/经济软件应用/multi-temp.csv'
df=pd.read_csv(data,header=None,names=['period','tem','hum'])#header=None没表头
df=df.dropna()#去掉缺失值 删除一整行
formula='period ~ C(tem)+C(hum)' #右边自变量 左边因变量
anova_results=anova_lm(ols(formula,df).fit())#
anova_results
'''
            df       sum_sq      mean_sq          F        PR(>F)
C(tem)     3.0  4726.300625  1575.433542  89.065802  3.050164e-18
C(hum)     2.0   644.000417   322.000208  18.204009  2.026119e-06
Residual  42.0   742.913750    17.688423        NaN           NaN
'''
############
#加交互项（tem和hun交叉产生的结果，既不是hum单独作用的结果，也不是tem单独作用的结果）
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
data='/Users/35865/Desktop/经济软件应用/multi-temp.csv'
df=pd.read_csv(data,header=None,names=['period','tem','hum'])#header=None没表头
df=df.dropna()#去掉缺失值 删除一整行
formula='period ~ C(tem)+C(hum)+C(tem):C(hum)' #右边自变量 左边因变量
anova_results=anova_lm(ols(formula,df).fit(),typ=3)
#typ=3即能用平衡的数据又能用于长度不相等的数据
#typ=2只能用于平衡数据
anova_results
'''
                     sum_sq    df            F        PR(>F)
Intercept      41127.840000   1.0  2372.541376  1.843916e-34
C(tem)          1762.296875   3.0    33.887202  1.386612e-10
C(hum)           176.585000   2.0     5.093329  1.127580e-02
C(tem):C(hum)    118.856250   6.0     1.142743  3.580588e-01
Residual         624.057500  36.0          NaN           NaN

Intercept 截距项
tem有影响
hum有影响
交互项没有影响
把交互项删掉再跑一次
'''
#Turkey检验
from statsmodels.stats.multicomp import pairwise_tukeyhsd
hsd1=pairwise_tukeyhsd(df['period'],df['tem'])
hsd2=pairwise_tukeyhsd(df['period'],df['hum'])
print (hsd1.summary())
print (hsd2.summary())

##################################################################


###################################################################
#非参数统计分析
#威尔科克森秩和检验
import scipy.stats as ss
X=[3,5,4,3,2,5,1,4,5,3,3,5,5,5,4]
y=[4,1,3,2,4,1,3,4,2,2,2,4,3,4,5]
statistic,p_value=ss.ranksums(X, y)
statistic, 0.5*p_value
#半面的P vaule
#(1.8250349827255485, 0.03399787521753456)


#威尔科克森符号秩检验
import scipy.stats as ss
X=[34,35,43,46,16,26,68,38,61,52,68,13,69,18,53,18, 41,25,17,26,44,30,19,48,29,24,51,40,26,20,19,42]
y=[31,31,44,44,15,28,63,39,63,54,65,12,71,13,55,19, 38,23,14,21,40,33,18,51,33,21,50,38,22,19,21,38]
statistic,p_value=ss.wilcoxon(x=X, y=y,zero_method="wilcox",correction=False)
statistic,p_value
# (160.5, 0.05147906613896756)


