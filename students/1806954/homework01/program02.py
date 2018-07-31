listU=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici',
           'dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto',
           'diciannove']
listD=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta',
            'novanta']
listD1=['vent','trent','quarant','cinquant','sessant','settant','ottant',
            'novant']

def dec(n):
    i=n//10-2 #decine in listD
    u=n%10 #unità
    if u==1 or u==8:
        s2=listD1[i] + conv(u)
    else:
        s2=listD[i] + conv(u)
    return s2

def cent(n):
    u=n%100
    i=n//100 #centinaia
    if i!=1:
        if u>=80 and u<=89:
            s3=listU[i] + 'cent' + conv(u)
        else:
            s3=listU[i] + 'cento' + conv(u)
    else:
        s3='cento' + conv(u)
    return s3

def mig(n):
    u=n%1000
    i=n//1000 #migliaia
    if i!=1:
        s4=conv(i) + 'mila' + conv(u)
    else:
        s4='mille' + conv(u)
    return s4

def milio(n):
    u=n%1000000
    i=n//1000000  #milioni
    if i!=1:
        s5=conv(i)+'milioni'+conv(u)
    else:
        s5='un milione'+conv(u)
    return s5

def milia(n):
    u=n%1000000000
    i=n//1000000000 #miliardi
    if i!=1:
        s6=conv(i)+'miliardi'+conv(u)
    else:
        s6='un miliardo'+conv(u)
    return s6

def conv(n):
    if n<20:
        s=listU[n]
        return s
    elif n<100:
        return dec(n)
    elif n<1000:
        return cent(n)
    elif n<1000000:
        return mig(n)
    elif n<1000000000:
        return milio(n)
    elif n<1000000000000:
        return milia(n)