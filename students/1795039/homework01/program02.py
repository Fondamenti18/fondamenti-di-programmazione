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


def calcola(n):
    if n == 0: 
        return ""
        
    elif n <= 19:
        return ("uno", "due", "tre", "quattro", "cinque", 
                "sei", "sette", "otto", "nove", "dieci", 
                "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto", "diciannove")[n-1]
    
                
    elif n <= 99:
        parole = n99(n)
        return parole + calcola(n%10)
        
    elif n <= 199:
        return "cento" + calcola(n%100)
        
    elif n <= 999:
        parole = n999(n)
        
        return calcola( int(n/100)) + parole + calcola(n%100)
        
    elif n<= 1999 :
        
        return "mille" + calcola(n%1000)
    
    elif n<= 999999:
        return calcola(int(n/1000)) + "mila" + calcola(n%1000)
        
    elif n <= 1999999:
        return "unmilione" + calcola(n%1000000)
        
    elif n <= 999999999:
        
        return calcola(int(n/1000000))+ "milioni" + calcola(n%1000000)
    
    elif n <= 1999999999:
        return "unmiliardo" + calcola(n%1000000000)
        
    else:
        return calcola(int(n/1000000000)) + "miliardi" + calcola(n%1000000000)

def n99(n):

    decine = ("venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta")
    parole = decine[int(n/10)-2]
    speciale = n%10
    if speciale == 1 or speciale == 8:
        parole = parole[:-1]

    return parole

    

def n999(n):

    speciale = n%100
    speciale = int(speciale/10)
    parole = "cent"
    if speciale != 8:
        parole = parole + "o"

    return parole

    

def conv(n):
  
   if n == 0:
      num = "zero"
   else:
      num = calcola(n)
   return num

	


