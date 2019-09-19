# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:24:03 2019

@author: Aspire
"""
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate Per Hour:")
r = float(rate)

if (h>40):
    x = h-40
    pay = 40*r+x*r*1.5
else :
    pay = h*r

print (pay)
        

            
        
            
            
    
    
    

 
 

    
    