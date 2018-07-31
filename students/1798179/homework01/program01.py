# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

ls=[121,4,37,441,7,16]
li=[ ]
ld=[121,4,37,441,7,16]

def modi(ls,k):
    i=0
    divisori=0
    x=len(ls)
    
    while i<x:
        n=2
        s=0
        while n<ls[i]:
            if ls[i]%n==0:
                s+=1
                divisori=divisori+1
            n=n+1
        if s==0:
            li.append(ls[i])
        if divisori!=k:
            ld.remove(ld[i])
            
        i+=1
        
        
    print(li)
    print(ld)           

                       