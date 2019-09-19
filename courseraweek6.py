# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:24:03 2019

@author: Aspire
"""
def computepay(h,r):
    if (h>40):
        x = h-40
        pay = 40*r+x*r*1.5   
    return pay

hrs = input("Enter Hours:")
hr=float(hrs);
rate = input("Enter Rate Per Hour:")
rt=float(rate);
p = computepay(hr,rt)
print(p)
            
            
    
    
    

 
 

    
    