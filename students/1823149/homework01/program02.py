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
    if n<20:
        return ("uno","due","tre","quattro","cinque","sei","sette","otto","nove","dieci","undici","dodici","tredici","quattordici","quindici","sedici","diciassette","diciotto","diciannove") [n-1]
    elif n<100:
        return minore_cento(n)
    elif n<1000:
        return minore_mille(n)
    if n<1000000000000:
        if n<1000000:
            a,b,c=3,"mille","mila"
        elif n<1000000000:
            a,b,c=6,"unmilione","milioni"
        elif n<1000000000000:
            a,b,c=9,"unmiliardo","miliardi"
        return funzione_standard(n,a,b,c)    
def funzione_standard(n,pot,singolare,plurale):
    x=int(n/(10**pot))
    y=n%(10**pot)
    if y!=0:
        if x==1:
            return singolare+conv(y)
        else:
            return conv(x)+plurale+conv(y)
    elif x==1:
        return singolare
    else:
        return conv(x)+plurale
        
def minore_cento(n):
    decineInLettere =("venti","trenta","quaranta","cinquanta","sessanta","settanta","ottanta","novanta")
    decine=int(n/10)
    unita=n%10
    decineLettere=decineInLettere[decine-2]
    if (unita==1 or unita==8):
        decineLettere= decineLettere[:-1]
    if (unita==0):
        return decineLettere
    else:
        return decineLettere + conv(unita)

def minore_mille(n):
    centinaia=int(n/100)
    restocentinaia=n%100
    testo="cento"
    if (restocentinaia>79 and restocentinaia<90):
        testo=testo[:-1]
    if restocentinaia!=0:
        if centinaia==1:
            return testo+conv(restocentinaia)
        else:
            return conv(centinaia)+testo+conv(restocentinaia)
    elif centinaia==1:
        return testo
    else:
        return conv(centinaia)+"cento"