Python 3.6.2 |Anaconda, Inc.| (default, Sep 20 2017, 13:35:58) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def cnv(n):
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
        return letter + cnv(n%10)
         
    elif n <= 199:
        return "cento" + cnv(n%100)
         
    elif n <= 999:
        m = n%100
        m = int(m/10)
        letter = "cent"
        if m != 8:
            letter = letter + "o"
        return cnv( int(n/100)) + 
               letter + 
               cnv(n%100)
         
    elif n<= 1999 :
        return "mille" + cnv(n%1000)
     
    elif n<= 999999:
        return cnv(int(n/1000)) + 
               "mila" + 
               cnv(n%1000)
         
    elif n <= 1999999:
        return "unmilione" + cnv(n%1000000)
         
    elif n <= 999999999:
        return cnv(int(n/1000000))+ 
               "milioni" + 
               cnv(n%1000000)
    elif n <= 1999999999:
        return "unmiliardo" + cnv(n%1000000000)
         
    else:
        return cnv(int(n/1000000000)) + 
               "miliardi" + 
               cnv(n%1000000000)
 
