# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:17:54 2021

@author: Roman
"""
"""
z1=int(6) 
z2="stroka" 
print(type(z1)) 
print(z2) 
 
z3=input("please, enter a 1 num\n") 
z4=input("please, enter a 2 num\n")
s=str(int(z3)+int(z4)) 
print("you entered" + s)
z5=input("pleasae, enter a word\n")
print("you entered " + z5)
"""
"""
inp1=input("please, enter a num of sec\n")
min1 = int(int(inp1) / 60)
sec1 = int(int(inp1) % 60)
chas1 = int(min1/60)
min2 = int(min1 % 60)

if sec1 < 10 :
    sec1 = str(0) + str(sec1)

if min2 < 10 :
    min2 = str(0) + str(min2)
if chas1 < 10 :
    chas1 = str(0) + str(chas1)
if chas1 > 99:
    chas1 = 99
    min2 = 59
    sec1 = 59


print("you entered " + str(chas1) + ":" + str(min2) + ":" + str(sec1))
"""

inp1 = int(input("please, enter a num\n"))
#s = inp1 + int(str(inp1) + str(inp1)) + int(str(inp1) + str(inp1) + str(inp1))
s = inp1 * 123
print("you entered " + str(s))
