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
    a=''
    t=str(n)
    unita=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    decine=['','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    if n==0:
        return a
    elif 0<n<=19:
        a+=unita[n]
        return a
    elif 20<=n<=99:
        ln=n%10
        if ln==1 or ln==8:
            a+=decine[int(t[0])-1][:-1]+conv(n%10)
        else:
            a+=decine[int(t[0])-1]+conv(n%10)
        return a
    elif 100<=n<=199:
        ls=int(t[1])
        if ls==8:
            a+='cent'+conv(n%100)
        else:
            a+='cento'+conv(n%100)
        return a
    elif 200<=n<=999:
        ls=int(t[1])
        if ls==8:
            a+=conv(int(n/100))+'cent'+conv(n%100)
        else:
            a+=conv(int(n/100))+'cento'+conv(n%100)
        return a
    elif 1000<=n<=1999:
        a+='mille'+conv(n%1000)
        return a
    elif 2000<=n<=999999:
        a+=conv(int(n/1000))+'mila'+conv(n%1000)
        return a
    elif 1000000<=n<=1999999:
        a+='unmilione'+conv(n%1000000)
        return a
    elif 2000000<=n<=999999999:
        a+=conv(int(n/1000000))+'milioni'+conv(n%1000000)
        return a
    elif 1000000000<=n<=1999999999:
        a+='unmiliardo'+conv(n%1000000000)
        return a
    elif 2000000000<=n<=999999999999:
        a+=conv(int(n/1000000000))+'miliardi'+conv(n%1000000000)
        return a
        
        
