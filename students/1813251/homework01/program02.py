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
    if 0<n<1000000000000:
       val = mlr(n)
    val =val.split()
    val="".join(val)
    return val

def u(n, val=''):
    
    if n==1:
        val=val[:len(val)-1]+'uno'
    if n==2:  
        val=val+'due'
    if n==3:  
        val=val+'tre'
    if n==4:  
        val=val+'quattro'
    if n==5:  
        val=val+'cinque'
    if n==6:  
        val=val+'sei'
    if n==7:  
        val=val+'sette'
    if n==8:
        val=val[:len(val)-1]+'otto'
    if n==9:  
        val=val+'nove'
    if n==0:  
        val=val+''
    return val
        
def d(n, val=''):
    if n==10: val=val+'dieci'
    elif n==11: val=val+'undici'
    elif n==12: val=val+'dodici'
    elif n==13: val=val+'tredici'
    elif n==14: val=val+'quattordici'
    elif n==15: val=val+'quindici'
    elif n==16: val=val+'sedici'
    elif n==17: val=val+'diciassette'
    elif n==18: val=val+'diciotto'
    elif n==19: val=val+'diciannove'
    
    elif 20<=n<=29:
        val=u(n%10, val +'venti')
    elif 30<=n<=39:
        val=u(n%10, val +'trenta')
    elif 40<=n<=49:
        val=u(n%10, val +'quaranta')
    elif 50<=n<=59:
        val=u(n%10, val +'cinquanta')
    elif 60<=n<=69:
        val=u(n%10, val +'sessanta')
    elif 70<=n<=79:
        val=u(n%10, val +'settanta')        
    elif 80<=n<=89:
        if val[(len(val)-2):] == "o ": 
            val = val[:(len(val)-2)]              
        val=u(n%10, val +'ottanta')
    elif 90<=n<=99:
        val=u(n%10, val +'novanta')
    else:
        val=u(n%10, val)
    return val

def c(n, val=' '):
        if 100<=n<=199:
            val=d(n%100, val +'cento ')
        elif 200<=n<=299:
            val=d(n%100, val +'duecento ')
        elif 300<=n<=399:
            val=d(n%100, val +'trecento ')
        elif 400<=n<=499:
            val=d(n%100, val +'quattrocento ')
        elif 500<=n<=599:
            val=d(n%100, val +'cinquecento ')
        elif 600<=n<=699:
            val=d(n%100, val +'seicento ')        
        elif 700<=n<=799:
            val=d(n%100, val +'settecento ')
        elif 800<=n<=899:
            val=d(n%100, val +'ottocento ')
        elif 900<=n<=999: 
            val=d(n%100, val +'novecento ') 
        else:
            val=d(n%100, val)       
        return val
    
def m(n, val=''):
    if 1000<=n<=1999:
        val=c(n%1000, val +'mille ')
    elif 2000<=n<=999999:
        val=c(n%1000, c(n//1000, val) +'mila ')
    else:
        val=c(n%1000, val)
    return val     


        
def ml(n, val=''):
    if 1000000<=n<=199999:
        val=m(n%1000000, val +'unmilione ')
    elif 2000000<=n<=999999999:
        val=m(n%1000000, m(n//1000000, val) +'milioni ')
    else:
        val=m(n%1000000, val)
    return val 
    
def mlr(n, val=''):
    if 1000000000<=n<=199999999:
        val=ml(n%1000000000, val +'unmiliardo ')
    elif 2000000000<=n<=999999999999:
        val=ml(n%1000000000, ml(n//1000000000, val) +'miliardi ')
    else:
        val=ml(n%1000000000, val)
        
    return val 