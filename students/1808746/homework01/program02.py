def conv(n):
    primiDiciannove=["uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci",
                     "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette",
                     "diciotto", "diciannove"]
    decine=["venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]
    if n == 0: 
        return ""
    elif n<20:
        return primiDiciannove[n-1]
    elif n<100:
        risultato = decine[n//10-2]
        d=n%10
        if d==1 or d==8:
            risultato = risultato[:-1]
        return risultato + conv(n%10)     
    elif n<200:
        return "cento" + conv(n%100)    
    elif n<1000:
        m=n%100
        m=m//10
        risultato = "cento"
        if m==8:
            risultato = risultato[:-1]
        return conv(n//100) + risultato + conv(n%100)   
    elif n<2000 :
        return "mille" + conv(n%1000)
    elif n<1000000:
        return conv(n//1000) + "mila" + conv(n%1000)    
    elif n<2000000:
        return "unmilione" + conv(n%1000000)      
    elif n <= 1000000000:
        return conv(n//1000000)+"milioni" +conv(n%1000000)
    elif n <= 1999999999:
        return "unmiliardo" + conv(n%1000000000)
    else:
        return conv(n//1000000000) + "miliardi" +conv(n%1000000000)