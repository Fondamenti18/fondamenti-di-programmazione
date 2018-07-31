# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:09:31 2017

@author: Gionitoo
"""

def conv(n):
    x=""
    y=str(n)
    u=["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]
    d=["", "venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]
    
    if n>0 and n<=19:
        x+=u[n]
        return x
    
    elif n>=20 and n<=99:
        eccn=n%10
        if eccn==1 or eccn==8:
            x+=d[int(y[0])-1][:-1]+conv(n%10)
        else:
            x+=d[int(y[0])-1]+conv(n%10)
        return x
    elif n>=100 and n<=199:
        eccn2=int(y[1])
        if eccn2==8:
            x+="cent"+conv(n%100)
        else:
            x+="cento"+conv(n%100)
        return x
    elif n>=200 and n<=999:
        eccn2=int(y[1])
        if eccn2==8:
            x+=conv(int(n/100))+"cent"+conv(n%100)
        else:
            x+=conv(int(n/100))+"cento"+conv(n%100)
        return x
    elif n>=1000 and n<=1999:
        x+="mille"+conv(n%100)
        return x
    elif n>=2000 and n<=999999:
        x+=conv(int(n/100))+"mila"+conv(n%1000)
        return x
    elif n>=1000000 and n<=1999999:
        x+="unmilione"+conv(n%1000000)
        return x
    elif n>=2000000 and n<=999999999:
        x+=conv(int(n/1000000))+"milioni"+conv(n%1000000)
        return x
    elif n>=1000000000 and n<=1999999999:
        x+="unmiliardo"+conv(n%1000000000)
        return x
    elif n>=2000000000 and n<=9999999999:
        x+=conv(int(n/1000000000))+"miliardi"+conv(n%1000000000)
        return x
            
        
        
    