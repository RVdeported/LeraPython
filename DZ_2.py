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
"""
inp = input("Enter nums via space\n")
Array = inp.split(" ")
for a, b in enumerate(Array):
    if a == len(Array) - 1:
        break
    if a % 2 == 0:
        Array[a] = Array[a+1]
        Array[a+1] = b
        print (str(Array[a]) + " " + str(Array[a+1]))
print(str(Array[len(Array)-1]))
print("Result " + str(Array))  

"""
"""
arr = [10,20]
buff = arr[a] #buff = 10
arr[a] = arr[a+1] # [20,20]
arr[a+1] = buff # [20,10]
print(arr)
"""
"""
inp = int(input("Enter a month\n"))
inp = inp - 1
Array = ["зима","зима",
         "весна","весна","весна",
         "лето","лето","лето",
         "осень","осень","осень","зима"]
print(str(Array[inp]))
"""
"""
inp = input("Enter a month\n")
dictt = {
        "0" : "zima",
        "1" : "vesna"
        }
print(dictt[inp])
"""
"""
char word[10] = ["W", "i", "n"]
string word = "Win"
"""
"""
word = "456789"
print(word[3:])
"""
"""
inp = input("enter two words\n")
inp=inp.split(" ")
for a,d in enumerate(inp):
    print(str(a) + " " + str(d[:10]))
"""
"""
inp = input("enter two words\n")
inp=inp.split(" ")
l=len(inp)
i=0
while i < l:
    print(str(i) + " " + str(inp[i][:10]))
    i=i+1
"""

class dog():
    def __init__(self, dog_type):
        self.Type = dog_type
        print("The " + self.Type + " dog initiated")
    Type = "Taksa"
    color = "blue"
    def shout(self):
        print("I'm " + self.Type + " and shouting loud with my color " + self.color)



belka = dog("Korol")
print(belka.Type)
belka.Type = "Layka"
print(belka.Type)
belka.shout()

    
    
    
    



