''' In determinate occasioni ci capita di dover scrivere i numeri in lettere, 
ad esempio quando dobbiamo compilare un assegno. 
Puo' capitare che alcuni numeri facciano sorgere in noi qualche dubbio.

Le perplessita' nascono soprattutto nella scrittura dei numeri composti con 1 e 8. 
Tutti i numeri come venti, trenta, quaranta, cinquanta, ecc... elidono la vocale 
finale (la "i" per 20, la "a" per tutti gli altri) fondendola con la vocale
iniziale del numero successivo; scriveremo quindi ventuno, ventotto, trentotto, 
cinquantuno ecc...

Il numero cento, nella formazione dei numeri composti con uno e otto, non si
comporta 
cosi'; il numero "cento" e tutte le centinaia (duecento, trecento, ecc...),
infatti, non elidono la vocale finale. Dunque non scriveremo centuno,
trecentotto ma centouno, trecentootto,ecc...

I numeri composti dalle centinaia e dalla decina "ottanta" invece tornano
ad elidere 
la vocale finale; scriveremo quindi centottanta, duecentottanta,  ecc..., 
non centoottanta, duecentoottanta, ...

Il numero "mille" non elide in nessun numero composto la vocale finale;
scriveremo 
quindi milleuno,  milleotto, milleottanta, ecc...

Altri esempi sono elencati nel file grade02.txt


Scrivere una funzione conv(n) che prende in input un intero n,
con 0<n<1000000000000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio
dell'esercizio e' zero.
'''


def conv(n):
    'Scrivete qui il codice della funzione'
    l1=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove', \
        'dieci','undici','dodici','tredici','quattordici','quindici','sedici', \
        'diciassette','diciotto','diciannove']
    l2=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta' \
        ,'novanta']
    l3=['cento','mille','mila','unmilione','milioni','unmiliardo','miliardi']
    if n<20:
        return l1[n]
    elif n<100:
        dec=l2[n//10-2]
        un=n%10
        if un==1 or un==8:
            return dec[:-1]+conv(un)
        else:
            return dec+conv(un)
    elif n<200:
        dec=n%100
        return l3[0]+conv(dec)
    elif n<1000:
        cen=n//100
        dec=n%100
        dec1=n%100//10
        if dec1==8:
            return l1[cen]+l3[0][:-1]+conv(dec)
        else:
            return l1[cen]+l3[0]+conv(dec)
    elif n<2000:
        cen=n%1000
        return l3[1]+conv(cen)
    elif n<1000000:
        mil=n//1000
        rest=n%1000
        return conv(mil)+l3[2]+conv(rest)
    elif n<2000000:
        mil=n%1000000
        return l3[3]+conv(mil)
    elif n<1000000000:
        milio=n//1000000
        mila=n%1000000
        return conv(milio)+l3[4]+conv(mila)
    elif n<2000000000:
        milio=n%1000000000
        return l3[5]+conv(milio)
    elif n<1000000000000:
        milia=n//1000000000
        milio=n%1000000000
        return conv(milia)+l3[6]+conv(milio)
