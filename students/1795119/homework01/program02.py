numeri = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]
decine = ["venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]

def conv(n):
    'Scrivete qui il codice della funzione'
    if n <= 19: #0-19
        return numeri[n]
    elif n <= 99:   #20-99
        result = decine[n//10-2]
        unita = n%10
        if unita == 1 or unita == 8:
            result = result[:-1]
        return result + numeri[unita]
    elif n <= 199:  #100-199
        return "cento" + conv(n%100)
    elif n <= 999:  #200-999
        unita = (n%100)//10
        cento = "cent"
        if unita != 8:
            cento+="o"
        return conv(n//100) + cento + conv(n%100)
    elif n <= 1999: #1.000-1.999
        return "mille" + conv(n%1000)
    elif n <= 999999:   #2.000-999.999
        return conv(n//1000) + "mila" + conv(n%1000)
    elif n <= 1999999:  #1.000.000-1.999.999
        return "unmilione" + conv(n%1000000)
    elif n <= 999999999:    #2.000.000-999.999.999
        return conv(n//1000000) + "milioni" + conv(n%1000000)
    elif n <= 1999999999:   #1.000.000.000-1.999.999.999
        return "unmiliardo" + conv(n%1000000000)
    else:   #2.000.000.000-999.999.999.999
        return conv(n//1000000000) + "miliardi" + conv(n%1000000000)
