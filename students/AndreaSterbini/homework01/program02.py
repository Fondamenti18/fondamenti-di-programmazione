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
    elisioni = {
                 'unomiliardo'  : 'unmiliardo',
                 'unomilione'   : 'unmilione',
                 'unomille'     : 'mille',
                 'unocent'      : 'cent',
                }
    potenze = { 
            9   : 'miliardi',
            6   : 'milioni',
            3   : 'mila',
            0   : '' }
    potenza = { 
            9   : 'miliardo',
            6   : 'milione',
            3   : 'mille',
            0   : '' }
    res = ''
    for p in sorted(potenze.keys(), reverse=True):
        K = n // 10**p
        n %= 10**p
        if K==1:res += convertiMille(K) + potenza[p]
        elif K: res += convertiMille(K) + potenze[p]
    for k, v  in elisioni.items():
        res = res.replace(k,v)
    return res

def convertiMille(N):
    numeri = {  0:  '',
                1:  'uno',
                2:  'due',
                3:  'tre',
                4:  'quattro',
                5:  'cinque',
                6:  'sei',
                7:  'sette',
                8:  'otto',
                9:  'nove',
                10: 'dieci',
                11: 'undici',
                12: 'dodici',
                13: 'tredici',
                14: 'quattordici',
                15: 'quindici',
                16: 'sedici',
                17: 'diciassette',
                18: 'diciotto',
                19: 'diciannove',
                20: 'venti',
                30: 'trenta',
                40: 'quaranta',
                50: 'cinquanta',
                60: 'sessanta',
                70: 'settanta',
                80: 'ottanta',
                90: 'novanta',
                100: 'cento',
                }
    elisioni = { 'ottantau'     : 'ottantu',
                 'antao'        : 'anto',
                 'entao'        : 'ento',
                 'entio'        : 'ento',
                 'antau'        : 'antu',
                 'entau'        : 'entu',
                 'entiu'        : 'entu',
                 'centoottant'  : 'centottant',
                }
    res = ''
    C = N // 100
    N %= 100
    if C:   res += numeri[C] + 'cento'
    for d in sorted(numeri.keys(), reverse=True):
        if N >= d:
            res += numeri[d]
            N -= d
    for k, v  in elisioni.items():
        res = res.replace(k,v)
    return res

