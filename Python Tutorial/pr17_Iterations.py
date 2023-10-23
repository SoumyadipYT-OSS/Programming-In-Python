# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 01:12:08 2023

@author: soumyadip
Topic: Iterations: Loop Idioms
"""

# =============================================================================
# FINDING THE LARGEST VALUE
# =============================================================================
print("__Example1__")
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)



# =============================================================================
# FINDING THE SMALLEST VALUE
# =============================================================================
print("__Example2__")
smallest = None
print('Before:', smallest)
givenSet = [3, 41, 12, 9, 74, 15]
for i in givenSet:
    if smallest is None or i<smallest:
        smallest = i
    print("Loop: ", i, smallest)
print("Smallest: ", smallest)