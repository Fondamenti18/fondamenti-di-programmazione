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
        if n==0:
                L0=''
                return L0
        elif n<=19:
                L1=('uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove')
                return L1[n-1]
        elif n<=99:
                L2=('venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta')
                unit=n%10
                L3=L2[int(n/10)-2]
                if unit==1 or unit==8:
                        L3=L3[:-1]
                return L3+conv(unit)
        elif n<=199:
                decine_unit=(n%100)
                L4='cento'
                if int(decine_unit/10)==8:
                        L4=L4[:-1]
                return L4+conv(decine_unit)
        elif n<=999:
                decine_unit=(n%100)
                L4='cento'
                if int(decine_unit/10)==8:
                        L4=L4[:-1]
                return conv(int(n/100))+L4+conv(n%100)
        elif n<=1999:
                L5='mille'
                return L5+conv(n%1000)
        elif n<=999999:
                L6='mila'
                return conv(int(n/1000))+L6+conv(n%1000)
        elif n<=1999999:
                L7='unmilione'
                return L7+conv(n%1000000)
        elif n<=999999999:
                L8='milioni'
                return conv(int(n/1000000))+L8+conv(n%1000000)
        elif n<=1999999999:
                L9='unmiliardo'
                return L9+conv(n%1000000000)
        elif n<=999999999999:
                L10='miliardi'
                return conv(int(n/1000000000))+L10+conv(n%1000000000)
