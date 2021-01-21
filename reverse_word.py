# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:56:39 2021

@author: ADITYA TANWAR
"""
#2. Reverse of word in given string

strg=input("Enter the string :")       
words = strg.split(' ')  #split into word
reverse_strg = ' '.join(reversed(words))       
print (reverse_strg)          #printing string with reverse word