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
    unita = ['uno', 'due', 'tre', 'quattro', 'cinque', \
             'sei', 'sette', 'otto', 'nove']
    speciali = ['undici', 'dodici', 'tredici', 'quattordici', 'quindici', \
                'sedici', 'diciassette', 'diciotto', 'diciannove']
    decine = ['dieci', 'venti', 'trenta', 'quaranta', 'cinquanta', \
              'sessanta', 'settanta', 'ottanta', 'novanta']
    if 0 < n <= 9:
        c = 0
        while c != n:
            c = c + 1
        n = unita[c - 1]    
    elif 10 <= n <= 99:
        stringa = str(n)
        if stringa[1] == '0':
            c = 0
            while c != int(stringa[0]):
                c = c + 1
            n = decine[c - 1]
        elif 11 <= n <= 19:
            c = 0
            while c != n:
                c = c + 1
            n = speciali[c - 11]
        else:
            d = 0
            u = 0
            c = 0
            while c != int(stringa[0]):
                c = c + 1
            d = c
            c = 0
            while c != int(stringa[1]):
                c = c + 1
            u = c
            if stringa[-1] == '1' or stringa[-1] == '8':
                decine[d - 1] = decine[d - 1][: -1]                
            n = decine[d - 1] + unita[u - 1]            
    return n

