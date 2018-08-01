def conv(n):
    a=n%100
    b=n%1000
    c=n%1000000
    d=n%1000000000
    if n==0:
        return 'zero'
    elif n<=9:
        unità=['uno','due','tre','quattro','cinque','sei','sette','otto','nove']
        return unità[n-1]
    elif n<=19:
        dieci=['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
        n=n%(10)
        return dieci[n]
    elif n<=99:
        decine=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
        t=n%10
        letter=decine[int(n/10)-2]
        if t==0:
            return letter
        if t==1 or t==8:
            letter=letter[ :-1]
        return letter+conv(n%10)
    elif n<=199:
        if (a)==0:
            return 'cento'
        if 80<=(a)<=89:
            return 'cent'+conv(a)
        else:
            return 'cento'+conv(a)
    elif n<=999:
        m=int(n/100)
        k=(a)+100
        if k==100:
            return conv(m)+'cento'
        else:
            return conv(m)+conv(k)
    elif n<=1999:
        if (b)==0:
            return 'mille'
        else:
            return 'mille'+conv(b)
    elif n<=999999:
        if (b)==0:
            return conv(int(n/1000))+'mila'
        else:
            return conv(int(n/1000))+'mila'+conv(b)
    elif n<=1999999:
        if (c)==0:
            return 'unmilione'
        else:
            return 'unmilione'+conv(c)
    elif n<=999999999:
        if (c)==0:
            return conv(int(n/1000000))+'milioni'
        else:
            return conv(int(n/1000000))+'milioni'+conv(c)
    elif n<=1999999999:
        if (d)==0:
            return 'unmiliardo'
        else:
            return 'unmiliardo'+conv(d)
    elif n<1000000000000:
        if (d)==0:
            return conv(int(n/1000000000))+'miliardi'
        else:
            return conv(int(n/1000000000))+'miliardi'+conv(d)
