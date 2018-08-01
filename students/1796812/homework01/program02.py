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
    lett = ''
    if n//10**9 != 0:
        lett += miliardi(n//10**9)
        n %= 10**9
    if n//10**6 != 0:
        lett += milioni(n//10**6)
        n %= 10**6
    if n//10**3 != 0:
        lett += migliaia(n//10**3)
        n %= 10**3
    lett += centinaia(n)
    return lett

def unita(n):
    if n == 0: return ''
    elif n == 1: return 'uno'
    elif n == 2: return 'due'
    elif n == 3: return 'tre'
    elif n == 4: return 'quattro'
    elif n == 5: return 'cinque'
    elif n == 6: return 'sei'
    elif n == 7: return 'sette'
    elif n == 8: return 'otto'
    elif n == 9: return 'nove'

def num_speciali(n):
    if n == 10: return 'dieci'
    elif n == 11: return 'undici'
    elif n == 12: return 'dodici'
    elif n == 13: return 'tredici'
    elif n == 14: return 'quattordici'
    elif n == 15: return 'quindici'
    elif n == 16: return 'sedici'
    elif n == 17: return 'diciassette'
    elif n == 18: return 'diciotto'
    elif n == 19: return 'diciannove'

def decine(n):
    lett = ''
    if n//10 == 0:
        return unita(n)
    elif n//10 == 1:
        return num_speciali(n)
    elif n//10 == 2:
        lett += 'venti'
    elif n//10 == 3:
        lett += 'trenta'
    elif n//10 == 4:
        lett += 'quaranta'
    elif n//10 == 5:
        lett += 'cinquanta'
    elif n//10 == 6:
        lett += 'sessanta'
    elif n//10 == 7:
        lett += 'settanta'
    elif n//10 == 8:
        lett += 'ottanta'
    elif n//10 == 9:
        lett += 'novanta'
    if n%10 == 1 or n%10 == 8:
        lett += ' '
        lett = lett.replace(lett[-2]+' ', '')
    return lett + unita(n%10)

def centinaia(n):
    lett = ''
    if n//100 == 0:
        return decine(n)
    elif n//100 == 1:
        lett += 'cento'
    elif n//100 != 0:
        lett += unita(n//100) + 'cento'
    if n%100 >80 and n%100 <89:
        lett += ' '
        lett = lett.replace(lett[-2]+' ', '')
    return lett + decine(n%100)



def migliaia(n):
    if n == 1: return 'mille'
    else: return centinaia(n) + 'mila'

def milioni(n):
    if n == 1: return 'unmilione'
    else: return centinaia(n) + 'milioni'

def miliardi(n):
    if n == 1: return 'unmiliardo'
    else: return centinaia(n) + 'miliardi'
