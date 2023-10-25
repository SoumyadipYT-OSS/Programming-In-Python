# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 01:36:36 2023

@author: soumyadip
Topic: Lists
"""

# =============================================================================
# Lists are mutable this is important line
# =============================================================================

# Example 1
print("__Example 1__")
print([1, 24, 76])
print(['red', 'yellow', 'blue'])
print('red', 24, '45')

# Example 2
print("__Example 2__")
friends = ['Ashutosh', 'Mansish', 'Saswat']
print(friends)

# Example 3
print("__Example 3__")
ex2 = [2, 14, 26, 41, 63]
print("Original ex2 list: ", ex2)
ex2[2] = 28
print("Updated list: ", ex2)

# Example 4
print("__Example 4__")
fruits = ['Banana', 'Orange', 'Lemon', 'Pomegranate', 'Apple']
for index in fruits:
    x = index.lower()
    print(x)


# Example 5
print("__Example 5__")
greet = 'Hello World'
print(greet)
print(len(greet))
x = [1, 2, 'Lenovo', 'ideapad']
print(x)
print(len(x))


# Example 6
print("__Example 6__")
programLanguages = ['C', 'C#', 'Python', 'Java']
print(programLanguages)
print(len(programLanguages))
