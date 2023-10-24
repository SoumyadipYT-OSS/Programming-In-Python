# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:32:45 2023

@author: soumyadip
Topic: Strings methods
"""

# Slicing strings
print("__Example1__")
s = "Python Programming"
print(s[:2])    # print two letters from beginning
print(s[8:])    # print eight letters from last
print(s[:])     # print whole string


print("__Example2__")
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)


print("__Example3__")
greet = 'Hello Soumyadip'
zap = greet.lower()
print(zap)


print("__Example4__")
fruit = 'banana'
pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)   # no letter like there so return -1 by default



print("__Example5__")
greet = 'Hello Lenovo'
nstr = greet.replace('Lenovo', 'Motorola!')
print(nstr)
nstr = nstr.replace('rola', 'xxxx')
print(nstr)