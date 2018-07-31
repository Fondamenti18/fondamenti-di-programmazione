# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:48:24 2017

@author: Ali
"""


lista1= ["",'uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
lista2= ['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
lista3= ["","",'due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
def conv(n):
    if n<=19:
        return lista1[n]
    elif n<100:
        lettera=lista2[(n//10)-2]
        unita=n%10
        if unita==1 or unita==8:
            lettera=lettera[:-1]
        return lettera + conv(unita)
    elif n<1000:
        centinaia=n//100
        decine=n%100
        d=decine//10
        if centinaia==1:
            return "cento" + conv(decine)
        if d != 8:
            lett = "cento"
        else:
            lett = "cent"
        return conv(centinaia) + lett + conv(decine)
    elif n<10**6:
        centinaia=n//1000
        decine=n%1000
        return conv(centinaia) + 'mila' + conv(decine) if centinaia != 1 else "mille" + conv(decine)
    elif n<10**9:
        centinaia=n//1000000
        decine=n%1000000
        return conv(centinaia) + 'milioni' + conv(decine) if centinaia != 1 else "unmilione" + conv(decine)
    elif n<10**12:
        centinaia=n//1000000000
        decine=n%1000000000
        return conv(centinaia) + 'miliardi' + conv(decine) if centinaia != 1 else "unmiliardo" + conv(decine)
     
    
    
        
    