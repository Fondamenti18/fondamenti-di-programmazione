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
def scrooge(n):
    if n==1000000000:
        return 'unmiliardo'
    elif n//1000000000==1:
        'unmiliardo'+baby(n%1000000000)
    elif n%1000000000==0:
        return blink(n//1000000000)+'miliardi'
    else:
        return blink(n//1000000000)+'miliardi'+baby(n%1000000000)
def baby(n):
    if n<1000000:
        return mila(n)
    if n==1000000 :
        return 'unmilione'
    elif n//1000000==1:
        return 'unmilione'+mila(n%1000000)
    elif n%1000000==0:
        return blink(n//1000000)+'milioni'
    else:
        return blink(n//1000000)+'milioni'+mila(n%1000000)
def mila(n):
    if n<1000:
        return blink(n)
    elif n%1000==0 and n//1000==1:
        return 'mille'
    elif n//1000==1 :
        return 'mille'+blink(n%1000)
    elif n%1000==0:
        officina(n//1000)+'mila'
    else:
       return blink(n//1000)+'mila'+blink(n%1000)
def blink(n):
    centinaia=['0','cento','duecento','trecento','quattrocento','cinquecento','seicento','settecento','ottocento','novecento']
    if n<100:
        return officina(n)
    if n%100==0 :
        return centinaia[(n//100)]
    elif ((n%100)%80)<9 and ((n%100)//80)>0:
        return centinaia[(n//100)][0:-1]+officina(n%100)
    else: 
        return centinaia[(n//100)]+officina(n%100)
def officina(n):
    unita =['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    decine=['0','0','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    if n<20 :
        return unita[n]
    elif n%10!=1 and n%10!=8 and n%10!=0  :
        return decine[n//10]+unita[n%10]
    elif n%10==1 or n%10==8 :
        return decine[n//10][0:-1]+unita[n%10]
    elif n%10==0 and n<100 :
        return decine[n%10]
def conv(n):
    if n<100 :
        return officina(n)
    elif n<1000:
        return blink(n)
    elif n<1000000:
        return mila(n)
    elif n<1000000000 :
        return baby(n)
    elif n<1000000000000 :
        return scrooge(n)
    else:
        return 'questo numero non mi piace'