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
    if n in range(1,10):
        return ("uno", "due", "tre", "quattro", "cinque",               # cambia il numero in input da cifra a lettere nel range 
                "sei", "sette", "otto", "nove")[n-1]                    # da 1 a 9.
    
    
    if n in range(10,20):                                               # torna il numero in input da cifra a lettere nel range 
        return ("dieci", "undici", "dodici", "tredici"                  # da 10 a 19.
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto","dicianove")[n-11]
    
    if n in range(20,100):                                              # l'insieme k rappresenta la traduzione da cifre a lettere
        k = ("venti", "trenta", "quaranta",                              # di tutte le decine .
                     "cinquanta", "sessanta", "settanta",
                     "ottanta", "novanta")
        c = k[int(n/10)-2]                                              # cambio tutti i numeri da 20 a 99 in lettere specialmente 
        b = n%10                                                        # tutti i numeri che eludono le finali, tutte le decine 
        if b == 1 or b == 8:                                            # da 1 a 8, ad esempio 21 e 38.
            c = c[:-1]
        return c + conv(n%10)
        
    if n in range(100,200):                                             # il range scorre tutti i numeri da scrivere in lettere 
        return ("cento" + conv(n%100))                                  # dati in input da 100 a 199.
                
    if n in range(200,1000):                                            # il range scorre da 200 a 999, tutti i numeri in centinaia
        x = n%100                                                       # e con decina in 8 eludono le finali come ad esempio 180,380        
        x = int(x/10)                                                   # tutti gli altri numeri non eludono le finali compreso 
        c = "cent"                                                      # l'8 nelle unità.
        if x != 8:
            c = c + "o"
        return conv(int(n/100)) + c + conv(n%100)
    
    if n in range(1000,2000):                                           # il range scorre da 1000 a 1999 e aggiunge in lettere "mille" 
        return "mille" + conv(n%1000)                                   # con tutte le eccezioni presentate dagli if precedenti,
                                                                        # fa lo stesso fino a numeri compresi miliardi.
    if n in range(2000,1000000):
        return conv(int(n/1000)) + "mila" + conv(n%1000)
    
    if n in range(100000,2000000):
        return "unmilione" + conv(n%1000000)
    
    if n in range(2000000,1000000000):
        return conv(int(n/1000000)) + "milioni" + conv(n%1000000)
    
    if n in range(1000000000,2000000000):
        return "unmiliardo" + conv(int(n/1000000000))

    if n in range(2000000000,10000000000):
        return conv(int(n/1000000000))+ "miliardi" + conv(n%1000000000)
    
    if n in range(10000000000,2000000000000):
        return conv(int(n/10000000000))+ "miliardi" + conv(n%10000000000)