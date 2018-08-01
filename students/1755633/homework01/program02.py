
''' In determinate occasioni ci capita di dover scrivere i numeri in parole, 
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
e restituisce in output una stringa con il numero espresso in parole

ATTENZIONE: NON USATE parole ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


 

def numLet(n): #definizione funzione(ricorsiva)
    
    if n==0: 
        return ""
    
    elif n<=19:
        return ("uno", "due", "tre", "quattro", "cinque","sei", "sette", "otto", "nove", "dieci","undici", "dodici", "tredici",   
                "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove")[n-1] 
                
    elif n<=99:
        decine=("venti", "trenta", "quaranta","cinquanta", "sessanta","settanta", "ottanta", "novanta")
        parola=decine[int(n/10)-2]           
        v=n%10
        if v==1 or v==8:
            parola=parola[:-1]
        return parola+numLet(n%10)                
                
                 
    elif n<=199:
        return "cento" + numLet(n%100)     
        
        
    elif n<= 999:
        c= n%100
        c=int(c/10)
        parola="cent"
        if c!=8:
            parola=parola + "o"
        return numLet( int(n/100))+ parola + numLet(n%100)     
               
               
    elif n<=1999 :
        return "mille" +numLet(n%1000)
         
  
    elif n<=999999:
        return numLet(int(n/1000))+ "mila" + numLet(n%1000)
               
                       
    elif n <=1999999:
        return "unmilione" + numLet(n%1000000)
         
    elif n <=999999999:
        return numLet(int(n/1000000))+ "milioni"+  numLet(n%1000000)              
               
    elif n <= 1999999999:
        return "unmiliardo" + numLet(n%1000000000)  
 
    else:
       return numLet(int(n/1000000000))+  "miliardi" +numLet(n%1000000000)
                            
 

def conv(n):  #definizione funzione

      num = numLet(n)#chiamata della funzione 
      return num #ritorniamo il valore in stringa
 
