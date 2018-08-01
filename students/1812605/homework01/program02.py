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
def conv (n):
    numero = n
    if numero == 0:
        return ''
    if numero <= 19:                                                    # Fino a 19
        return ("uno", "due", "tre", "quattro", "cinque", 
                "sei", "sette", "otto", "nove", "dieci", 
                "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto", "diciannove")[numero-1]            
    if numero <= 99 :                                                   # Fino a 99
        decine = ("venti", "trenta", "quaranta",
                  "cinquanta", "sessanta", 
                  "settanta", "ottanta", "novanta")
        letter = decine[int(n/10)-2]
        n1 = numero%10
        if n1 == 1 or n1 == 8:                                              # Elisione
            letter = letter[:-1]
        return letter + conv(n%10)     
    if n <= 199:                                                        # Fino a 199
        return "cento" + conv(n%100)    
    if n <= 999:                                                        # Da 200 a 999
        n2 = numero%100
        n2 = int(n2/10)
        cent_pref = "cent"                                                  # Trick prefisso
        if n2 != 8:
            cent_pref = cent_pref + "o"
        return conv( int(numero/100)) + \
               cent_pref + \
               conv(numero%100)     
    if numero<= 1999 :                                                  # Da 1000 a 1999
        return "mille" + conv(numero%1000) 
    if numero<= 999999:                                                 # Da 2000 a 999999
        return conv(int(numero/1000)) + \
               "mila" + \
               conv(numero%1000)     
    if numero <= 1999999:                                               # Da 1Mln a 1999999
        return "unmilione" + conv(numero%1000000)    
    if numero <= 999999999:                                             # Fino a 999999999
        return conv(int(numero/1000000))+ \
               "milioni" + \
               conv(numero%1000000)
    if numero <= 1999999999:                                            # Da 1 mld a 1999999999
        return "unmiliardo" + conv(numero%1000000000)     
    else:
        return conv(int(numero/1000000000)) + \
               "miliardi" + \
               conv(numero%1000000000)