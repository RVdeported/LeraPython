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

inp1 = int(input("please, enter a num\n"))
#s = inp1 + int(str(inp1) + str(inp1)) + int(str(inp1) + str(inp1) + str(inp1))
s = inp1 * 123
print("you entered " + str(s))
"""
"""
i = 0
lengh = 20
while i < lengh:
    #print("the number is " + str(i))
    if i == 9:
        break
    i = i + 1
"""

#inp1=int(input("Pls, inter a num\n"))
"""
step2 = int(inp1 / 10)
step3 = inp1 % 10
if step2 > step3:
    print(step2)
else : print(step3)

max_num = 0
while inp1 == 0:
    if (inp1 % 10 > max_num):
        max_num = inp1 % 10
    print("Compared " + str(inp1 % 10) + ". Curr max is " + str(max_num))
    inp1= int(inp1 / 10)
print("the result is " + str(max_num))


inp1=int(input("Pls, enter revenue\n"))
inp2=int(input("Pls, enter costs\n"))
result = inp1 - inp2
if result > 0 :
    print("Profit " + str(result))
    print("% profit " + str(result / inp1))
else :
    print("Loss " + str(result))
inp3 = int(input("Pls, enter num of emp\n"))
print("Profit per emp " + str(result / inp3))
"""
"""
inp1= 2 #int(input("Pls, enter a km\n"))
inp2= 3 #int(input("Pls, enter b km\n"))
i=1
while inp1 <= inp2 :
    print(str(i) + " день " + ": " + str(inp1))
    inp1 = round(inp1 * 1.1,2)
    i=i + 1
print(str(i) + " день " + ": " + str(inp1))
"""

    
    



 