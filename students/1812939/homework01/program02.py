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


def conv(num):
    if num==0:
        return ""
    elif num<=19:
        return("uno","due","tre","quattro","cinque","sei","sette","otto",
               "nove","dieci","undici","dodici","tredici","quattordici","quindici",
               "sedici","diciassette","diciotto","diciannove")[num-1]
    elif num<=99:
        dieci=("venti","trenta","quaranta","cinquanta","sessanta",
               "settanta","ottanta","novanta")
        parola=dieci[int(num/10)-2]
        i=num%10
        if i==1 or i==8:
            parola=parola[:-1]
        return parola+conv(num%10)
    elif num<=199:
        return "cento"+conv(num%100)
    elif num<=999:
        j=num%100
        j=int(j/10)
        parola="cent"
        if j!=8:
            parola=parola+"o"
        return conv(int(num/100))+\
               parola+\
               conv(num%100)
    elif num<=1999:
        return "mille"+conv(num%1000)
    elif num<=999999:
        return conv(int(num/1000))+\
               "mila"+\
               conv(num%1000)
    elif num<=1999999:
        return "unmilione"+conv(num%1000000)
    elif num<=999999999:
        return conv(int(num/1000000))+\
               "milioni"+\
               conv(num%1000000)
    elif num<=1999999999:
        return "unmiliardo"+conv(num%1000000000)
    else:
        return conv(int(num/1000000000))+\
               "miliardi"+\
               conv(num%1000000000)
                    
