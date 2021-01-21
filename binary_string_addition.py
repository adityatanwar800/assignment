# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:10:33 2021

@author: ADITYA TANWAR
"""
#1 Adding two binary strings  -(without inbuilt function)

a=input("enter binary string1 :")
b=input("enter binary string2 :")
result=""
i=len(a)-1
j=len(b)-1
carry=0
while i >= 0 or j >= 0:
    sum = carry 
    if i >=0:
        sum = sum+ord(a[i]) - ord('0') 
    if j >= 0:
        sum = sum+ord(b[j]) - ord('0') 
    i,j=i-1,j-1 
    if sum > 1:
        carry = 1 
    else:
        carry=0
    result = result + str(sum%2)
if carry != 0:
    result = result + str(carry) 
print(result[::-1]) 

#With Inbuilt function:-

#a=input()
#b=input()
#ans=bin(int(a,2) + int(b,2))
#print(str(ans[2:]))