# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 19:08:12 2021

@author: Roman
"""

"""
Array = [11,12,13,14,"Word",16,17,18,19]

i = 0
while (i < len(Array)):
    print(Array[i])
    i += 1

dictt = {
        "Word" : "descaription",
        "Word2" : "descaription2"
        }
dictt["Word"]
"""
"""
for n in Array:
    print(n)
"""
"""
Array = [1,2,3,"bebebe",5,6,"besit","hren'",[9],[8],[7]]
Array2 = [9,8,7]
for n in Array :
    print (type(n))
    if type(n) == list:
        print(n[0])
    else:
        print (n)
"""
"""
for ind, n in enumerate(Array):
    print(str(ind)+" "+str(n))
""" 

Array = [1,2,3,"bebebe",5,6,"besit","hren'",[9],[8],[7]]
for a, b in enumerate(Array):
    if a == len(Array) - 1:
        break
    if a % 2 == 0:
        Array[a] = Array[a+1]
        Array[a+1] = b
        print (str(Array[a]) + " " + str(Array[a+1]))
print(str(Array[len(Array)-1]))  
"""
arr = [10,20]
buff = arr[a] #buff = 10
arr[a] = arr[a+1] # [20,20]
arr[a+1] = buff # [20,10]
print(arr)
"""
 
  
    
