# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 21:36:37 2023

@author: Soumyadip
"""

# =============================================================================
#   WORKING WITH STRINGS IN PYTHON
# =============================================================================
s1 = ""
s2 = " "
s3 = "a b c"
print(len(s1))
print(len(s2))
print(len(s3))

fullName = "Soumyadip"
print("S" in fullName)
print("s" in fullName)
print('S' in fullName)
print('s' in fullName)
print('a' in fullName)
print('y' in fullName)
print(fullName[0])
print(fullName[5])
print(fullName[4])
print(fullName[:])  # accessing all the characters using '[:]'
print(fullName[0 : 2])
print(fullName[0 : 6])

word1 = "This is SPYDER IDE"
print(word1)
print(word1.capitalize())
print(word1.lower())
print(word1.upper())
print(word1.title())    # show without spaces
print(word1.swapcase()) # uppercase become lower and vice-versa

word2 = "abcd"
print(word2.isalpha())
print(word2.isascii())

word3 = "ab3d"
print(word3.isalpha())
print(word3.isalnum())