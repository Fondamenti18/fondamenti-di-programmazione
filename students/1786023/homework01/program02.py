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
    
    k = 1000 
    k2=2000
    m = k * k #1,000,000
    m2 = k2 * k #2,000,000
    b = m * k #1,000,000,000
    b2 = m * k2 #2,000,000,000
    t = b * k #1,000,000,000,000
    if n == 0:
        return ""

    if (n < 20):
        return ("uno", "due", "tre", "quattro", "cinque",
                "sei", "sette", "otto", "nove", "dieci",
                "undici", "dodici", "tredici",
                "quattordici", "quindici", "sedici",
                "diciassette", "diciotto", "diciannove")[n-1]

    if (n < 100):
        tens = ("venti", "trenta", "quaranta",
                  "cinquanta", "sessanta",
                  "settanta", "ottanta", "novanta")
        parola = tens[int(n/10)-2]
        unit = n%10
        if unit == 1 or unit == 8:
            parola = parola[:-1]
        return parola + conv(n%10)
    
    if (n < 200):
        return "cento" + conv(n%100)

    if (n < k):
        d = n%100
        d = int(d/10)
        parola = "cent"
        if d!= 8:
            parola = parola + "o"
        return conv(int(n/100)) + parola + conv(n % 100)
    
    if (n < k2):
        return "mille" + conv(n%k)

    if (n < m):
        return conv(int(n/k)) + "mila" + conv(n%k)

    if (n < m2):
        return "unmilione" + conv(n%m)

    if (n < b):
        return conv(int(n/m)) + "milioni" + conv(n%m)
    if (n < b2):
        return "unmiliardo" + conv(n%b)

    else:
        return conv(int(n/b)) + "miliardi" + conv(n%b)        
               
