# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:20:15 2021

@author: ADITYA TANWAR
"""
#3.Largest lucky number(frequency)

lst1=list(map(int,input("Enter space seprated numbers :").split(' ')))
lst2=[]
for i in lst1:
    if lst1.count(i)==i: 
        lst2. append (int(i))
if len(lst2) > 0: 
        print (max(lst2))
else:
    print ("-1")
