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
       
    # per il numero "0" non possiamo usare la dicitua "zero" perchè altrimenti causerebbe dei problemi con alcuni numeri, percio useremo il valore ""#
    
    if n == 0: 
        return ""
    
    # andiamo a definire i numerio minori uguali di "19" #  
    
    elif n <= 19:
        
        return ("uno", "due", "tre", "quattro", "cinque", 
                "sei", "sette", "otto", "nove", "dieci", 
                "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto", "diciannove")[n-1]
    
        # ora andiamo a definire i valori delle decine fino a "90" #         

    elif n <= 99:
        
        decine = ("venti", "trenta", "quaranta",
                  "cinquanta", "sessanta", 
                  "settanta", "ottanta", "novanta")
        
        letter = decine[int(n/10)-2]
        
        t = n%10

        # a causa dell'elisione causata da 1 e 8 andiamo a specificare l'elisione di una lettera #

        if t == 1 or t == 8:
        
            letter = letter[:-1]
        
        return letter + conv(n%10)
        
        # defioniamo che i numeri fino a 199 devono avere la radice "centO" # 
    
    elif n <= 199:
     
        return "cento" + conv(n%100)
     
        # per tutti i numeri compresi fra "200" e "999" basta incrementare di un valore ogni centinaia #
    
    elif n <= 999:
        
        m = n%100
        m = int(m/10)
        letter = "cent"
    
        # quando c'è un valore con l'"8" bisogna aggiongere una "o", percio #
    
        if m != 8:
        
            letter = letter + "o"
            
        return conv( int(n/100)) + \
               letter + \
               conv(n%100)
        
        # definiamo che i numeri compresi fra "1000" e "1999" hanno la radice "mille" #
    
    elif n<= 1999 :
        
        return "mille" + conv(n%1000)
        
        # definiamo che per i numeri compresi fra "2000" e "999999" i numeri hanna la radice mila  #
    
    elif n<= 999999:
        
        return conv(int(n/1000)) + \
               "mila" + \
               conv(n%1000)
         
        # definiamo che per i numerio compresi tra "1000000" e "1999999" la radice sarà "unmilione"#
    
    elif n <= 1999999:
        
        return "unmilione" + conv(n%1000000)
        
        # definiamo che per i numeri compresi fra "1999999" e "999999999" la radice sarà milioni con l' incremento della prima cifra di +1 per ogni milione #
    
    elif n <= 999999999:
        
        return conv(int(n/1000000))+ \
               "milioni" + \
               conv(n%1000000)
         
        # definiamo che per i numerio compresi tra "1000000000" e "1999999999" la radice sarà "unmiliardo" #
    
    elif n <= 1999999999:
        
        return "unmiliardo" + conv(n%1000000000)
         
    else:
        
        return conv(int(n/1000000000)) + \
               "miliardi" + \
               conv(n%1000000000)
         
        # facciamo eseguire l'intero programma con il camando return #    
    
    return conv(n)          
   
