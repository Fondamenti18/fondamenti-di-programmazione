''' In determinate occasioni ci capita di dover scrivere i numeri in letterae, 
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
e restituisce in output una stringa con il numero espresso in letterae

ATTENZIONE: NON USATE letteraE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


'''
    'Scrivete qui il codice della funzione'
    '''
def conv(n):

    if n == 0: 
        return ""
         
    elif n <= 19:
        return ("uno", "due", "tre", "quattro", "cinque", "sei", "sette", 
                "otto", "nove", "dieci", "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici","diciassette", "diciotto", 
                "diciannove")[n-1]
                 
    elif n <= 99:
        decine = ("venti", "trenta", "quaranta","cinquanta", "sessanta", 
                  "settanta", "ottanta", "novanta")
        lettera = decine[int(n/10)-2]
        x = n%10
        if x == 1 or x == 8:
            lettera = lettera[:-1]
        return lettera + conv(n%10)
         
    elif n <= 199:
        return "cento" + conv(n%100)
         
    elif n <= 999:
        y = n%100
        y = int(y/10)
        lettera = "cent"
        if y != 8:
            lettera = lettera + "o"
        return conv( int(n/100)) + \
               lettera + \
               conv(n%100)
         
    elif n<= 1999 :
        return "mille" + conv(n%1000)
     
    elif n<= 999999:
        return conv(int(n/1000)) + \
               "mila" + \
               conv(n%1000)
         
    elif n <= 1999999:
        return "unmilione" + conv(n%1000000)
         
    elif n <= 999999999:
        return conv(int(n/1000000))+ \
               "milioni" + \
               conv(n%1000000)
    elif n <= 1999999999:
        return "unmiliardo" + conv(n%1000000000)
         
    else:
        return conv(int(n/1000000000)) + \
               "miliardi" + \
               conv(n%1000000000)
 
