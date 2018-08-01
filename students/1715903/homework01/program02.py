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
    ft=('uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove','dieci',
        'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette','diciotto', 'diciannove')
    de=('venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta')

    
    if n<100: return d(n,ft,de)
    elif n<1000: return h(n,ft) + conv(n%100)
    elif n<1000000: return t(n) + conv(n%1000)
    elif n<1000000000: return o(n) + conv(n%1000000)
    elif n<1000000000000: return m(n) + conv(n%1000000000)
    
def d(n,ft,de):
    if n==0: return ''
    if n<20:
        return ft[n-1]

    elif n<100:
        com = de[(n//10)-2]
        if n%10 == 1 or n%10 == 8:
            com=com[:-1]
        return com + conv(n%10)

def h(n,ft):
    st='cento'
    if (n%100)//10==8:
        st='cent'
    if n<200:
        com=st
    else:
        com=ft[(n//100)-1]+st
    return com

def t(n):
    if n<2000:
        com='mille'
    else:
        com=conv(n//1000)+'mila'
    return com

def o(n):
    if n<2000000:
        com='unmilione'
    else:
        com=conv(n//1000000)+'milioni'
    return com

def m(n):
    if n<2000000000:
        com='unmiliardo'
    else:
        com=conv(n//1000000000)+'miliardi'
    return com
