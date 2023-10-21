# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:29:52 2023

@author: Soumyadip
"""
for x in range(1,11):
    print("Iteration: ",x)

# Using Jumping Notation
for y in range(1,11,2):
    print("Jump iteration value: ",y)   # jump by 2
    
my_str = "STRING"
for z in my_str:
    print("Character: ",z)
    

_List = ["A", "B", "C"]
for x in _List:
    for y in range(3):
        print(y)
    print(x)