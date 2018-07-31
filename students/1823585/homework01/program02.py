def conv(n):
    if n == 0: 
        return ""
    if n <= 19:
        a=((
            "UNO","DUE","TRE",
				"QUATTRO","CINQUE", 
            "SEI","SETTE",
				"OTTO","NOVE",
				"DIECI","UNDICI",
				"DODICI","TREDICI",
				"QUATTORDICI","QUINDICI",
				"SEDICI","DICIASSETTE",
				"DICIOTTO","DICIANNOVE"
                )[n-1])
        return a.lower()
    if n <= 99:
        decine = (
                  "VENTI","TRENTA","QUARANTA",
                  "CINQUANTA","SESSANTA","SETTANTA",
				      "OTTANTA","NOVANTA"
                 )
        Carattere = decine[int(n/10)-2]
        sel = n%10
        if sel == 1 or sel == 8:
            Carattere = Carattere[:-1]
        return Carattere.lower() + conv(n%10)
    if n <= 199:
        b=("CENTO")
        return b.lower() + conv(n%100)
    if n <= 999:
        m = n%100
        m = int(m/10)
        Carattere = "cent"
        if m!= 8:
            Carattere = Carattere + "o"
        return conv( int(n/100)) + Carattere + conv(n%100)
    if n <= 1999 :
        mi=("MILLE")
        return mi.lower() + conv(n%1000)
    if n <= 999999:
        mile=("MILA")
        return conv(int(n/1000))+ mile.lower()+conv(n%1000)
    if n <= 1999999:
        umln="UNMILIONE"
        return umln.lower()+conv(n%1000000)
    if n <= 999999999:
        mln="MILIONI"
        return conv(int(n/1000000))+mln.lower()+conv(n%1000000)
    if n <= 1999999999:
        umlrd="UNMILIARDO"
        return umlrd.lower()+conv(n%1000000000)
    if n <= 999999999999:
        mlrd="MILIARDI"
        return conv(int(n/1000000000))+mlrd.lower()+conv(n%1000000000)
    if n <= 1999999999999:
        unbmln="UNBILIONE"
        return unbmln.lower() + conv(n%1000000000000)
    else:
        biln="BILIONI"
        return conv(int(n/1000000000000))+biln.lower()+conv(n%1000000000000)