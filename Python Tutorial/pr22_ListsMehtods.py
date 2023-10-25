# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 02:06:38 2023

@author: soumyadip
Topic: Lists method
"""

# Example 1
print("__Example 1__")
x = list()
print(x)
print(type(x))


# Example 2
print("__Example 2__")
y = dir()
print(y)
print(type(y))


# Example 3
print("__Example 3__")
z = dir(x)
print(z)


# Example 4
print("__Example 4__")
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums) / len(nums))


# Example 5
print("__Example 5__")
numList = list()
print("write 'done' when you have complete your list")
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : 
        break
    
    value = float(inp)
    numList.append(value)

average = sum(numList) / len(numList)
print('Average: ', average)

