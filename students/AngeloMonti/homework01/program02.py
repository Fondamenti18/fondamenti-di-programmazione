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

'''


def conv(n):
    'Scrivete qui il codice della funzione'
    s=''
    a=n//1000000000
    n=n%1000000000
    b=n//1000000
    n=n%1000000
    c=n//1000
    d=n%1000
    if a>0:
        if a==1: s=s+'unmiliardo'
        else:
            s=s+conv1(a)+'miliardi'
    if b>0:
        if b==1: s=s+'unmilione'
        else:
            s=s+conv1(b)+'milioni'
    if c>0:
        if c==1: s=s+'mille'
        else:
            s=s+conv1(c)+'mila'
    if d>0:
        s=s+conv1(d)
    return s




def conv1(n):
    '''dato l'intero n, con 0<n<1000, lo restituisce espresso in lettere'''
    U=['zero', 'uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    P=['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    D=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    s=''
    a=n//100
    n=n%100
    b=n//10
    c=n%10
    if a>0:
        if a>1: s=s+U[a]
        s=s+'cento'
        if b==8: s=s[:-1]
    if b==1 : 
        s+=P[c]
    else:
        if b> 1:
            s+=D[b-2]
            if c==1 or c==8 : s=s[:-1]
        if c>0 : s=s+U[c]
    return s

