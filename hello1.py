# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:29:16 2019

@author: teng
"""
import this
import random  
import math  


print('hello, world!')

print('你好', '世界')

print('hello', 'world', sep=',', end='!')

print('goodbye, world', end='!\n')


#判断闰年
year=int(input('请输入年份： '))
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)

#函数
x= float(input('请输入x: '))
if x > 1:
    print('y=%0.2f'%(3*x-5))


#随机游戏
from random import randint

face = randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲冷笑话'
print(result)

#分数评级
score=float(input('输入分数： '))
if score<60:
    print('不及格')
elif score<70:
    print('d')
elif score<80:
    print('c')
elif score<90:
    print('b')
elif score<=100:
    print('a')
    
    
#求和
sum=0
for i in range(2,101,2):
    sum+=i
print('sum=',sum)


#猜数字
x=random.randint(1,100)
y=int(input('请输入: '))
count=0
while y!=x:
    count+=1
    if y>x:
        print('大了，继续：')
    elif y<x:
        print('小了，继续。')
    y=int(input('请输入: '))
 
print('恭喜！正确答案是%d,次数是%d'%(x,count))  


#九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print('%d*%d=%d'%(i,j,i*j),end='\t')
    print()


#判断质数
x=int(input('num= '))
while x<=1:
    print('again')
    x=int(input('num= '))
    
for i in range(2,int(math.sqrt(x))):
    if x%i==0:
        print('no')
print('yes')



#更相减损法
def max1():
    x=int(input('x= '))
    y=int(input('y= '))
    count=0
    while(not(x%2) and not(y%2)):
        x=int(x/2)
        y=int(y/2)
        count+=2
    if x<y:x,y=y,x
    while x-y!=y:
        x,y=(x-y),y
        if x<y:
           x,y=y,x
    return y

a=max1()
print(a)
               


#打印三角形
row=int(input('shuruhangshu: '))
for i in range(1,row+1):print('*'*i)
for i in range(1,row+1):
    print(' '*(row-i),end='')
    print('*'*i)
for i in range(1,row+1):
    print(' '*(row-i),end='')
    print('*'*(2*i-1))      

#寻找水仙花数
for n in range(100,1000):
    a=n//100
    b=n%100//10
    c=n%10
    if(n==a**3+b**3+c**3):
        print('%i is Narcissistic'%n)


#完全数（Perfect number）
for n in range(1,1000):
    sum=0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            sum+=i
    if sum==n:
        print(n)

#百鸡百钱
for cock in range(0,100):
    for hen in range(1,100):
        if cock*5+3*hen+(100-cock-hen)/3==100:
            print(cock,hen,100-cock-hen)

    
#斐波那契数列（Fibonacci sequence）
n=1
m=1
while n<1000:
    print(n,end='->')
    n,m=m,n+m

    
#craps赌博游戏
money=int(input('你带来了多少钱: '))
while money>0:
    while True:
        debt=int(input('请下注: '))
        if debt>money:print('资金不够')
        if 0<debt<=money:
            break
    x1=random.randint(1,6) 
    x2=random.randint(1,6) 
    x=x1+x2
    print('你摇出了%d点'%x)
    if x in (7,11):
        money=money+debt
        print('你赢了，资金为：%d'%money)
    elif x in (2,3,12):
        money=money-debt
        print('你输了，资金为：%d'%money)
    else:
        flag=1
        while flag:
            x1=random.randint(1,6) 
            x2=random.randint(1,6) 
            print('你摇出了%d点,第一次为%d点'%((x1+x2),x))
            if x==x1+x2:
                money=money+debt
                print('你赢了，资金为：%d'%money)
                flag=0
            elif 7==x1+x2:
                money=money-debt
                print('你输了，资金为：%d'%money)
                flag=0
    
print('资金不足，game over!')   


            
    



