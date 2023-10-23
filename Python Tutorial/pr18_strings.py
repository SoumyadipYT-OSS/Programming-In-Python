# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:15:45 2023

@author: soumyadip
Topic: String data type
"""

print("__Example1__")
model = 'Lenovo'
letter = model[1]
print(letter)

x = 3
w = model[x-1]
print(w)

print(len(model))   # len() to calculate length of string



print("__Example2__")
fruit = 'banana'
for letter in fruit:
    print(letter)
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
    

print("__Example3__")
word = 'banana'
count = 0
for i in word:
    if i == 'a':
        count = count + 1
print(count)
