def conv(n):
    if n < 0:
        return ""
    elif n == 0:
        return ""
    elif n <= 19:
        numero = ("uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto","nove", "dieci","undici","dodici","tredici","quattordici","quindici","sedici","diciassette","diciotto","diciannove")
        return numero[n-1]
    elif n <= 99:
        decina = ("venti", "trenta", "quaranta","cinquanta","sessanta","settanta","ottanta","novanta")
        decinaInLettere = decina[int(n/10)-2]
        if( n%10 == 1 or n%10 == 8):
            return decinaInLettere[:-1] + conv(n%10)
        else:
            return decinaInLettere + conv(n%10)
    elif n <= 999:
        centinaia = ("cento", "duecento","trecento","quattrocento","cinquecento","seicento","settecento","ottocento","novecento")
        centinaiainlettere = centinaia[int(n/100)-1]
        if(n%100 > 79 and  n%100 < 90):
            return centinaiainlettere[:-1] + conv(int(n%100))
        elif( n%100 == 0):
            return centinaiainlettere
        else:
            return centinaiainlettere + conv(int(n%100))
    elif n <= 1999:
        mille = "mille"
        return mille + conv(int(n%1000))
    elif n <= 999999:
        mila = "mila"
        return conv(int(n/1000)) + mila + conv(int(n%1000))
    elif n <= 1999999:
        milione = "unmilione"
        return milione + conv(n%1000000)
    elif n <= 999999999:
        milioni = "milioni"
        return conv(int(n/1000000)) + milioni + conv(int(n%1000000))
    elif n <= 1999999999:
        miliardo = "unmiliardo"
        return miliardo + conv(int(n%1000000000))
    elif n <= 999999999999:
        miliardi = "miliardi"
        return conv(int(n/1000000000)) + miliardi + conv(int(n%1000000000))
