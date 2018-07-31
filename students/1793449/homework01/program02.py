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

def conv(n):
    #Controllo a quanto equivale il mio n
    if n < 20:
        #Se n è minore di 20 allora varra' uno dei seguenti valori ordinati
        parola = ["","uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"][n]   
    elif n < 100:
        #Se n è minore di 100 allora utilizzo una lista di decine da 20 a 90 come numerazione, dove prendo il valore della decina di n
        inizio = ["venti", "trenta", "quaranta","cinquanta", "sessanta", "settanta", "ottanta", "novanta"][int(n / 10) - 2]
        #Se le unita' sono uno o otto, allora elimino l'ultima lettera della parte iniziale della parola
        if (n % 10) == 1 or (n % 10) == 8:
            inizio = inizio[:-1]
        #Avendo calcolato ora solamente parola iniziale fino alla decina, richiamo di nuovo la mia funzione cosi' da calcolare a quanto il mio resto, cioe' l'unita', equivalga in lettere
        parola = inizio + conv(n % 10)  
    elif n < 200:
        #Se n e' minore di 200 allora la mia parola sara' cento piu' i processi precedenti, richiamo quindi la funzione con n pari alle mie decine e unita' sommate (ex. se ho 123 allora n sara' richiamato come 23)
        parola = "cento" + conv(n % 100)  
    elif n < 1000:
        inizio = "cento"
        #Se la mia unita' di n e' uguale da 8, allora rimuovo la "o" finale dell'inizio della mia parola
        if int((n % 100) / 10) == 8:
            inizio = inizio[:-1]
        #Calcolo la parola trovando anche all'inizio della parola a quanto la mia centinaia equivalga in lettere
        parola = conv(int(n / 100)) + inizio + conv(n % 100)
    elif n < 2000:
        #Faccio lo stesso passaggio eseguito per i n < 200, solo che invece di dare decine ed unita' alla funzione, do' anche le centinaia (ex. se ho 1234 restituisco 234)
        parola = "mille" + conv(n % 1000)
    elif n < 1000000:
        #Stessi passaggi precedenti, solamente che all'inizio della parola richiamo di nuovo la funzione conv, questa volta non volendo trovare il resto della funzione, quindi le ultime cifre, ma la cifra piu' "significativa"
        parola = conv(int(n / 1000)) + "mila" + conv(n % 1000)
    elif n < 2000000:
        #Stesso passaggio eseguito per cento con diverso n
        parola = "unmilione" + conv(n % 1000000)
    elif n < 1000000000:
        #Stesso passaggio eseguito per mila con diverso n
        parola = conv(int(n / 1000000)) + "milioni" + conv(n % 1000000)
    elif n < 2000000000:
        #Stesso passaggio eseguito per cento con diverso n
        parola = "unmiliardo" + conv(n % 1000000000) 
    else:
        #Stesso passaggio eseguito per mila con diverso n
        parola = conv(int(n / 1000000000)) + "miliardi" +  conv(n % 1000000000)
    return parola