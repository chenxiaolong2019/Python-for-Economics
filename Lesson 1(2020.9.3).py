# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:36:19 2020

@author: ChenXiaolong
"""
######################################
a=1
b="1"

c=True
type(a) #帮助我们识别括号里的元素是什么属性的函数

e=1.0
type(e)

type(c)#bool值

print("abc")#输出字符


h="r"
print(b+h)

f=2
print(a+f)

###########################################
lst1=[1,2,3,4,5]#列表
len(lst1)#计算列表元素长度（有多少元素）经常用来检验两个列表是不是一样长
type(lst1)#列表（最有用）

tup1=(1,2,3,4,5,6,7)
type(tup1)#元组

dict1={'Name':'Zara'}
type(dict1)#字典

#这里出现三种python的数据结构分别是list、tuple和dictionary
#list用[]  tuple用()  dictionary用{}
#list的元素可以是数字、字符、字符串、布尔值
#tuple的元素可以是字符串、数字
#dictionary的元素可以为字符串、数字

#type len print是识别型命令

############################################

lst1=[1,2,3,4,5]
lst2=lst1.copy()
print(lst2)#copy函数的应用 PPT10

lst1=[1,2,3,4,5]
lst4=lst1
print(lst4)
#lst4=lst1也具有复制的功能

tup1=(1,2,3)
tup2=tup1.copy()
print(tup2) #元组不能被复制

lst1=[1,2,3,4,5]
del lst1[0]#删除函数
print(lst1)

lst2=lst1.copy()
del lst2[2]
print(lst2)

lst6=[1,2,3,4,5]
lst6[0:3]#选的元素是第0个元素到第2个元素，3代表终点，不包括终点，左闭右开
print(lst6[0:3])

lst7=[1,2,3,4,5]
lst7[0:4:2]#最后一个参数n代表：隔(n-1)个元素选一个元素
print(lst7[0:4:2])

lst8=[0,1,2,3,4,5,6,7,8,9]
print(lst8[0:10:3])#课堂练习 早期IDE可能会报错,要进行如下操作
lst9=[0,1,2,3,4,5,6,7,8,9]
lst9[0:3]
print(lst9[0:10:3])

#定义元组（1，2，3，4，5，6，8，9）删除数字5
tup2=(0,1,2,3,4,5,6,7,8,9)
tup3=(0,1,2,3,4)
tup4=(6,7,8,9)
print(tup3+tup4)#元组不能del,可以考虑相加

tup2=(0,1,2,3,4,5,6,7,8,9)
print(tup2[0:5]+tup2[6:10])

###############################################
#    作业：弄明白列表和元组什么样，怎么筛选元素   #
###############################################
