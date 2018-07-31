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
    'Scrivete qui il codice della funzione'
    n=int(n)
    if 0 < n < 1000000000000: string = miliardi(n)
    string = string.split(" ")
    string = "".join(string)
    return string


def unita(n, string=""):
    if int(n) == 1: string = string[:(len(string)-1)] + "uno"
    elif int(n) == 2: string = string + "due"
    elif int(n) == 3: string = string + "tre"
    elif int(n) == 4: string = string + "quattro"
    elif int(n) == 5: string = string + "cinque"
    elif int(n) == 6: string = string + "sei"
    elif int(n) == 7: string = string + "sette"
    elif int(n) == 8: string = string[:(len(string)-1)] + "otto"
    elif int(n) == 9: string = string + "nove"
    elif int(n) == 0: string = string + " "
    return string

def decinespeciali(n, string=""):
    if int(n) == 10: string = string + "dieci"
    elif int(n) == 11: string = string + "undici"
    elif int(n) == 12: string = string + "dodici"
    elif int(n) == 13: string = string + "tredici"
    elif int(n) == 14: string = string + "quattordici"
    elif int(n) == 15: string = string + "quindici"
    elif int(n) == 16: string = string + "sedici"
    elif int(n) == 17: string = string + "diciassette"
    elif int(n) == 18: string = string + "diciotto"
    elif int(n) == 19: string = string + "diciannove"
    return string
    
    
def decine(n, string=""):
    if 10 <= int(n) <= 19: string = decinespeciali(n,string)
    elif 20 <= int(n) <= 29:
        string = unita(n%10,string + "venti")
    elif 30 <= int(n) <= 39:
        string = unita(n%10,string + "trenta")
    elif 40 <= int(n) <= 49:
        string = unita(n%10,string + "quaranta")
    elif 50 <= int(n) <= 59:
        string = unita(n%10,string + "cinquanta")
    elif 60 <= int(n) <= 69:
        string = unita(n%10,string + "sessanta")
    elif 70 <= int(n) <= 79:
        string = unita(n%10,string + "settanta")
    elif 80 <= int(n) <= 89:
        if string[(len(string)-2):] == "o ": string = string[:(len(string)-2)]
        elif string[(len(string)-1):] == "o": string = string[:(len(string)-1)]
        string = unita(n%10,string + "ottanta")
    elif 90 <= int(n) <= 99:
        string = unita(n%10,string + "novanta")
    else: string = unita(n%10,string)
    return string
        

def centinaia(n, string=""):
    if 100 <= int(n) <=199:
        string = decine(n%100,string+"cento ")
    elif 200 <= int(n) <=999:
        string = decine(n%100,unita(n//100,string) + "cento ")
    else: string = decine(n%100,string)
    return string


def migliaia(n, string=""):
    if 1000 <= int(n) <=1999:
        string = centinaia(n%1000,string+"mille ")
    elif 2000 <= int(n) <=999999:
        string = centinaia(n%1000,centinaia(n//1000,string) + "mila ")
    else: string = centinaia(n%1000,string)
    return string


def milioni(n, string=""):
    if 1000000 <= int(n) <=1999999:
        string = migliaia(n%1000000,string+"unmilione ")
    elif 2000000 <= int(n) <=999999999:
        string = migliaia(n%1000000,centinaia(n//1000000,string) + "milioni ")
    else: string = migliaia(n%1000000,string)
    return string

    
def miliardi(n, string=""):
    if 1000000000 <= int(n) <=1999999999:
        string = milioni(n%1000000000,string+"unmiliardo ")
    elif 2000000000 <= int(n) <=999999999999:
        string = milioni(n%1000000000,centinaia(n//1000000000,string) + "miliardi ")
    else: string = milioni(n%1000000000,string)
    return string