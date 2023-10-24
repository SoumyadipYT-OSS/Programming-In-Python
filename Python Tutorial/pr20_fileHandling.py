# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:49:54 2023

@author: soumyadip
Topic: File handling
"""
# open and description the file
print("__Open the file__")
fhand = open('test.txt')
print(fhand)

# read file
print("__Read file__")
handle = open('test.txt', 'r')
print(handle)


# counting lines in a text file
print("__Counting line in a text file__")
fhand = open('test.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Coune: ', count)


# Reading the whole file
print("__Reading the whole file__")
fhand = open('test.txt')
inp = fhand.read()
print(len(inp))
print(inp[:])   # reading the file


# searching through a file
fhand = open('test.txt')
for line in fhand:
    if line.startswith('Created'):
        print(line)
       
        
        
# Prompt for a file name and if user input bad file names
fname = input('Enter the file name: ')
try: 
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
