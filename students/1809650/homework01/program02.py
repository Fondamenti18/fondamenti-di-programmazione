def conv(n):
    if n == 0: 
        return ""
        
    elif n <= 19:
        return ("uno", "due", "tre", "quattro", "cinque", 
                "sei", "sette", "otto", "nove", "dieci", 
                "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto", "diciannove")[n-1]
                
    elif n <= 99:
        dec = ("venti", "trenta", "quaranta",
                  "cinquanta", "sessanta", 
                  "settanta", "ottanta", "novanta")
        letter = dec[int(n/10)-2]
        p = n%10
        if p == 1 or p == 8:
            letter = letter[:-1]
        return letter + conv(n%10)
        
    elif n <= 199:
        return "cento" + conv(n%100)
        
    elif n <= 999:
        t = n%100
        t = int(t/10)
        letter = "cent"
        if t != 8:
            letter = letter + "o"
        return conv( int(n/100)) + \
               letter + \
               conv(n%100)
        
    elif n<= 1999 :
        return "mille" + conv(n%1000)
    
    elif n<= 999999:
        return conv(int(n/1000)) + \
               "mila" + \
               conv(n%1000)
        
    elif n <= 1999999:
        return "unmilione" + conv(n%1000000)
        
    elif n <= 999999999:
        return conv(int(n/1000000))+ \
               "milioni" + \
               conv(n%1000000)
    elif n <= 1999999999:
        return "unmiliardo" + conv(n%1000000000)
        
    else:
        return conv(int(n/1000000000)) + \
               "miliardi" + \
               conv(n%1000000000)
