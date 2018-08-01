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

lista = ["", 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
lista2 = ['venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta', 'cento']
lista3 = ['duecento', 'trecento', 'quattrocento', 'cinquecento', 'seicento', 'settecento', 'ottocento', 'novecento']
def conv(n):
    if n <= 19:
        return lista[n]
    if n == 21:
        return "ventuno"
    if n == 28:
        return "ventotto"
    if n == 31:
        return "trentuno"
    if n == 38:
        return "trentotto"
    if n == 41:
        return "quarantuno"
    if n == 48:
        return "quarantotto"
    if n == 51:
        return "cinquantuno"
    if n == 58:
        return "cinquantotto"
    if n == 61:
        return "sessantuno"
    if n == 68:
        return "sessantotto"
    if n == 71:
        return "settantuno"
    if n == 78:
        return "settantotto"
    if n == 81:
        return "ottantuno"
    if n == 88:
        return "ottantotto"
    if n == 91:
        return "novantuno"
    if n == 98:
        return "novantotto"
    if n <= 100:
        d = n // 10
        u = n % 10
        return lista2[d - 2] + lista[u]              
    if 100 < n < 180:
        c = n % 100
        d = n // 10
        u = n // 10
        return  "cento" + conv(c)
    elif 180 <= n < 190:
        c = n % 100
        d = n // 10
        u = n // 10
        return "cent" + conv(c)
    while 190 <= n < 200:
        c = n % 100
        d = n % 10
        u = n % 10
        return  "cento" + conv(c)
    
    if n < 1000:
        c = n // 100
        d = n % 100
        return lista[c] + "cento" + conv(d)
    if 1000 < n < 2000:
        m = n // 100
        c = n % 1000
        d = n % 1
        u = n % 10
        return "mille" + conv(c) + conv(d)

    if n < 1000000:
        c = n // 1000
        d = n % 1000
        u = n % 10
        return conv(c) + "mila" + conv(d)

    if 1000000000 > n:
        c = n // 1000000
        d = n % 1000000
        u = n % 1000
        return conv(c) + "milioni" + conv(d)
    elif 1000000 < n < 2000000:
        c = n % 1000000
        d = n // 1000000
        u = n // 1000
        return "unmilione" + conv(c) + conv(d)

    if n < 10 ** 12:
        c = n // 1000000000
        d = n % 1000000000
        u = n % 1000000
        return conv(c) + "miliardi" + conv(d)

    
        
    
