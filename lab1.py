# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:35:09 2021

@author: Dell
"""
import math 
print('Hello World!')

#1---

r=1.5
Area=math.pi*r**2
print('Area: ',Area)

#2--

a=2
b=3

c=a**2+b**2
print('c: ',c)

#3--
factorial=1

x=0.5
for n in range(1,5):
    for i in range(1,n):
        factorial=factorial*i
    D=((x**n)/factorial)
    n=n+1
D=D+1
print('D: ',D)

#4--

r=1.5
Volume=((4/3)*math.pi*(r**3))
print('Volume: ',Volume)

#5--
x=(1+(5**0.5))/2
n=8
#unicode of phi= \u03C3
print('\u03C3: '+str(x))
GR=((x**n)-((1-x)**n))/math.sqrt(5)
print('GR',GR)


#6---
si=0.5
mu=0
x=0
t=(1/si*(math.sqrt(2*math.pi)))*((math.e**((-1/2)*(((x-mu)/si)**2))))
print('t: ', t)

            
