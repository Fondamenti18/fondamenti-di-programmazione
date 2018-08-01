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

dizuni = {0: "", 1: "uno", 2: "due", 3: "tre", 4: "quattro", 5: "cinque", 6: "sei", 7: "sette",
          8: "otto", 9: "nove", 10: "dieci", 11: "undici", 12: "dodici", 13: "tredici", 14: "quattordici",
          15: "quindici", 16: "sedici", 17: "diciassette", 18: "diciotto", 19: "diciannove"}
dizdecine = {'0': "", '2': "venti", '3': "trenta", '4': "quaranta", '5': "cinquanta", '6': "sessanta",
             '7': "settanta", '8': "ottanta", '9': "novanta"}
dizcenti = {'0': "", '1': "cento", '2': "duecento", '3': "trecento", '4': "quattrocento", '5': "cinquecento", '6': "seicento",
            '7': "settecento", '8': "ottocento", '9': "novecento"}
ordini = ["", "mila", "milioni", "miliardi"]
ordini_singolari = ["", "mille", "milione", "miliardo"]


def conv_cent(num):
    ris = ''
    if int(num[1:]) <= 19:
        ris += dizuni[int(num[1:3])]
    else:
        if num[2] == '1' or num[2] == '8':
            ris = dizdecine[num[-2]][0:-1] + dizuni[int(num[-1])]
        else:
            ris = dizdecine[num[1]] + dizuni[int(num[2])]
    if num[1] == '8':
        ris = dizcenti[num[0]][0:-1] + ris
    else:
        ris = dizcenti[num[0]] + ris
    return ris


def conv(n):
    num = str(n)
    zeri = 3 - (len(num) % 3) # zeri da aggiungere (normalizzazione)
    if zeri != 3: num = ('0' * zeri) + num # se ho meno di 3 zeri da aggiungere li aggiungo altrimenti va gia bene
    ordine = 0
    fine = len(num)
    inizio = fine - 3
    risultato = ''
    while ordine < len(num) / 3: # ogni 3 cifre prese aumenta l'ordine di grandezza
        parziale = conv_cent(num[inizio:fine])
        if parziale != '':
            if parziale == 'uno' and ordine > 1:
                risultato = 'un' + ordini_singolari[ordine] + risultato
            elif parziale == 'uno' and ordine == 1:
                risultato = ordini_singolari[ordine] + risultato # mille
            else:
                risultato = parziale + ordini[ordine] + risultato
        ordine += 1
        inizio -= 3
        fine -= 3
    return risultato


# i = 1000
# print(str(i) + ": " + conv(i))
