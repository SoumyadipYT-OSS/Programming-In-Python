# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:32:11 2023

@author: Soumyadip
"""

# =============================================================================
#   Date and Time in Python
# =============================================================================
import datetime as dt
current = dt.date.today()
print("day: ", current.day)
print("month: ", current.month)
print("year: ", current.year)

new_date = dt.date(2023, 10, 28)
print("newDay: ", new_date.day)
print("newMonth: ", new_date.month)
print("newYear: ", new_date.year)