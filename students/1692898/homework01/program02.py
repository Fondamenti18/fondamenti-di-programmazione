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
    NumeroAParole=""
    unita=["uno","due","tre","quattro","cinque","sei","sette","otto","nove"]
    decine=["dieci","venti","trenta","quaranta","cinquanta","sessanta","settanta","ottanta","novanta"]
    if n>=1000000000000 or n<=0:
        return 'numero troppo grande o troppo piccolo'
    for e in range(3,-1,-1):                   #lista che va da 0 a 3
        centinaia = (n // 10**(2+3*e))%10
        if centinaia !=0:         #10**2)%10 è le centinaia
            if centinaia > 1:     #se le centinaia sono maggiori di uno
                NumeroAParole += unita[centinaia - 1]   #alla fine cè-1 perchè nella posizione 0 cè uno e tutto è scalato indietro
            NumeroAParole += "cento"   #quella a destra si aggiunge tipo: tre-cento
        dec = (n // 10**(1+3*e))%10
        u = (n // 10**(3*e))%10
        if dec > 1:
            NumeroAParole += decine[dec - 1]
            if (u == 1 or u == 8) :   #>1 serve per controllare che ci siano decine >=2 ??
                NumeroAParole = NumeroAParole [:len(NumeroAParole)-1]  #taglia la stringa es: otannt -a
        elif dec == 1: 
            if u == 1:
                NumeroAParole += "undici"
            elif u == 2:
                NumeroAParole += "dodici"
            elif u == 3:
                NumeroAParole += "tredici"
            elif u == 4:
                NumeroAParole += "quattordici"
            elif u == 5:
                NumeroAParole += "quindici"
            elif u == 6:
                NumeroAParole += "sedici"
            elif u == 7:
                NumeroAParole += "diciassette"
            elif u == 8:
                NumeroAParole += "diciotto"
            elif u == 9:
                NumeroAParole += "diciannove"
        if dec != 1 and u != 0:
            NumeroAParole += unita[u - 1]
        if e == 3:
            if centinaia != 0 or dec != 0 or u != 0:
                if centinaia == 0 and dec == 0 and u == 1:
                    NumeroAParole = NumeroAParole [:len(NumeroAParole)-3]
                    NumeroAParole += "un miliardo "
                else:
                    NumeroAParole += "miliardi"
        if e == 2:
            if centinaia != 0 or dec != 0 or u != 0:
                if centinaia == 0 and dec == 0 and u == 1:
                    NumeroAParole = NumeroAParole [:len(NumeroAParole)-3]
                    NumeroAParole += "un milione "
                else:
                    NumeroAParole += "milioni"
        if e == 1:
            if centinaia != 0 or dec != 0 or u != 0:
                if centinaia == 0 and dec == 0 and u == 1:
                    NumeroAParole = NumeroAParole [:len(NumeroAParole)-3]  #-uno
                    NumeroAParole  += "mille"
                else:
                    NumeroAParole += "mila"
    return NumeroAParole


listone=[908000001647,18,128,508,1501,17081,981001818]

for n in listone:
    print (conv(n))
        
    
