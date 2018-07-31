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
def under100(under20,over20,n):
    
    if n==0: return ''
    
    elif n<= 19: return under20[n-1]
    
    else:
        resto=n%10
        prefisso=over20[n//10-2]
        
        if resto==1 or resto==8:
            prefisso=prefisso[:-1]
        return prefisso + conv(resto)
 
def under1000(n):   

        resto=n%100
        resto=resto//10
        prefisso="cent"
        
        if resto !=8: prefisso="cento"
        
        if n<=199: return prefisso + conv(n%100)
        else: return conv(n//100) + prefisso + conv(n%100)
        
def under1000000000(n):
    if n<= 1999: return "mille" + conv(n%10**3)
    elif n<=999999: return conv(n//10**3) + "mila" + conv(n%10**3)
    elif n<=1999999: return "unmilione" + conv(n%10**6)
    else: return conv(n//10**6) + "milioni" + conv(n%10**6)
    
def conv(n):
    'Scrivete qui il codice della funzione'
    
    under20=("uno","due","tre","quattro","cinque","sei","sette","otto","nove","dieci","undici","dodici","tredici","quattordici","quindici","sedici","diciassette","diciotto","diciannove")
    over20=("venti","trenta","quaranta","cinquanta","sessanta","settanta","ottanta","novanta")
    
    if n<=99:return under100(under20,over20,n)
    if n<=999:return under1000(n)
    if n<=999999999:return under1000000000(n)     
    
    else:        
        if n<=1999999999: return "unmiliardo" + conv(n%10**9)
        else: return conv(n//10**9) + "miliardi" + conv(n%10**9)

        
        
    