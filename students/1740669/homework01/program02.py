def conv(s):
    if s == 0: 
        return ""
         
    elif s <= 19:
        return ("uno", "due", "tre", "quattro", "cinque", 
                "sei", "sette", "otto", "nove", "dieci", 
                "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto", "diciannove")[s-1]
                 
    elif s <= 99:
        decine = ("venti", "trenta", "quaranta",
                  "cinquanta", "sessanta", 
                  "settanta", "ottanta", "novanta")
        letter = decine[int(s/10)-2]
        l = s%10
        if l == 1 or l == 8:
            letter = letter[:-1]
        return letter + conv(s%10)
         
    elif s <= 199:
        return "cento" + conv(s%100)
         
    elif s <= 999:
        k = s%100
        k = int(k/10)
        letter = "cent"
        if k != 8:
            letter = letter + "o"
        return conv( int(s/100)) + \
               letter + \
               conv(s%100)
         
    elif s<= 1999 :
        return "mille" + conv(s%1000)
     
    elif s<= 999999:
        return conv(int(s/1000)) + \
               "mila" + \
               conv(s%1000)
         
    elif s <= 1999999:
        return "unmilione" + conv(s%1000000)
         
    elif s <= 999999999:
        return conv(int(s/1000000))+ \
               "milioni" + \
               conv(s%1000000)
    elif s <= 1999999999:
        return "unmiliardo" + conv(s%1000000000)

    elif s <= 999999999999:
        return conv(int(s/1000000000))+ \
               "miliardi" + \
               conv(s%1000000000) 

    elif s <= 1999999999999:
        return "unbiliardo" + conv(s%1000000000000)

    else:
        return conv(int(s/1000000000000)) + \
               "biliardi" + \
               conv(s%1000000000000)
