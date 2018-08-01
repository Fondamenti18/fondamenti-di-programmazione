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
    if n == 0: 
        return ""
         
    elif 0 < n <= 19:
        return ("uno", "due", "tre", "quattro", "cinque", 
                "sei", "sette", "otto", "nove", "dieci", 
                "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto", "diciannove") [n-1]
        
    elif 19< n <= 99:
        multipli_dieci= ("venti", "trenta", "quaranta","cinquanta", "sessanta", "settanta", "ottanta", "novanta")
        
        unita = n%10
        if unita == 1 or unita == 8:
             multipli_dieci = [ stringa[:-1] for stringa in multipli_dieci ]
        return (multipli_dieci)[(n//10)-2]+ conv(n%10)
    
    elif 99<n <= 199:
        centinaia="cento"
        if 80<=n%100<=89:
            centinaia=centinaia[:-1]
        return centinaia + conv(n%100)      
    
    elif 199<n<=999:
        cifra_significativa=conv(n//100)
        multiplo_centinaia="cento"
        if 80<=n%100<=89:
            multiplo_centinaia= multiplo_centinaia[:-1]
        return cifra_significativa + multiplo_centinaia + conv(n%100)
        
    elif 1000<=n<=1999:        
        return  "mille" + conv(n%1000) 
        
    elif  1999<n<=999999 :               
        return conv(n//1000)+"mila"+conv(n%1000) 
    
    elif 1000000 < n <= 1999999:       
        return "unmilione"+ conv(n%1000000)
    
    elif 1999999 < n <= 999999999:                 
        return conv(n//1000000)+"milioni"+conv(n%1000000)
    
    elif  1000000000 <= n <= 1999999999:
        return "unmiliardo"+conv(n%1000000000)
    
    elif 1999999999 < n <= 999999999999:
        return conv(n//1000000000)+"miliardi"+conv(n%1000000000)