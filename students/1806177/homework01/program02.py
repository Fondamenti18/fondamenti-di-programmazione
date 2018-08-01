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
       valore = mld(n)
    valore =valore.split()
    valore="".join(valore)
    return valore

def u(n, valore=''):
    
    if n==1:
        valore=valore[:len(valore)-1]+'uno'
    if n==2:  
        valore=valore+'due'
    if n==3:  
        valore=valore+'tre'
    if n==4:  
        valore=valore+'quattro'
    if n==5:  
        valore=valore+'cinque'
    if n==6:  
        valore=valore+'sei'
    if n==7:  
        valore=valore+'sette'
    if n==8:
        valore=valore[:len(valore)-1]+'otto'
    if n==9:  
        valore=valore+'nove'
    if n==0:  
        valore=valore+''
    return valore
        
def d(n, valore=''):
    if n==10: valore=valore+'dieci'
    elif n==11: valore=valore+'undici'
    elif n==12: valore=valore+'dodici'
    elif n==13: valore=valore+'tredici'
    elif n==14: valore=valore+'quattordici'
    elif n==15: valore=valore+'quindici'
    elif n==16: valore=valore+'sedici'
    elif n==17: valore=valore+'diciassette'
    elif n==18: valore=valore+'diciotto'
    elif n==19: valore=valore+'diciannove'
    
    elif 20<=n<=29:
        valore=u(n%10, valore +'venti')
    elif 30<=n<=39:
        valore=u(n%10, valore +'trenta')
    elif 40<=n<=49:
        valore=u(n%10, valore +'quaranta')
    elif 50<=n<=59:
        valore=u(n%10, valore +'cinquanta')
    elif 60<=n<=69:
        valore=u(n%10, valore +'sessanta')
    elif 70<=n<=79:
        valore=u(n%10, valore +'settanta')        
    elif 80<=n<=89:
        if valore[(len(valore)-2):] == "o ": 
            valore = valore[:(len(valore)-2)]              
        valore=u(n%10, valore +'ottanta')
    elif 90<=n<=99:
        valore=u(n%10, valore +'novanta')
    else:
        valore=u(n%10, valore)
    return valore

def c(n, valore=' '):
        if 100<=n<=199:
            valore=d(n%100, valore +'cento ')
        elif 200<=n<=299:
            valore=d(n%100, valore +'duecento ')
        elif 300<=n<=399:
            valore=d(n%100, valore +'trecento ')
        elif 400<=n<=499:
            valore=d(n%100, valore +'quattrocento ')
        elif 500<=n<=599:
            valore=d(n%100, valore +'cinquecento ')
        elif 600<=n<=699:
            valore=d(n%100, valore +'seicento ')        
        elif 700<=n<=799:
            valore=d(n%100, valore +'settecento ')
        elif 800<=n<=899:
            valore=d(n%100, valore +'ottocento ')
        elif 900<=n<=999: 
            valore=d(n%100, valore +'novecento ') 
        else:
            valore=d(n%100, valore)       
        return valore
    
def m(n, valore=''):
    if 1000<=n<=1999:
        valore=c(n%1000, valore +'mille ')
    elif 2000<=n<=999999:
        valore=c(n%1000, c(n//1000, valore) +'mila ')
    else:
        valore=c(n%1000, valore)
    return valore     


        
def ml(n, valore=''):
    if 1000000<=n<=199999:
        valore=m(n%1000000, valore +'unmilione ')
    elif 2000000<=n<=999999999:
        valore=m(n%1000000, m(n//1000000, valore) +'milioni ')
    else:
        valore=m(n%1000000, valore)
    return valore 
    
def mld(n, valore=''):
    if 1000000000<=n<=199999999:
        valore=ml(n%1000000000, valore +'unmiliardo ')
    elif 2000000000<=n<=999999999999:
        valore=ml(n%1000000000, ml(n//1000000000, valore) +'miliardi ')
    else:
        valore=ml(n%1000000000, valore)
        
    return valore 