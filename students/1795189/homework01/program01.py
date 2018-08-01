# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:57:33 2017

@author: PC
"""

def modi(ls,k):
    ls1=[]
    a=0
    delete=[]
    for n in ls:
        divisore=0
        for i in range(2,n//2+1):
            if n%i==0:
                divisore=divisore+1
            if k>divisore:
                break
        if divisore==0:
            ls1=ls1+[n]
        if k!=divisore:
            delete=delete+[a]
        a=a+1
    c=0
    for i in delete:
        del ls[i-c]
        c=c+1
    return ls1    