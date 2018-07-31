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
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

literal_numbers = {"1": "uno", "2": "due", "3": "tre", "4": "quattro", "5": "cinque", "6": "sei", "7": "sette", "8": "otto", "9": "nove", "10": "dieci", "11": "undici", "12": "dodici", "13": "tredici", "14": "quattordici", "15": "quindici", "16": "sedici", "17": "diciassette", "18": "diciotto", "19": "diciannove", "20": "venti", "30": "trenta", "40": "quaranta", "50": "cinquanta", "60": "sessanta", "70": "settanta", "80": "ottanta", "90": "novanta", "100": "cento", "1000": "mille", "10x3": "mila", "10x6": "milioni", "10x9": "miliardi"}

def decine(n):
    if n[0] == "1":
        return literal_numbers[n]
    elif n[1] == "0":
        return literal_numbers[n]
    elif n[1] == "1" or n[1] == "8":
        return literal_numbers[str(int(n[0])*10)][:-1] + literal_numbers[n[1]]
    else:
        return literal_numbers[str(int(n[0])*10)] + literal_numbers[n[1]]

def centinaia(n):
    n2 = n[-2:].lstrip("0")
    cond = 0
    if n2[0] == "8" and len(n2) == 2:
        cond = 1
    if len(n2) == 1:
        n2 = literal_numbers[n2]
    elif len(n2) == 2 and n2 != "":
        n2 = decine(n2)
    if n[0] != "1":
        if cond == 1:
            return literal_numbers[n[0]] + literal_numbers["100"][:-1] + n2
        else:
            return literal_numbers[n[0]] + literal_numbers["100"] + n2
    else:
        if cond == 1:
            return literal_numbers["100"][:-1] + n2
        else:
            return literal_numbers["100"] + n2

def migliaia(n):
    n1 = n[:-3]
    n2 = n[-3:].lstrip("0")
    if len(n2) == 1:
        n2 = literal_numbers[n2]
    elif len(n2) == 2:
        n2 = decine(n2)
    else:
        n2 = centinaia(n2)
    if len(n1) == 1:
        if n1 != "1":
            return literal_numbers[n1] + literal_numbers["10x3"] + n2
        else:
            return literal_numbers["1000"] + n2
    elif len(n1) == 2:
        return decine(n1) + literal_numbers["10x3"] + n2
    else:
        return centinaia(n1) + literal_numbers["10x3"] + n2

def milioni(n):
    n1 = n[:-6]
    n2 = n[-6:].lstrip("0")
    if len(n2) == 1:
        n2 = literal_numbers[n2]
    elif len(n2) == 2:
        n2 = decine(n2)
    elif len(n2) == 3:
        n2 = centinaia(n2)
    elif 3<len(n2)<7:
        n2 = migliaia(n2)
    if len(n1) == 1:
        if n1 != "1":
            return literal_numbers[n1] + literal_numbers["10x6"] + n2
        else:
            return "un" + literal_numbers["10x6"][:-1] + "e" + n2
    elif len(n1) == 2:
        return decine(n1) + literal_numbers["10x6"] + n2
    elif len(n1) == 3:
        return centinaia(n1) + literal_numbers["10x6"] + n2

def miliardi(n):
    n1 = n[:-9]
    n2 = n[-9:].lstrip("0")
    if len(n2) == 1:
        n2 = literal_numbers[n2]
    elif len(n2) == 2:
        n2 = decine(n2)
    elif len(n2) == 3:
        n2 = centinaia(n2)
    elif 3<len(n2)<7:
        n2 = migliaia(n2)
    elif 6<len(n2)<10:
        n2 = milioni(n2)
    if len(n1) == 1:
        if n1 != "1":
            return literal_numbers[n1] + literal_numbers["10x9"] + n2
        else:
            return "un" + literal_numbers["10x9"][:-1] + "o" + n2
    elif len(n1) == 2:
        return decine(n1) + literal_numbers["10x9"] + n2
    elif len(n1) == 3:
        return centinaia(n1) + literal_numbers["10x9"] + n2

def conv(n):
    if 0<n<10**12:
        n = str(n)
        l = len(n)
        if l == 1:
            return literal_numbers[n]
        elif l == 2:
            return decine(n)
        elif l == 3:
            return centinaia(n)
        elif 3<l<7:
            return migliaia(n)
        elif 6<l<10:
            return milioni(n)
        elif 9<l<13:
            return miliardi(n)
    else:
        return "Invalid Number"
