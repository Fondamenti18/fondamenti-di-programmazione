def conversione(n):
    pl=('', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove')
    sl=('dieci', 'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove')
    tl=('', '', 'venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta')
    tle=('', '', 'vent', 'trent', 'quarant', 'cinquant', 'sessant', 'settant', 'ottant', 'novant')
    u=n%10
    d=n//10
    d=d%10
    c=n//100
    c=c%10
    stringa=''
#da 1 a nove
    if c==0 and d==0:
        stringa=pl[u]
#da dieci a diciannove
    elif c==0 and d==1:
        stringa=sl[u]
#da venti a novantanove
    elif c==0 and d>1:
        if u==8 or u==1:
            stringa=tle[d]+pl[u]
        else:    
            stringa=tl[d]+pl[u]
#da cento a centonove
    elif c==1 and d==0:
        stringa='cento'+pl[u]
#da centodieci a centodiciannove
    elif c==1 and d==1:
        stringa='cento'+sl[u]
#da centoventi a centonovantanove
    elif c==1 and d>1:
        if d==8:
            if u==1 or u==8:
                stringa='cent'+tle[d]+pl[u]
            else:
                stringa='cent'+tl[d]+pl[u]
        elif d>1:
            if u==8 or u==1:
                stringa='cento'+tle[d]+pl[u]
            else:
                stringa='cento'+tl[d]+pl[u]
#multipli di cento e unità
    elif c>1 and d==0:
        stringa=pl[c]+'cento'+pl[u]
#multipli di cento+y (undici<y<novantanove)
    elif c>1:
        if d==1:
            stringa=pl[c]+'cento'+sl[u]
        elif d==8:
            if u==1 or u==8:
                stringa=pl[c]+'cent'+tle[d]+pl[u]
            else:
                stringa=pl[c]+'cent'+tl[d]+pl[u]
        elif d>1:
            if u==8 or u==1:
                stringa=pl[c]+'cento'+tle[d]+pl[u]
            else:
                stringa=pl[c]+'cento'+tl[d]+pl[u]
    return(stringa)

def conv(n):  
   u=n%1000
   n=n//1000
   convu=conversione(u)
   stringaf=convu  
   if n!=0:
       k=n%1000
       n=n//1000
       if k==1:
           stringaf='mille'+stringaf
       elif k==0:
           convmig=conversione(k)
           stringaf=convmig+stringaf
       else:
           convmig=conversione(k)
           stringaf=convmig+'mila'+stringaf
       if n!=0:
           m=n%1000
           n=n//1000
           convoni=conversione(m)
           if m==0:
               stringaf=convoni+stringaf
           else:
               stringaf=convoni+'milioni'+stringaf
           if n!=0:
               g=n%1000
               n=n//1000
               convardi=conversione(g)
               if g==0:
                   stringaf=convardi+stringaf
               else:
                   stringaf=convardi+'miliardi'+stringaf
   return(stringaf)
   print(stringaf)