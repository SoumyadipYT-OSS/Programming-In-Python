# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 14:25:42 2023

@author: Soumyadip
"""
import datetime
import time
prefix = "Sir "
name = "Soumyadip Majumder"

LocalTime = time.localtime()
current_Time = datetime.datetime.now()
current_Hour = current_Time.hour

print(time.strftime('The time is now %I:%M %p', LocalTime))
if current_Hour < 12 and current_Hour > 3 :
    print("Good Morning, "+prefix+name)
elif current_Hour < 17 :
    print("Good Afternoon, "+prefix+name)
elif current_Hour < 23:
    print("Good Evening, "+prefix+name)
else : 
    print("Good Night, "+prefix+name)