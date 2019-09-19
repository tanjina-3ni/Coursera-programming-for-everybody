# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:35:05 2019

@author: Aspire
"""


largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        inp = int(num)    
    except:
        print ("Invalid input")
        

    if largest is None:
        largest = inp
    elif(inp > largest):
        largest = inp

    if smallest is None:
        smallest =inp
    elif inp < smallest:
        smallest = inp

print ("Maximum is", largest)
print ("Minimum is", smallest)