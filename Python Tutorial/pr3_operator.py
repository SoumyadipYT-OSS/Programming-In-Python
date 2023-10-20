# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:41:35 2023

@author: Soumyadip
"""

# =============================================================================
#  OPERATORS IN PYTHON
# =============================================================================

# ARITHMETIC OPERATORS
print("ARITHMETIC OPERATORS")
firstNumber = 10
secondNumber = 5
print(firstNumber + secondNumber)   # addition
print(firstNumber - secondNumber)   # substraction
print(firstNumber * secondNumber)   # multiplication
print(firstNumber / secondNumber)   # division
print(firstNumber % secondNumber)   # modulus (to show the remainder value)
print(firstNumber ** secondNumber)  # expotent (here 10^5)
print(firstNumber // secondNumber)  # floor division (how many times divide)t

# COMPARISON OPERATORS
print("COMPARISON OPERATORS")
print(2 < 3)    # less than
print(3 <= 3)   # less than or equal to
print(4 > 3)    # greater than
print(5 >= 6)   # greater than or equal to
print(5 == 5)   # equals checking
print(5 == 6)   # equals checking
print(4 != 4)   # not equals checking
print(4 != 3)   # not equals checking
print("abcd" == "1234")
print("abcd" == "abcd")
print("abcd" == "abc")
print("abcd" != "abc")
print("abcd" != "abcd")
print("abcd" != "1234")
a = 5
b = 5
print(a is b)   # object identity
c = 4
d = 6
print(c is d)   # object identity

print(a is not b)   # negated object identity
print(c is not d)   # negated object identity

# BOOLEAN OPERATORS
x = 0
y = 1
print(x or y)
print(x and y)
print(not x)    # checking x is not full (0 means is not full)
print(not y)    # checking y is not full (1 means full)