# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:07:02 2023

@author: Soumyadip
"""

# =============================================================================
#   WHILE LOOP IN PYTHON
# =============================================================================
initialize_digit = 65
while initialize_digit < 91:
    print(str(initialize_digit)+" = "+chr(initialize_digit))
    initialize_digit+=1
print("Loop completed first part")



counter = 65
while counter < 91:
    if counter < 80:
        counter += 1 
        continue
    print(str(counter)+" = "+chr(counter))
    counter += 1
    if counter > 86:
        break
print("Loop completed for the second part")        