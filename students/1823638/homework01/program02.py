def conv(n):
    unita1=['', 'uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    decine1=['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    decine2=['venti','trenta','quaranta','cinquanta','sessanta', 'settanta','ottanta','novanta']
    centinaia=['cento','duecento','trecento','quattrocento','cinquecento','seicento','settecento','ottocento','novecento']
    
    if n<=9:
        return unita1[n]
    elif n>=10 and n<=19:
        return decine1[n-10]
    elif n>=20 and n<=99:
        num=n%10
        if num==8 or num==1:
            return decine2[n//10-2][:-1] + unita1[n%10]
        else:
            return decine2[n//10-2] + unita1[n%10]
    elif n>=100 and n<=999:
        numc=n%100
        if numc>=80 and numc<=89:
            return centinaia[n//100-1][:-1] + conv(n%100)
        else:
            return centinaia[n//100-1] + conv(n%100)
    elif n>=1000 and n<=1999:
        return 'mille' + conv(n%1000)
    elif n>=2000 and n<=999999:
        return conv(n//1000) + 'mila' + conv(n%1000)
    elif n>=1000000 and n<=1999999:
        return conv(n//1000000)[:-1] + 'milione' + conv(n%1000000)
    elif n>=2000000 and n<=999999999:
        return conv(n//1000000) + 'milioni' + conv(n%1000000)
    elif n>=1000000000 and n<=1999999999:
        return 'unmiliardo' + conv(n%1000000000)
    elif n>=1000000000 and n<=999999999999:
        return conv(n//1000000000) + 'miliardi' + conv(n%1000000000)