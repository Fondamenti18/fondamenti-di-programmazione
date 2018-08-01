def primi_cento(n): 
    primi_diciannove=('uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici',
                      'tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove')
    if n <= 19:
        if n==0:
            return ''
        else:
            return (primi_diciannove[n-1])
    elif n <= 99:
        decine=('venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta')
        decina_n=decine[(n//10)-2]
        if n%10 in (1, 8):
            return (decina_n[:-1]+conv(n%10))
        else:
            if n%10==0:
                return decina_n
            else:
                return decina_n+conv(n%10)
def conv(n):
    if n <= 99:
        return primi_cento(n)
    elif n <= 199:
        if (n%100)//10==8:
            return 'cent'+conv(n%100)
        else:
            return 'cento'+conv(n%100)
    elif n <= 999:
        if (n%100)//10==8:
            return conv(n//100)+'cent'+conv(n%100)
        else:
            return conv(n//100)+'cento'+conv(n%100)
    elif n<= 1999 :
        return 'mille' +conv(n%1000)
    elif n<= 999999:
        return conv(n//1000)+'mila'+conv(n%1000)    
    elif n <= 1999999:
        return 'unmilione'+conv(n%1000000)   
    elif n <= 999999999:
        return conv(n//1000000)+'milioni'+conv(n%1000000)
    elif n <= 1999999999:
        return 'unmiliardo'+conv(n%1000000000)     
    else:
        return conv(n//1000000000)+'miliardi'+conv(n%1000000000)


