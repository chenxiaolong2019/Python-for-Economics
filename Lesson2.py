# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 16:59:27 2020

@author: ChenXiaolong
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:32:11 2020

@author: ChenXiaolong
"""

dict1={'Name':'Zara','Age':7,'Class':'First'}#key引导value,key一定要字符型的
dict1[0]
print(dict1[0])#dic是没有顺序的，不能这样选取

#选取元素的方法
dict1['Name']#可以选取key
print(dict1['Name'])

#添加元素的方法
dict1={'Name':'Zara','Age':7,'Class':'First'}
dict1['School']="DPS School"
print(dict1)#顺序不一样

dict1={'Name':'Zara','Age':7,'Class':'First'}
del dict1['Name']
print(dict1)#dic删除元素Name

dict1={'Name':'Zara','Age':7,'Class':'First'}
dict1.setdefault('Sex',None)


####################################
#bool值
lst0=[4>2,1>2]
print(lst0)


##################################
#python的循环与控制流 PPT27
x=True
if x:
    print(1)
else:
    print(2)

#Test 条件语句
x=4
if x>3:
    print("It's over")
else:
    print("Ok")
    
#while语句 循环语句 用while必须先赋予初始值
count=1
while count<6:
    print("count is:",count)
    count+=1#count=count+1
else:
    print("Not a correct value!")

#for 语句
for count in range(7):
    print("count is:",count)
    
#TEST
lst=[0,2,4,6,8]
count=0
while count<5:
    print("count is:",lst[count])
    count+=1
else:
    print("End")
    
#countine break
lst=[0,2,4,6,8]
for count in lst:
    print("count is:",count)
    continue
else:
    print("OK")
    
#TEST
for count in range(8):
    if 3<count<6:
        print(count)
    else:
        print("Error")
    continue
else:
    print("Over")
    
####################
for i in range(8):
    if i<6 and i>3:
        continue
        print(i)
    else:
        print("wrong")
    print("It is over!")

    
for i in range(8):
    if i<6 and i>3:
        pass
        print(i)
    else:
        print("wrong")
    print("It is over!")
    
    
    
#来自https://www.runoob.com/python/python-continue-statement.html的一些例子
#continue语句#

for letter in 'Python':     # 第一个实例
   if letter == 'h':  
      continue
   print ('当前字母 :', letter)
#continue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分,比如‘h’  

var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('当前变量值 :', var)
print ("Good bye!")

#break#强制终止
 
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      break
   print ('当前字母 :', letter)


var = 10                    # 第二个实例
while var > 0:              
   print ('当前变量值 :', var)
   var = var -1
   if var == 5:   # 当变量 var 等于 5 时退出循环
      break
print ("Good bye!")

# 输出 Python 的每个字母
for letter in 'Python':
   if letter == 'h':
      pass
      print ('这是 pass 块')
   print ('当前字母 :', letter)
print ("Good bye!")
    
######################################
#        >=大于等于
#         !=不等于
######################################

"""
练习：请找出1~100之间的质数，并写成一个列表。
       a%b==0，b能被整除
"""
num=[]
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
         num.append(i)
print(num) 
#############

num=[]
for x in range(2,101):
    count=0
    for y in range(2,101):
        if x%y==0:
            count+=1
    if count==1:
        num.append(x)
print(num)
     
#######################################

#定义函数
def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dsquared=dx**2+dy**2
    result=dsquared**0.5
    return result
print(distance(0,0,3,4))

def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    result=(dx**2+dy**2)**0.5
    return result
print(distance(1,2,3,4))

def circlearea(r):#计算圆的面积
    area=3.14159265*r**2
    return area
print(circlearea(2))


#函数的调用
def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dsquared=dx**2+dy**2
    result=dsquared**0.5
    return result
    
def circlearea(r):
    area=3.14159265*r**2
    return area
    
