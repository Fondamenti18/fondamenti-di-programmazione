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


def conv(d):
    '''La funzione restituisce un numero scritto in lettere'''
    if d==0: 
        return ''
    if d<20:
        return ('uno','due', 'tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette', 'diciotto', 'diciannove')[d-1]
    if d<=100:
        decine=('venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta')
        letter=decine[int(d/10)-2]
        t=d%10
        if t==1 or t==8:
            letter=letter[ :-1]
        return letter+conv(d%10)
    elif d<200:
        return 'cento'+conv(d%100)
    if d<=999:
        m=d%100
        m=int(m/10)
        letter ='cent'
        if m!=8:
            letter=letter+'o'
        return conv(int(d/100))+letter+conv(d%100)
    elif d<=2000:
        return 'mille'+conv(d%1000)
    if d<1000000:
        return conv(int(d/1000))+'mila'+conv(d%1000)
    elif d<=1000000000:
        return conv(int(d/1000000))+'milioni'+conv(d%1000000)
    if d<1000000000000:
        return conv(int(d/1000000000))+'miliardi'+conv(d%1000000000)
