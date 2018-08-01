# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 23:48:43 2017

@author: Lucrezia
"""


def modi(Lista,k):
    L1=[]
    L2=[]
    
    for i in Lista:
        stringa=factors(i)
        lung=len(stringa)
        if lung==k:
            L2.append(i)
        elif lung==0:
            L1.append(i)
    Lista[:]=L2
    return L1

from math import sqrt

def factors(n):
    factors = set()
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)





