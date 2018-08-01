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


def divide(n):  #funzione che preso un numero in input ne divide le cifre in gruppi di 3
    numero = str(n)
    lista_cifre = []
    unit = ""
    mil = ""
    mill = ""
    mld = ""
    k = len(numero)
    i = 0
    while i < len(numero):
        if 10 <= k <= 12:
            mld += numero[i]
            k -= 1
        elif 7 <= k <= 9:
            mill += numero[i]
            k -= 1
        elif 4 <= k <= 6:
            mil += numero[i]
            k -= 1
        elif 1 <= k <= 3:
            unit += numero[i]
            k -= 1
        i += 1
    lista_cifre.append(mld)
    lista_cifre.append(mill)
    lista_cifre.append(mil)
    lista_cifre.append(unit)
    return converti(lista_cifre)  #richiama converti(lista_cifre)


def converti(lista_cifre): #funzione che prende in input gruppi di cifre
    cent = ["", "cento", "duecento", "trecento", "quattrocento", "cinquecento", "seicento", "settecento", "ottocento",
            "novecento"]
    unita = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci", "undici",
             "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]
    decine = ["", "", "venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]
    decin = ["", "", "vent", "trent", "quarant", "cinquant", "sessant", "settant", "ottant", "novant"]
    lista_stringhe = []
    i = 0
    while i < len(lista_cifre): #ciclo che scorre la lista di gruppi di valori
        risultato = ""
        valore = lista_cifre[i]
        numero_cifre = len(valore)
        z = 0
        while z < len(valore): #ciclo che scorre le singole cifre nel gruppo
            if numero_cifre == 3: #se le cifre sono 3 si tratta di centinaia e va a cercare il valore corrispondente in cent
                risultato += (cent[int(valore[z])])
                z += 1
                numero_cifre -= 1 #passa alle decine
            elif numero_cifre == 2: #se le cifre sono 2 si tratta di decine e va a cercare il valore in decine
                val_null = [1, 8]
                if risultato != "" and int(valore[z]) == 8: #se la decina e' 8
                    if int(valore[z + 1]) in val_null: #se l'unita' e' 1 o 8
                        risultato += "ttant"
                    else:
                        risultato += "ttanta"
                    z += 1
                    numero_cifre -= 1
                elif int(valore[z]) == (0 or 1):    #se la decina e' 0 o 1 cerca nella lista unita' l'unione delle decine con l'unita'
                    y = valore[z] + valore[z + 1]
                    risultato += unita[int(y)]
                    numero_cifre -= 2
                    z += 2
                else:
                    if int(valore[z + 1]) in val_null: #se l'unita' e' 8 o 1 cerca il valore nella lista delle decine troncate
                        risultato += decin[int(valore[z])]
                        numero_cifre -= 1
                        z += 1
                    else:
                        risultato += decine[int(valore[z])]
                        numero_cifre -= 1
                        z += 1
            elif numero_cifre == 1:#se la cifra e' 1 cerca il valore in unita'
                risultato += unita[int(valore[z])]
                z += 1
                numero_cifre -= 1
            else:
                z += 1
        lista_stringhe.append(risultato)
        i += 1
    return lista_stringhe


def conv(n):
    numero = divide(n) #richiama la funzione divide(n)
    risultato = ""
    i = 0
    while i < len(numero): #ciclo che scorre la lista di cifre gia' convertite in lettere
        if numero[i] != "":
            if i == 0:
                if numero[i] == "uno": #controlla che il numero non sia 'uno'
                    risultato += "un miliardo"
                else:
                    risultato += numero[i] + "miliardi" #se non e' 'uno' aggiunge al numero il nome corrispondente al gruppo di cifre da 3
            elif i == 1:
                if numero[i] == "uno":
                    risultato += "un milione"
                else:
                    risultato += numero[i] + "milioni"
            elif i == 2:
                if numero[i] == "uno":
                    risultato += "mille"
                else:
                    risultato += numero[i] + "mila"
            elif i == 3:
                risultato += numero[i]
        i += 1
    return risultato
