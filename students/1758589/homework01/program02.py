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
    diz_num = {0:'', 1: 'uno', 2: 'due', 3: 'tre', 4: 'quattro', 5: 'cinque', 6: 'sei', 7: 'sette', 8: 'otto', 9: 'nove', 10: 'dieci', 11: 'undici', 12: 'dodici',
                13: 'tredici', 14: 'quattordici', 15: 'quindici', 16: 'sedici', 17: 'diciassette', 18: 'diciotto', 19: 'diciannove'}
    lis_dec = ['venti','trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta']

    if 0 <= n <= 19:
        return diz_num[n]

    elif 20 <= n <= 99:
        decine1 = lis_dec[(n // 10) - 2]
        u = n % 10
        if u == 1 or u == 8:
            decine1 = decine1[:-1]
        return decine1 + diz_num[n % 10]

    elif n <= 199:
        return 'cento' + conv(n % 100)

    elif n <= 999:
        decine2 = n % 100
        decine2 = decine2 // 10
        centinaia = 'cent'
        if decine2 != 8:
            centinaia = centinaia + 'o'
        return diz_num[n // 100] + centinaia + conv(n % 100)

    elif n <= 1999:
        return 'mille' + conv(n % 1000)

    elif n <= 999999:
        return conv(n // 1000) + 'mila' + conv(n % 1000)

    elif n <= 1999999:
        return 'unmilione' + conv(n % 1000000)

    elif n <= 999999999:
        return conv(n // 1000000) + 'milioni' + conv(n % 1000000)

    elif n < 1999999999:
        return 'unmiliardo' + conv(n % 1000000000)

    else:
        return conv(n // 1000000000) + 'miliardi' + conv(n % 1000000000)
