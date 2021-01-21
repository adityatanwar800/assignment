# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:51:02 2021

@author: ADITYA TANWAR
"""
#4 Fake Calculator Addtion of two number without carry

import math 
a= int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
sum1 = 0
result = 0
place = 1
while (a or b) :
    sum1 = ((a % 10) + (b % 10)) 
    sum1 = sum1 % 10               # Neglect carry
    result = result + (sum1 *place)
    a = math.floor(a / 10) 
    b = math.floor(b / 10) 
    place = place* 10   # Update place value 
print (result) 