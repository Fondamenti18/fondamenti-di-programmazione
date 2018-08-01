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


def conv(n):
     if n == 0: 
        return ""
     elif n <= 19:
        return ("uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove")[n-1]
     elif n <= 99:
        d = ("venti", "trenta", "quaranta","cinquanta", "sessanta", "settanta", "ottanta", "novanta")
        div, mod = divmod(n, 10)
        let = d[int(div)-2]
        if mod == 1 or mod == 8:
            let = let[:-1]
        return let + conv(mod)
     elif n <= 199:
        div, mod = divmod(n, 100)
        return "cento" + conv(mod)
     elif n <= 999:
        div, mod = divmod(n, 100)
        mood = int(mod/10)
        let = "cent"
        if mood != 8:
            return conv(int(div)) + "cento" + conv(mod)
        return conv(int(div)) + let + conv(mod)
     elif n<= 1999 :
        div, mod = divmod(n, 1000)
        return "mille" + conv(mod)
     elif n<= 999999:
        div, mod = divmod(n, 1000)
        return conv(int(div)) + "mila" + conv(mod)
     elif n <= 1999999:
        div, mod = divmod(n, 1000000)
        return "unmilione" + conv(mod)
     elif n <= 999999999:
        div, mod = divmod(n, 1000000)
        return conv(int(div))+ "milioni" + conv(mod)
     elif n <= 1999999999:
        div, mod = divmod(n, 1000000000)
        return "unmiliardo" + conv(mod)
     else:
        div, mod = divmod(n, 1000000000)
        return conv(int(div)) + "miliardi" + conv(mod)
    
    
    
