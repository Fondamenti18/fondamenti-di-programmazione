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
    una_cifra = ['', 'uno', 'due','tre','quattro','cinque', 'sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici',
             'diciassette','diciotto','diciannove']
    decine = ['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    prova = []
    if type(n) != int and n<0 and n>1000000000000:
        return "Inserisci un valore corretto"
    if n<=19:
        return una_cifra[n]
    if n<=99:
        if n%10 == 0:
            return decine[int(n/10)-2]
        else:
            b = n%10
            lettera = decine[int (n/10)-2]
            if b == 1 or b == 8:
                lettera = lettera[:-1]
            prova = [lettera,una_cifra[b]]
            return ''.join(prova)
    if n<=199:
            a = n%100
            if int(a/10) == 8:
                return "cent" + conv(n%100)
            else:
                return "cento" + conv(n%100)
    if n<=999:
        a = n%100
        if int(a/10) == 8:
            return conv(int(n/100)) + "cent" + conv(n%100)
        else:
            return conv(int(n/100)) + "cento" + conv(n%100)
    if n<=1999:
            return "mille" + conv(n%1000)
    if n<=999999:
            return conv(int(n/1000)) + "mila" + conv(n%1000)
    if n<=999999999:
            if int(n/1000000) == 1:
                return "unmilione" + conv(n%1000000)
            else:
                return conv(int(n/1000000)) + "milioni" + conv(n%1000000)
    if n<=999999999999:
            if n/1000000000 == 1:
                return "unmiliardo" + conv(n%1000000000)
            else:
                return conv(int(n/1000000000)) + "miliardi" + conv(n%1000000000)
