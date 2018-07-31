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
    stringa = ''
    n2 = n
    miliardi = n2 // 1000000000
    x = miliardi // 100
    y = (miliardi % 100) // 10
    z = (miliardi % 100) % 10
    n2 = n2 - miliardi*1000000000
    milioni = n2 // 1000000
    a = milioni // 100
    b = (milioni % 100) // 10
    c = (milioni % 100) % 10
    n2 = n2 - milioni*1000000
    migliaia = n2 // 1000
    d = migliaia // 100
    e = (migliaia % 100) // 10
    f = (migliaia % 100) % 10
    n2 = n2 - migliaia* 1000
    cent = n2 // 100
    n2 = n2 - cent*100
    dec = n2 // 10
    n2 = n2 - dec*10
    u = n2 
    u_lett = ['', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
    dec_lett = ['', '', 'venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta']
    cent_lett = ['', 'cento', 'duecento', 'trecento', 'quattrocento', 'cinquecento', 'seicento', 'settecento', 'ottocento', 'novecento']
    speciale = ['dieci','undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    if n == 0:
        stringa += 'zero'
    else:
        if miliardi != 0:
            if miliardi == 1:
                stringa += 'unmiliardo'
            elif miliardi == 1000:
                stringa += 'millemiliardi'
            elif miliardi >= 10 and miliardi < 20:
                stringa += speciale[miliardi % 10] + 'miliardi'
            else:
                if y == 1:
                    stringa += cent_lett[d] + speciale[z] + 'mila'
                elif y == 8:
                    if z == 1 or z == 8:
                        stringa += cent_lett[x][: -1] + dec_lett[y][: -1] + u_lett[z] + 'miliardi'
                    else:
                        stringa += cent_lett[x][: -1] + dec_lett[y] + u_lett[z] + 'miliardi'
                else: 
                    if z == 1 or z == 8:
                        stringa += cent_lett[x] + dec_lett[y][: -1] + u_lett[z] + 'miliardi'
                    else:
                        stringa += cent_lett[x] + dec_lett[y] + u_lett[z] + 'miliardi' 
                
        if milioni != 0:
            if milioni == 1:
                stringa += 'unmilione'
            elif milioni >= 10 and milioni < 20:
                stringa += speciale[milioni % 10] + 'milioni'
            else:
                if b == 1:
                    stringa += cent_lett[d] + speciale[c] + 'mila'
                elif b == 8:
                    if c == 1 or c == 8:
                        stringa += cent_lett[a][: -1] + dec_lett[b][: -1] + u_lett[c] + 'milioni'
                    else:
                        stringa += cent_lett[a][: -1] + dec_lett[b] + u_lett[c] + 'milioni'
                else: 
                    if c == 1 or c == 8:
                        stringa += cent_lett[a] + dec_lett[b][: -1] + u_lett[c] + 'milioni'
                    else:
                        stringa += cent_lett[a] + dec_lett[b] + u_lett[c] + 'milioni' 
        if migliaia != 0:
            if migliaia == 1:
                stringa += 'mille'
            elif migliaia >= 10 and migliaia < 20:
                stringa += speciale[migliaia % 10] + 'mila'
            else:
                if e == 1:
                    stringa += cent_lett[d] + speciale[f] + 'mila'
                elif e == 8:
                    if f == 1 or f == 8:
                        stringa += cent_lett[d][: -1] + dec_lett[e][: -1] + u_lett[f] + 'mila'
                    else:
                        stringa += cent_lett[d][: -1] + dec_lett[e] + u_lett[f] + 'mila'
                else:
                    if f == 1 or f == 8:
                        stringa += cent_lett[d] + dec_lett[e][: -1] + u_lett[f] + 'mila'
                    else:
                        stringa += cent_lett[d] + dec_lett[e] + u_lett[f] + 'mila'
        if dec == 8:
            if u == 1 or u == 8:
                stringa += cent_lett[cent][: -1] + dec_lett[dec][: -1] + u_lett[u] 
            else:
                stringa += cent_lett[cent][: -1] + dec_lett[dec] + u_lett[u]
        elif dec == 1:
            stringa += cent_lett[cent] + speciale[u]
        else:
            if u == 1 or u == 8:
                stringa += cent_lett[cent] + dec_lett[dec][: -1] + u_lett[u] 
            else:
                stringa += cent_lett[cent] + dec_lett[dec] + u_lett[u]
    return stringa