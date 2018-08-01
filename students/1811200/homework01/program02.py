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

def numeri_fino_a_venti(n):
    numeridaunoadieci=["","uno","due","tre","quattro","cinque","sei","sette","otto","nove","dieci","undici","dodici","tredici","quattordici","quindici","sedici","diciasette","diciotto","diciannove","venti"]
    if n<=20:
        n=numeridaunoadieci[n:n+1]
    return n

def decine(n):
     decine=["venti","trenta","quaranta","cinquanta","sessanta","settanta","ottanta","novanta"]
     lettere= decine[int(n/10)-2]
     p=n%10
     if p==1 or p==8:
         lettere=lettere[:-1]
     return lettere + numeri_fino_a_venti(n%10)
 

def cento(n):
    centinaia=["cento"]
    lettere = centinaia[int(n/100-2)]
    p=n%100
    if p==80:
        lettere=lettere[:-1]
    return(lettere + decine(n%100))
    if n<=120:
        return (lettere + numeri_fino_a_venti(n%100))
    else:
        return (lettere + decine(n%100))
    
def centinaia(n):
    lettere=["cento"]
    p=n%100
    p=int(p/10)
    if n<=999:
        lettere=["cento"]
        if p==1 or p==8:
         lettere=lettere[:-1]
        return (numeri_fino_a_venti + lettere + decine)
    else:
        return (numeri_fino_a_venti(n)+ lettere + decine(n))

def mille(n):
    mille=["mille"]
    p=n%100
    p=int(p/100)
    if n<=1999:
        return(mille + decine(n%100))

def conv(n):
    if n<=20:
        return numeri_fino_a_venti(n)
    if n<=99:
        return decine(n)
    if n<=199:
        return cento(n)
    if n<=999:
        return centinaia(n)
    
                
                    
         
            
            
            
    
      
          
          
        
    
    
    
     
        

    
    
    
    
    
       
     
        
        
    
        
        
    
    


    
