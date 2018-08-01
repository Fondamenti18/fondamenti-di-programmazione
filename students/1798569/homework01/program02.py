
def conv(n):
    listaNum=["uno","due","tre","quattro","cinque","sei","sette","otto","nove",
              "dieci","undici","dodici","tredici","quattordici","quindici","sedici",
              "diciassette","diciotto","diciannove"]
    listaDec=["venti","trenta","quaranta","cinquanta","sessanta","settanta",
              "ottanta","novanta"]
    stringa=''
    if n==0:
        return ''
    
    elif n<=19:
        stringa=listaNum[n-1]
        return stringa
        
        
    elif n<=99:
        dec= (n//10)-2     
        unit=(n%10)
        lettere=listaDec[dec]
        if unit == 1 or unit == 8:
          lettere=lettere[:-1]
        stringa=lettere + conv(unit)
        return stringa

    elif n <= 199:
        dec=  n%100
        stringa='cento'+conv(dec)
        return stringa
    
    elif n<=999:
        cent= (n//100)
        dec=  n%100
        unit = n%100
        unit = int(unit/10)
        lettere='cent'
        if unit!=8:
            lettere = lettere + "o"
        stringa=listaNum[cent-1]+lettere+conv(dec)
        return stringa
    
    elif n<= 1999 :
        mila= (n%1000)
        stringa='mille'+conv(mila)
        return stringa
    
    elif n<=999999:
        mila= (n//1000)
        cent= (n%1000)
        stringa=conv(mila)+'mila'+conv(cent)
        return stringa
    
    elif n <= 1999999:
        mila=(n%1000000)
        stringa='unmilione'+conv(mila)
        return stringa
    
    elif n<=999999999:
        mili=(n//1000000)
        mila=(n%1000000)
        stringa=conv(mili)+'milioni'+conv(mila)
        return stringa
    
    elif n <= 1999999999:
        mili=(n%1000000000)
        stringa='un milardo' +conv(mili)
        return stringa
    
    elif n<=999999999999:
        miliardi=(n//1000000000)
        mili=(n%1000000000)
        stringa=conv(miliardi)+'miliardi'+conv(mili)
        return stringa 