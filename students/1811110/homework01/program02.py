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
import math


u=["uno","due","tre","quattro","cinque","sei","sette","otto","nove","dieci","undici","dodici",
   "tredici","quattordici","quindici","sedici","diciassette","diciotto","dicianove"]
p2=["dieci","venti","trenta","quaranta","cinquanta","sessanta","settanta","ottanta","novanta"]
p3=["cento","duecento","trecento","quattrocento","cinquecento","seicento","settecento","ottocento","novecento"]

def cento(n):
           unit=""
           d=n//10
           w=p2[d-1]   #aggiungo a w le decine
           i=n%10
           if (i != 0):
               unit=u[i-1]
           if i==1 or i==8:
               w=w[:-1] 
               w=w+conv(n%10)
               return w
           else:
               w=w+unit
               return w

def duecento(n):
           a=conv(n%100)
           if(n%100<90 and n%100>79):
               w="cent"+ a
           else:
               w="cento"+ a
           return w

def mille(n):
           c=n//100
           a=p3[c-1]  #dentro a a ci sono le centinaia a lettere 
            
           d=n%100
           if(d<90 and d>79):
               w=a[:-1]+conv(d)
           else:
               w=a+conv(d)
           return w
def conv(n):

       if n==0:
           w="zero"
           return w

       elif n<=19:
            w=u[n-1]
            return w

       elif n<=99:
           w=cento(n)
           return(w)
           
       elif n<=199:
           w=duecento(n)
           return(w)

       elif n<=999:
           w=mille(n)
           return w

       elif n<=1999:
           w="mille"+conv(n%1000)
           return w

       elif n<=999999:
           w=conv(n//1000)+"mila"+conv(n%1000)
           return w


       elif n<=1999999:
           w="unmilione"+conv(n%1000000)
           return w

       elif n<=999999999:
           w=conv(n//1000000)+"milioni"+conv(n%1000000)
           return w

       elif n<=1999999999:
            w="unmiliardo"+conv(n%1000000000)
            return w

       elif n<=999999999999:
           w=conv(n//1000000000)+"miliardi"+conv(n%1000000000)
           return w
    
