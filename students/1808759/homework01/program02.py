def conv(n):
    ls=["","uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]
    decine=["venti", "trenta", "quaranta","cinquanta", "sessanta", "settanta", "ottanta", "novanta"]
    decine1=["vent", "trent", "quarant","cinquant", "sessant", "settant", "ottant", "novant"]
    centinaia:[]
    if n<19:
        return ls[n]
    elif n<=99:
        if n%10==0:
            return decine[int(n/10-2)]
        elif n%10==1 or n%10==8:
            return decine1[int(((n-(n%10))/10)-2)]+ls[int(n%10)]
        else:
            return decine[int(((n-(n%10))/10)-2)]+ls[int(n%10)]
    elif n<=199:
        if n%100==0:
            return 'cento'
        elif 1<=(n-100)<=19:
            return 'cento'+ls[int(n-100)]
        elif 80<=(n-100)<=89:
            if (n%100)%10==1 or (n%100)%10==8:
                return 'cent'+decine1[int((((n-100)-((n%100)%10))/10)-2)]+ls[int(n%100)%10]
            else:
                return 'cent'+decine[int((((n-100)-((n%100)%10))/10)-2)]+ls[int(n%100)%10]
        elif (n%100)%10==1 or (n%100)%10==8:
            return 'cento'+decine1[int((((n-100)-((n%100)%10))/10)-2)]+ls[int(n%100)%10]
        else:
            return 'cento'+decine[int((((n-100)-((n%100)%10))/10)-2)]+ls[int(n%100)%10]
    elif n<=999:
        if n%100==0:
            return ls[int(n/100)]+'cento'
        elif 1<=(n%100)<=19:
            return ls[int(n/100)]+'cento'+ls[int(n%100)]
        elif 80<=(n%100)<=89:
            if (n%100)%10==1 or (n%100)%10==8:
                return ls[int(n/100)]+'cent'+decine1[int((((n%100)-((n%100)%10))/10)-2)]+ls[int(n%100)%10]
            else:
                return ls[int(n/100)]+'cent'+decine[int((((n%100)-((n%100)%10))/10)-2)]+ls[int(n%100)%10]
        elif (n%100)%10==1 or (n%100)%10==8:
            return ls[int(n/100)]+'cento'+decine1[int((((n%100)-((n%100)%10))/10)-2)]+ls[int(n%100)%10]
        else:
            return ls[int(n/100)]+'cento'+decine[int((((n%100)-((n%100)%10))/10)-2)]+ls[int(n%100)%10]
    #vedo che la funzione si ripete:la riapplico per velocizzare il procedimento(in alternativa avrei pututo richiamare delle funzioni per le decine,centinaia e migliaia)
    elif n<=1999:
       return 'mille'+conv(n%1000)
   
    elif n<=9999:
        return ls[int(n/1000)]+'mila'+conv(int(n%1000))
    
    elif n<=19999:
        return ls[int(n/1000)]+'mila'+conv(int(n%1000))
    elif n<=99999:
        return conv(int(n/1000))+'mila'+conv(int(n%1000))
    elif n<=999999:
        return conv(int(n/1000))+'mila'+conv(int(n%1000))
    elif n<=1999999:
        return 'unmilione'+conv(n%1000000)
    elif n<=999999999:
        return conv(int(n/1000000))+'milioni'+conv(int(n%1000000))
    elif n <= 1999999999:
        return 'unmiliardo'+conv(n%1000000000)
    elif n<=99999999999:
         return conv(int(n/1000000000))+'miliardi'+conv(int(n%1000000000))
  
            
   
  
