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

lista_u=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
lista_d=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
lista_d18=['vent','trent','quarant','cinquant','sessant','settant','ottant','novant']


def conv(n):
    if n<=19:
        return lista_u[n]
    elif n<=99:
        d=n//10
        u=n-(d*10)
        if u==1 or u==8:
            return lista_d18[d-2]+lista_u[u]
        else:
            return lista_d[d-2]+lista_u[u]
    elif n<=999:
        c1='cento'
        c2='cent'
        c=n//100
        d=(n-(c*100))//10
        if c==1:
            if d==8:
                return c2+conv(n-(c*100))
            else:
                return c1+conv(n-(c*100))
        else:
            if d==8:
                return lista_u[c]+c2+conv(n-(c*100))
            else:
                return lista_u[c]+c1+conv(n-(c*100))
    elif n<=999999:
        m1='mille'
        m2='mila'
        m=(n//1000)
        if m==1:
            return m1+conv(n-(m*1000))
        else:
            return conv(m)+m2+conv(n-(m*1000))
    elif n<=999999999:
        mn1='unmilione'
        mn2='milioni'
        mn=(n//1000000)
        if mn==1:
            return mn1+conv(n-(mn*1000000))
        else:
            return conv(mn)+mn2+conv(n-(mn*1000000))
    elif n<=999999999999:
        ml1='unmiliardo'
        ml2='miliardi'
        ml=(n//1000000000)
        if ml==1:
            return ml1+conv(n-(ml*1000000000))
        else:
            return conv(ml)+ml2+conv(n-(ml*1000000000))


print(conv(68258148238))