#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 08:25:36 2017

@author: teresa
"""

l1=['uno','due','tre','quattro','cinque','sei' ,'sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
l2=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']

def conv(n):
    risultato=""
    if (n>0 and n<20):
        return l1[n-1]
    elif (n in [20,30,40,50,60,70,80,90]):
        return l2[(n//10)-2]
    elif (n in [21,31,41,51,61,71,81,91]):
        l3=l2[(n//10)-2]
        return l3.strip(l3[-1])+'uno'
    elif (n in [28,38,48,58,68,78,88,98]):
        l3=l2[(n//10)-2]
        return l3.strip(l3[-1])+'otto'
    elif (n>21 and n<100):
        return l2[(n//10)-2]+l1[(n%10)-1]
    elif n==100:
        return 'cento'
    elif (n>100 and n<200):
        risultato+='cento'
        q=n-100
        return risultato+conv(q)
    elif (n>199 and n<1000):
        q=n//100
        n=n-q*100
        if (n in [80,81,82,83,84,85,86,87,88,89]):
            risultato+=l1[q-1]+'cent'+conv(n)
        else:
            risultato+=l1[q-1]+'cento'+conv(n)
        return risultato

    elif n==1000:
        return 'mille'
    elif (n>1000 and n<2000):
        risultato+='mille'+conv(n-1000)
    elif (n>1999 and n<10000):
        risultato+=conv(n//1000)+'mila'+conv(n-(n//1000)*1000)
    elif (n>9999 and n<100000):
        risultato+=conv(n//1000)+'mila'+conv(n-(n//1000)*1000)    
    elif (n>99999 and n<1000000):
        risultato+=conv(n//1000)+'mila'+conv(n-(n//1000)*1000)    
    elif (n==1000000):
         risultato+='un milione'
    elif (n>1000000 and n<2000000):
        risultato+='un milione'+conv(n-1000000)    
    elif (n>1999999 and n<1000000000):
        risultato+=conv(n//1000000)+'milioni'+conv(n-(n//1000000)*1000000)    
    elif (n==1000000000):
         risultato+='un miliardo'
    elif (n>1000000000 and n<2000000000):
        risultato+='un miliardo'+conv(n-1000000000)    
    elif (n>1999999999 and n<1000000000000):
        risultato+=conv(n//1000000000)+'miliardi'+conv(n-(n//1000000000)*1000000000)    
    return risultato
        