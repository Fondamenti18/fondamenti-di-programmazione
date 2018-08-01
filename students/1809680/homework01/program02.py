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
    if n<= 19:
        inizio=('uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove')
        return inizio[n-1]
    elif n<=99:
        decine=('venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta')
        parte_decine=decine[n//10 -2]
        if n%10==0:
            return decine[n//10 -2]
        elif n%10==1 or n%10==8:
            parte_decine=parte_decine[:-1]
        return parte_decine + conv(n%10)
    elif n<=199:
        if n==100:
            return 'cento'
        else:
            return 'cento'+conv(n%100)
    elif n<=999:
        if n%100==0:
            return conv(n//100)+'cento'
        else:
            return conv(n//100)+'cento'+conv(n%100)
    elif n<=1999:
        if n==1000:
            return 'mille'
        else:
            return 'mille'+conv(n%1000)
    elif n<=9999:
        if n%1000==0:
            return conv(n//1000)+'mila'
        else:
            return conv(n//1000)+'mila'+conv(n%1000)
    elif n<=99999:
        if n%1000==0:
            return conv(n//1000)+'mila'
        else:
            return conv(n//1000)+'mila'+conv(n%1000)
    elif n<=999999:
        if n%1000==0:
            return conv(n//1000)+'mila'
        else:
           return conv(n//1000)+'mila'+conv(n%1000)
    elif n<=9999999:
        if n==1000000:
            return 'unmilione'
        elif n//1000000==1:
            return 'unmilione'+conv(n%1000000)
        elif n%1000000==0:
            return conv(n//1000000)+'milioni'
        else:
            return conv(n//1000000)+'milioni'+conv(n%1000000)
    elif n<=99999999:
        if n%1000000==0:
            return conv(n//1000000)+'milioni'
        elif str(n//10000).endswith('8'):
            return conv(n//1000000)+'milioni'+'ottocent'+conv(n%100000)[-33:-11]+'ottantotto'
        else:
            return conv(n//1000000)+'milioni'+conv(n%1000000)
    elif n<=999999999:
        decine=('venti','ottanta')
        end=str(n//10000000)
        if n%10000000==0:
            return conv(n//1000000)+'milioni'
        elif end.endswith('8'):
            return conv(n//100000000)+'cent'+conv(n%100000000)
        else:
            return conv(n//1000000)+'milioni'+conv(n%1000000)
    elif n<=1999999999:
        if n==1000000000:
            return 'unmiliardo'
        else:
            return 'unmiliardo'+conv(n%1000000000)
    elif n<=9999999999:
        return conv(n//1000000000)+'miliardi'+conv(n%1000000000)
    elif n<=999999999999:
        return conv(n//1000000000)+'miliardi'+conv(n%1000000000)
            
        
        
        
        
        
        
        
      