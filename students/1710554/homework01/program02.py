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


l1 = ["","uno", "due", "tre", "quettro", "cinque", "sei", "sette", "otto", "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]
l2 = ["venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]
l3 = ["vent", "trent", "quarant", "cinquant", "sessant", "settant", "ottant", "novant"]

def conv(n):
    if n < 20:
        return l1[n]
    elif n < 100:
        decine = n // 10
        unita = n % 10
        if unita == 1 or unita == 8:
            return l3 [decine - 2] + l1[unita]
        else:
            return l2[decine - 2] + l1[unita]
    elif n < 200:
        decine = n % 100
        if 180 <= n < 190:
            return "cent" + conv(decine)
        else:
            return "cento" + conv(decine)
    elif n < 1000:
        centinaia = n // 100
        decine = n % 100
        if 80 <= decine < 90:
            return l1[centinaia] + "cent" + conv(decine)
        else:
            return l1[centinaia] + "cento" + conv(decine) 
    elif n < 2000:
        decine = n % 1000
        return "mille" + conv(decine)
    elif n < 1000000:
        centinaia = n // 1000
        decine = n % 1000
        return conv(centinaia) + "mila" + conv(decine)
    elif n < 2000000:
        decine = n % 1000000
        return "unmilione" + conv(decine)
    elif n < 1000000000:
        centinaia = n // 1000000
        decine = n % 1000000
        return conv(centinaia) + "milioni" + conv(decine)
    elif n < 2000000000:
        decine = n % 1000000000
        return "unmiliardo" + conv(decine)
    elif n < 1000000000000:
        centinaia = n // 1000000000
        decine = n % 1000000000
        return conv(centinaia) + "miliardi" + conv(decine)
    
