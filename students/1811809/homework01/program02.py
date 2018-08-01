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

def conv3Num(c, d, u):
    table = [["uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove"],
             ["dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"],
             ["venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]]
    ret = ''
    if c != 0:
        ret += ('' if c == 1 else table[0][c-1]) + "cento"
    if d == 1:
        ret += table[1][u]
    elif d == 0:
        ret += (table[0][u-1] if u > 0 else '')
    else:
        sd = (table[2][d-2] if (u != 1 and u != 8) else table[2][d-2][:-1])+(table[0][u-1] if u > 0 else '')
        ret += (sd[1:] if (d == 8 and c > 0) else sd)
    return ret

def conv(n):
    table = [['mille', 'mila'],
             ['unmilione', 'milioni'],
             ['unmiliardo', 'miliardi']]
    ind = -1
    answ = []
    while n != 0:
        u = n%10
        n //= 10
        d = n%10
        n //= 10
        c = n%10
        n //= 10
        ret = conv3Num(c, d, u)

        if ind == -1:
            answ.append(ret)
        elif u == 1 and d == 0 and c == 0:
            answ.append(table[ind][0])
        elif u > 1 or d > 0 or c > 0:
            answ.append(ret+table[ind][1])

        ind += 1

    answ.reverse()
    return ''.join(answ)
