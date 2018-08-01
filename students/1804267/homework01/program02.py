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
        decine = ("venti", "trenta", "quaranta",
                  "cinquanta", "sessanta", 
                  "settanta", "ottanta", "novanta")
        letter = decine[int(n/10)-2]
        t = n%10
        if t == 1 or t == 8:
            letter = letter[:-1]
        return letter + conv(n%10)
    elif n <= 199:
        return "cento" + conv(n%100)
    elif n <= 999:
        m = n%100
        m = int(m/10)
        letter = "cent"
        if m != 8:
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