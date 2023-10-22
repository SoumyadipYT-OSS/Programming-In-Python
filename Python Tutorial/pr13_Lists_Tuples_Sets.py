# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:45:54 2023

@author: Soumyadip
"""

# =============================================================================
#  Lists, Tuples and Sets in python
# =============================================================================

# Lists
print("___Lists in python___")
students = ["Soumyadip", 91, "Debraj", 89, "Saswat", 88, "Mansish", 90, "Sreeyansh", 88]
for x in range(0, len(students), 2):
    print(" ", students[x], " rating ", students[x+1])
print(students)

# updating new value
students.append("Ashutosh")
students.append(95)

print("__Updated List__")
for y in range(0, len(students), 2):
    print(" ", students[y], " rating ", students[y+1])
print(students)

print("new list example")
fruits1 = ["Apple", 10, "Guava", 15, "Grapes", 16]
print(fruits1)
fruits2 = ["Pomegranate", 18, "Lemon", 20]
fruits1.extend(fruits2)
print(fruits1)
fruits1.remove("Pomegranate")       # using simple remove method to pass the value which you will remove
fruits1.remove(18)
print(fruits1)
fruits1.pop()       # If you use pop() method without parameter, it will delete the Last_In value like Stack
print(fruits1)
fruits1.pop(0)
fruits1.pop(1)
fruits1.pop(-1)     # to remove the last index
print(fruits1)
fruits1.clear()     # to empty the list
print(fruits1)


# we have taken a number list to use various methods on it
numbers_list = [10, 15, 4, 2, 9, 6, 11, 10]
names_list = ["Pinku Shaw", "Swathi Di", "Tamal Da", "Ayush", "Ayon", "Soumyadip"]
print("__Before sort__")
print(numbers_list)
print(names_list)
print("__After sort__")
numbers_list.sort()
names_list.sort()
print(numbers_list)
print(names_list)
# copy data
new_name_list_backup = names_list.copy()
print(new_name_list_backup)



# Tuples
print("__TUPLES in python__")
prices = (29.95, 4.5, 15.5, 4.5)
print(4.5 in prices)
print(1.5 not in prices)
print(prices.count(4.5))
print(prices[0])




# Sets
print("__SETS in python__")
values = {29.95, 19.6, 8.5, 8.5}; print(values);
values.add(20)
values.update([10, 15, 25]); print("Updating values")
print(values)