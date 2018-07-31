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


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1'000'000'000'000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


toDecine=["uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci", 
                "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]
def conv(n):
    if n <= 0:
        return ""
    elif n <= 999:
        return UTCifre(n)
    elif n <= 999999:
        return QSCifre(n)
    elif n <= 999999999:
        return SNCifre(n)
    elif n <= 999999999999:
        return NDCifre(n)
    else:
        return ""


def UTCifre(n):
    toCentinaia=["venti", "trenta", "quaranta","cinquanta", "sessanta", "settanta", "ottanta", "novanta"] 
    if n <= 19:   
        return toDecine[n-1]
    elif n <= 99:
        if n%10 == 1 or n%10 == 8:
            return toCentinaia[n//10-2][:-1] + conv(n%10)   
        else:
            return toCentinaia[n//10-2] + conv(n%10) 
    elif n <= 199:
         #if per elisione del cento (caso = "ottanta...")
        if ((n%100)//10) == 8:     
            return 'cento'[:-1] + conv(n%100)
        else:
            return 'cento' + conv(n%100)
    else:
        #if per elisione del cento (caso = "ottanta...", n > 199)
        if (n%100)//10 == 8:        
            return toDecine[(n//100)-1] + 'cento'[:-1] + conv(n%100) 
        else:
            return toDecine[(n//100)-1] + 'cento' + conv(n%100)


def QSCifre(n):
    if n <=1999:
            return 'mille'+ UTCifre(n%1000)
    else:
        return UTCifre(n//1000) + 'mila' + UTCifre(n%1000)



def SNCifre(n):
    if n <= 1999999:
        return 'unmilione'+ QSCifre(n%1000000)
    else:
         return UTCifre(n//1000000) +'milioni'+ QSCifre(n%1000000)


def NDCifre(n):
    if n <= 1999999999 :
        return 'unmiliardo'+ SNCifre(n%1000000000)
    else:
        return UTCifre(n//1000000000) +'miliardi' + SNCifre(n%1000000000) 

