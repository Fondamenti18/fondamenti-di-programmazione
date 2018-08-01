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



unita = ["","uno","due","tre","quattro","cinque","sei","sette","otto","nove"]
unitaa = ["dieci","undici","dodici","tredici","quattordici","quindici","sedici","diciassette","diciotto","diciannove"]
decine = ["","dieci","venti","trenta","quaranta","cinquanta","sessanta","settanta","ottanta","novanta"]
centine =["","due","tre","quattro","cinque","sei","sette","otto","nove"]
migliaia=["mille","duemila","tremila","quattromila","cinquemila","seimila","settemila","ottomila","novemila",]
cose =["mila","unmilione","milioni","unmiliardo","miliardi","cent"]
       
def uno_due(n):
    s = str(n)
    a = len(s)
    if a == 1:
        return (unita[n])
    elif a == 2 and n<=19:
        return (unitaa[n-10])
    elif a == 2 and n>=20:
        l = decine[n//10]
        t = n%10
        if t == 1:
            l = l[:-1]
        if t == 8:
            l = l[:-1]
        return l + conv(n%10)


def tre(n):
    s = str(n)
    a = len(s)
    if a == 3:
        l = centine[n//100-1]
        p = (n%100)//10
        u = cose[5]
        if p != 8:
            u = cose[5] + "o"   
        return l + u + conv(n%100)


def quattro(n):
    s = str(n)
    a = len(s)
    if a == 4:
        l = migliaia[n//1000-1]
        return l + conv(n%1000)

def cinque_sei(n):
    s = str(n)
    a = len(s)
    if a == 5 or a == 6:
        return conv(n//1000) +  cose[0] +  conv(n%1000)

def sette(n):
    s = str(n)
    a = len(s)
    if a == 7 and n<=1999999:
        return cose[1] + conv(n%1000000)

def sette_2(n):
    s = str(n)
    a = len(s)
    if a == 7 and n>1999999:
        return conv(n//1000000)+  cose[2] +  conv(n%1000000)


def otto_nove(n):
    s = str(n)
    a = len(s)
    if a == 8 or a == 9 :
        return conv(n//1000000)+  cose[2] +  conv(n%1000000)

def dieci(n):
    s = str(n)
    a = len(s)
    if a == 10 and n<= 1999999999:
        return cose[3] + conv(n%1000000000)     

def dieci_2(n):
    s = str(n)
    a = len(s)
    if a == 10 and n> 1999999999:
        return conv(n//1000000000) +  cose[4] +  conv(n%1000000000)

def altro(n):
    s = str(n)
    a = len(s)
    if a>10:      
        return conv(n//1000000000) +  cose[4] +  conv(n%1000000000)


def conv(n):
    s = str(n)
    a = len(s)
    if a==1 or a==2:return uno_due(n)
    elif a==3:return tre(n)
    elif a==4:return quattro(n)
    elif a==5 or a==6:return cinque_sei(n)
    elif a==7 and n<=1999999:return sette(n)
    elif a==7 and n>1999999:return sette_2(n)
    elif a==8 or a==9:return otto_nove(n)
    elif a==10 and n<= 1999999999:return dieci(n)
    elif a==10 and n> 1999999999:return dieci_2(n) 
    else:return altro(n)
