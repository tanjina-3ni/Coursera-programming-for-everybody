# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:24:03 2019

@author: Aspire
"""
score = input("Enter Score: ")
s = float(score)
if (s>0.0 and s<1.0) :
    if (s>= 0.9):
        print('A')
    elif(s>= 0.8):
        print('B')
    elif(s>= 0.7):
        print('C')
    elif(s>= 0.6):
        print('D')
    else:
        print('F')
else:
    print('Out of range')
    
    
    

 
 

    
    