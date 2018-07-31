# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:39:41 2017

@author: tmald
"""
def conv(x):
    base=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','dicianove','venti']
    #multipli di 10
    mdd=['','','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    #ogni tre cifre
    otc=['miliardi','milioni','mila','']
    otcu=['miliardo','milione','mille','']
    cont=''
    risposta=''
    a=1000000000000
    b=1000000000
    j=0
    while j<4:
        n=(x%a)//b
        if (x%a)//b!=0:
            dec=(n%100)//10
            uni=n%10
            cent=n//100
            if n%100<21:
                cont=base[n%100]
            else:        
                if uni==1 or uni==8:
                    cont=str(mdd[dec][:-1])+str(base[uni])
                else:
                    cont=str(mdd[dec])+str(base[uni])
            if cent>0:
                if cent==1:
                    if dec==8:
                        cont='cent'+cont
                    else:
                        cont='cento'+cont
                else:
                    if dec==8:
                        cont=str(base[cent])+'cent'+cont
                    else:
                        cont=str(base[cent])+'cento'+cont 
            
            if (x%a)//b==1:
                if (x%a)//b==1 and j==2:
                    risposta+=otcu[j]
                else:
                    risposta+=str(cont)[:-1]+otcu[j]
            else:
                risposta+=str(cont)+otc[j]
        
        j+=1
        a=a//1000
        b=b//1000
    return risposta