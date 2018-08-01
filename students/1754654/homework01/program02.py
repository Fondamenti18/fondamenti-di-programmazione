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
    s_n = str(n)
    f_value = ''

    if 9 < len(s_n) <= 12:
        bl_app = s_n[:-9]
        if int(bl_app) == 1:
            f_value = f_value + 'unmiliardo'
        else:
            f_value = f_value + letter_quantity(int(bl_app)) + 'miliardi'
        s_n = s_n[-9:]

    if 6 < len(s_n) <= 9:
        ml_app = s_n[:-6]
        if int(ml_app) == 1:
            f_value = f_value + 'unmilione'
        else:
            f_value = f_value + letter_quantity(int(ml_app)) + 'milioni'
        s_n = s_n[-6:]


    if 3 < len(s_n) <= 6:
        th_app = s_n[:-3]
        if int(th_app) == 1:
            f_value = f_value + 'mille'
        else:
            f_value = f_value + letter_quantity(int(th_app)) + 'mila'
        s_n = s_n[-3:]


    if 0 < len(s_n) <= 3:
        f_value = f_value + letter_quantity(int(s_n))

    return f_value

def letter_quantity(number):
    unita = ['','uno','due','tre','quattro','cinque','sei','sette','otto','nove',]
    decine_2 = ['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    decine = ['','dieci','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    centinaia = ['cento']

    r_value = ''
    i_value = int(number)

    if 0 < i_value <= 9:
        r_value = unita[i_value]

    if 9 < i_value <= 99:
        if i_value <= 19:
            d_app = str(i_value)
            r_value = r_value + decine_2[int(d_app[1])]
        else:
            c_app = str(i_value)
            if c_app[1] == '1' or c_app[1] == '8':
                r_value = r_value + decine[int(c_app[0])][:-1] + unita[int(c_app[1])]

            else:
                r_value = r_value + decine[int(c_app[0])] + unita[int(c_app[1])]

    if 99 < i_value <= 999:
        h_app = str(i_value)
        if h_app[0] == '1':
            r_value = centinaia[0] + letter_quantity(h_app[-2:])
        else:
            if h_app[1] == '8':
                r_value = unita[int(h_app[0])] + centinaia[0][:-1] + letter_quantity(h_app[-2:])
            else:
                r_value = unita[int(h_app[0])] + centinaia[0] + letter_quantity(h_app[-2:])

    return r_value
