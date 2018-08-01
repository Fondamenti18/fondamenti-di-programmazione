''' In determinate occasioni ci capita di dover scrivere i numeri in lettere, 
ad esempio quando dobbiamo compilare un assegno. 
Puo' capitare che alcuni numeri facciano sorgere in noi qualche dubbio.

Le perplessita' nascono soprattutto nella scrittura dei numeri composti con 1 e 8. 
Tutti i numeri come venti, trenta, quaranta, cinquanta, ecc... elidono la vocale 
finale (la "i" per 20, la "a" per tutti gli altri) fondendola con la vocale iniziale 
del numero successivo; scriveremo quindi ventuno, ventotto, trentotto, 
cinquantuno ecc...

Il numero cento, nella formazione dei numeri composti con uno e otto, non si comporta 
cosi'; il numero "cento" e tutte le centinaia (duecento, trecento, ecc...), 
infatti, non elidono la vocale finale. Dunque non scriveremo centuno,  trecentotto ma centouno, 
trecentootto, ecc...

I numeri composti dalle centinaia e dalla decina "ottanta" invece tornano ad elidere 
la vocale finale; scriveremo quindi centottanta, duecentottanta,  ecc..., 
non centoottanta, duecentoottanta, ...

Il numero "mille" non elide in nessun numero composto la vocale finale; scriveremo 
quindi milleuno,  milleotto, milleottanta, ecc...

Altri esempi sono elencati nel file grade02.txt


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1000000000000, 
e restituisce in output una stringa con il numero espresso in lettere   999999999999

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''
def conv(n):
    'Scrivete qui il codice della funzione'
    unita = ("uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove","dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove")
    decine = ("venti", "trenta", "quaranta","cinquanta", "sessanta", "settanta", "ottanta", "novanta")
    centinaia = ("cento","duecento","trecento","quattrocento","cinquecento","seicento","settecento","ottocento","novecento")
    migliaia = ("mille","duemila","tremila","quattromila","cinquemila","seimila","settemila","ottomila","novemila","diecimila", "undicimila", "dodicimila", "tredicimila", "quattordicimila", "quindicimila", "sedicimila", "diciassettemila", "diciottomila"\
                , "diciannovemila")
    milione = ("unmilione", "duemilioni", "tremilioni", "quattromilioni", "cinquemilioni", "seimilioni", "settemilioni", "ottomilioni", "novemilioni","diecimilioni", "undicimilioni", "dodicimilioni", "tredicimilioni", "quattordicimilioni", "quindicimilioni"\
               , "sedicimilioni", "diciassettemilioni", "diciottomilioni", "diciannovemilioni")
    miliardi = ("unmiliardo", "duemiliardi", "tremiliardi", "quattomiliardi", "cinquemiliardi", "seimiliardi", "settemiliardi", "ottomiliardi", "novemiliardi","diecimiliardi", "undicimiliardi", "dodicimiliardi"\
             , "tredicimiliardi", "quattordicimiliardi", "quindicimiliardi", "sedicimiliardi", "diciassettemiliardi", "diciottomiliardi", "diciannovemiliardi")
    valoreI2 = ''
    valoreI1 = ''
    valoreI = ''
    valoreM2 = ''
    valoreM1 = ''
    valoreM = ''
    valorem2 = ''
    valorem1 = ''
    valorem = ''
    valoreu = ''
    valored = ''
    valorec = ''
    I = 0
    I1 = 0
    I2 = 0
    d = 0
    c = 0
    m = 0
    m1 = 0
    m2 = 0
    M = 0
    M1 = 0
    M2 = 0
    z1 = 0
    z2 = 0
    z3 = 0
    if 0 < n < 20:
        n = str(n)
        u = int(n)
        z = int(n)
    elif 100 > n >= 20:
        n = str(n)
        u = int(n[1])
        d = int(n[0])
        z = int(str(n[1]) + str(n[0]))
    elif 1000 > n >= 100:
        n = str(n)
        u = int(n[2])
        d = int(n[1])
        c = int(n[0])
        z = int(str(n[1]) + str(n[2]))
    elif 10000 > n >= 1000:
        n = str(n)
        u = int(n[3])
        d = int(n[2])
        c = int(n[1])
        m = int(n[0])
        z = int(str(n[2]) + str(n[3]))
    elif 100000 > n >= 10000:
        n = str(n)
        u = int(n[4])
        d = int(n[3])
        c = int(n[2])
        m = int(n[1])
        m1 = int(n[0])
        z = int(str(n[3]) + str(n[4]))
        z1 = int(str(n[0]) + str(n[1]))
    elif 1000000 > n >= 100000:
        n = str(n)
        u = int(n[5])
        d = int(n[4])
        c = int(n[3])
        m = int(n[2])
        m1 = int(n[1])
        m2 = int(n[0])
        z = int(str(n[4]) + str(n[5]))
        z1 = int(str(n[1]) + str(n[2]))
    elif 10000000 > n >= 1000000:
        n = str(n)
        u = int(n[6])
        d = int(n[5])
        c = int(n[4])
        m = int(n[3])
        m1 = int(n[2])
        m2 = int(n[1])
        M = int(n[0])
        z = int(str(n[5]) + str(n[6]))
        z1 = int(str(n[2]) + str(n[3]))
    elif 100000000 > n >= 10000000:
        n = str(n)
        u = int(n[7])
        d = int(n[6])
        c = int(n[5])
        m = int(n[4])
        m1 = int(n[3])
        m2 = int(n[2])
        M = int(n[1])
        M1 = int(n[0])
        z = int(str(n[6]) + str(n[7]))
        z1 = int(str(n[3]) + str(n[4]))
        z2 = int(str(n[0]) + str(n[1]))
    elif 1000000000 > n >= 100000000:
        n = str(n)
        u = int(n[8])
        d = int(n[7])
        c = int(n[6])
        m = int(n[5])
        m1 = int(n[4])
        m2 = int(n[3])
        M = int(n[2])
        M1 = int(n[1])
        M2 = int(n[0])
        z = int(str(n[7]) + str(n[8]))
        z1 = int(str(n[4]) + str(n[5]))
        z2 = int(str(n[1]) + str(n[2]))
    elif 10000000000 > n >= 1000000000:
        n = str(n)
        u = int(n[9])
        d = int(n[8])
        c = int(n[7])
        m = int(n[6])
        m1 = int(n[5])
        m2 = int(n[4])
        M = int(n[3])
        M1 = int(n[2])
        M2 = int(n[1])
        I = int(n[0])
        z = int(str(n[8]) + str(n[9]))
        z1 = int(str(n[5]) + str(n[6]))
        z2 = int(str(n[2]) + str(n[3]))
    elif 100000000000 > n >= 10000000000:
        n = str(n)
        u = int(n[10])
        d = int(n[9])
        c = int(n[8])
        m = int(n[7])
        m1 = int(n[6])
        m2 = int(n[5])
        M = int(n[4])
        M1 = int(n[3])
        M2 = int(n[2])
        I = int(n[1])
        I1 = int(n[0])
        z = int(str(n[9]) + str(n[10]))
        z1 = int(str(n[6]) + str(n[7]))
        z2 = int(str(n[3]) + str(n[4]))
        z3 = int(str(n[0]) + str(n[1]))
    elif 1000000000000 > n >= 100000000000:
        n = str(n)
        u = int(n[11])
        d = int(n[10])
        c = int(n[9])
        m = int(n[8])
        m1 = int(n[7])
        m2 = int(n[6])
        M = int(n[5])
        M1 = int(n[4])
        M2 = int(n[3])
        I = int(n[2])
        I1 = int(n[1])
        I2 = int(n[0])
        z = int(str(n[10]) + str(n[11]))
        z1 = int(str(n[7]) + str(n[8]))
        z2 = int(str(n[4]) + str(n[5]))
        z3 = int(str(n[1]) + str(n[2]))
    elif n == 0:
        return 'zero'
    if 0 < u < 10:
        valoreu = unita[u-1] 
    if 9 < z <= 19:
        valoreu = unita[z-1]
    if d > 1:
        if u == 8 or u == 1:
            valored = decine[d-2]
            valored = valored[:-1]
        else:
            valored = decine[d-2]
    if c > 0:
        if d == 8:
            valorec = centinaia[c-1]
            valorec = valorec[:-1]
        else:
           valorec = centinaia[c-1]
    if m > 0:
        valorem = migliaia[m-1]
    if m1 > 1:
        if m == 0:
            valorem1 = decine[m1-2] + 'mila'
        elif m == 8:
            valorem1 = decine[m1-2]
            valorem1 = valorem1[:-1]
        elif m == 1:
            valorem1 = decine[m1-2]
            valorem1 = valorem1[:-1]
            valorem = 'unomila'
        else:
            valorem1 = decine[m1-2]
    if 9 < z1 <= 19:
        valorem = migliaia[z1-1]
    if m2 > 0:
         if m1 == 0 and m == 0:
            valorem2 = centinaia[m2-1] + 'mila'
         elif m1 == 8:
             valorem2 = centinaia[m2-1]
             valorem2 = valorem2[:-1]
         else:
             valorem2 = centinaia[m2-1]
         if m == 1:
             valorem = 'unomila'
    if M > 0:
        valoreM = milione[M-1]
    if M1 > 1:
        if M == 0:
            valoreM1 = decine[M1-2] + 'milioni'
        elif M == 8:
            valoreM1 = decine[M1-2]
            valoreM1 = valoreM1[:-1]
        elif M == 1:
            valoreM1 = decine[M1-2]
            valoreM1 = valoreM1[:-1]
            valoreM = 'unomilioni'
        else:
            valoreM1 = decine[M1-2]
    if 9 < z2 <= 19:
        valoreM = milione[z2-1]
    if M2 > 0:
         if M1 == 0 and M == 0:
            valoreM2 = centinaia[M2-1] + 'milioni'
         elif M1 == 8:
             valoreM2 = centinaia[M2-1]
             valoreM2 = valoreM2[:-1]
         else:
             valoreM2 = centinaia[M2-1]
         if M == 1:
             valoreM = 'unomilioni'
    if I > 0:
        valoreI = miliardi[I-1]
    if I1 > 1:
        if I == 0:
            valoreI1 = decine[I1-2] + 'miliardi'
        elif I == 8:
            valoreI1 = decine[I1-2]
            valoreI1 = valoreI1[:-1]
        elif I == 1:
            valoreI1 = decine[I1-2]
            valoreI1 = valoreI1[:-1]
            valoreI = 'unomiliardi'
        else:
            valoreI1 = decine[I1-2]
    if 9 < z3 <= 19:
        valoreI = miliardi[z3-1]
    if I2 > 0:
         if I1 == 0 and I == 0:
            valoreI2 = centinaia[I2-1] + 'miliardi'
         elif I1 == 8:
             valoreI2 = centinaia[I2-1]
             valoreI2 = valoreI2[:-1]
         else:
             valoreI2 = centinaia[I2-1]
         if I == 1:
             valoreI = 'unomiliardi'
    
    return (valoreI2 + valoreI1 + valoreI + valoreM2 + valoreM1 + valoreM + valorem2 + valorem1 + valorem + valorec + valored + valoreu)
