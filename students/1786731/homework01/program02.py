c1 = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove"]
c15 = ["dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]
c2 = ["", "dieci", "venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]
c3 = ["", "cento", "duecento", "trecento", "quattrocento", "cinquecento", "seicento", "settecento", "ottocento", "novecento"]
c4 = ["mille", "mila", "unmilione", "milioni", "unmiliardo", "miliardi"]
lookupc2, lookupc1 = [999,999,999,999,999,999,999,999,-1,999], [999,-1,999,999,999,999,999,999,-1,999]

def convertigruppi(gruppidatre):
    for i, g in enumerate(gruppidatre):
        gint = int(g)
        conversionegruppo = ''
        primacifra, secondacifra, terzacifra = gint % 10, (gint // 10) % 10, (gint // 100)

        if gint == 0: # i gruppi con '000' vengono skippati:
            gruppidatre[i] = 0
            continue

        conversionegruppo += c3[terzacifra][0:lookupc2[secondacifra]] # appende centinaia - slice syntax lookup previene if statements

        if secondacifra == 1: # appende decine e unita'
            conversionegruppo += c15[primacifra]
        else:
            conversionegruppo += c2[secondacifra][0:lookupc1[primacifra]]
            conversionegruppo += c1[primacifra]
        
        gruppidatre[i] = conversionegruppo
    
    return gruppidatre

def getgruppidatre(cifre, stringa):
    gruppidatre = [ stringa[i:i+3][::-1] for i in range(0, cifre, 3) ]
    return convertigruppi(gruppidatre)

def appendiNotazioneNumeriGrandi(i, g, n, conversione):
    if g == 0:
        return
    if ((n // 10**(3 * (i+1))) % 1000) == 1:
        conversione = c4[i*2 + 0] + conversione
    else:
        conversione = g + c4[i*2 + 1] + conversione
    return conversione

def conv(n):
    stringa = str(n)[::-1] # extended slice syntax - fa il reverse della stringa
    cifre = len(stringa)
    conversione = ''

    gruppidatre = getgruppidatre(cifre, stringa)

    # fuori dal primo ciclo - concatenamento per i numeri molto grandi
    conversione = gruppidatre[0] or ''    
    for i, g in enumerate(gruppidatre[1:]):
        conversione = appendiNotazioneNumeriGrandi(i, g, n, conversione)

    return conversione