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
#prende numero stringato, converte nella parola corrispondente e la restituisce
def leggiUnita(x):
    lista=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    return lista[int(x)]

def leggiDecineParticolari(x):
    diz={10:'dieci',11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici',16:'sedici',17:'diciassette',18:'diciotto',19:'diciannove'}
    return diz[int(x)]

def leggiDecine(x):
    diz={2:'venti',3:'trenta',4:'quaranta',5:'cinquanta',6:'sessanta',7:'settanta',8:'ottanta',9:'novanta'}
    return diz[int(x)]


def trasformaNumero(x):
    lista=[]
    for carattere in str(x):
        lista.append(carattere)
    return lista

def conv(n):
    listaDiCaratteri = trasformaNumero(n)
    listaDiCaratteri.reverse()
    listaReversed=listaDiCaratteri
    posizione = 0
    stringaParziale = ''
    for numero in listaReversed:

        # gestione unità
        if posizione==0:
            stringaParziale = leggiUnita(listaReversed[posizione])
            posizione += 1

        # gestione decine
        elif posizione == 1:
            # caso 0
            if listaReversed[posizione] == '0':
                posizione = posizione + 1

            else:
                if listaReversed[1] == '1':
                    stringaParziale = leggiDecineParticolari(listaReversed[1]+listaReversed[0])
                else:
                    if listaReversed[0] == '1' or listaReversed[0] == '8':
                        stringaParziale = leggiDecine(listaReversed[1])[:-1]
                    else:
                        stringaParziale = leggiDecine(listaReversed[1]) + stringaParziale
                posizione += 1

        # gestione centinaia
        elif posizione == 2:
            # caso 0
            if listaReversed[posizione] == '0':
                posizione = posizione + 1
            elif listaReversed[2] == '1':
                if listaReversed[1] == '8':
                    stringaParziale = 'cent' + stringaParziale
                    posizione = posizione + 1
                else:
                    stringaParziale = 'cento' + stringaParziale
                    posizione = posizione + 1
            elif listaReversed[1] == '8':
                stringaParziale = leggiUnita(listaReversed[2]) + 'cent' + stringaParziale
                posizione = posizione + 1
            else:
                stringaParziale = leggiUnita(listaReversed[2]) + 'cento' + stringaParziale
                posizione = posizione + 1

        # gestione unita di migliaia
        elif posizione == 3:

            # caso 0
            if listaReversed[posizione] == '0':
                posizione = posizione + 1
            elif listaReversed[3] == '1':
                stringaParziale = 'mille' + stringaParziale
                posizione += 1
            else:
                stringaParziale == leggiUnita(listaReversed[3]) + 'mila' + stringaParziale
                posizione += 1

        # gestione decine di migliaia
        elif posizione == 4:
            # caso 0
            if listaReversed[posizione] == '0':
                posizione = posizione + 1
            elif listaReversed[4] == '1':
                stringaParziale == leggiDecineParticolari(listaReversed[4]+listaReversed[3]) + 'mila'
                posizione += 1
            elif listaReversed[3] == '1':
                stringaParziale = leggiDecine(listaReversed[4])[:-1] + 'unmila' + stringaParziale[5:]
                posizione += 1
            elif listaReversed[3] == '8':
                stringaParziale = leggiDecine(listaReversed[4])[:-1] + 'mila' + stringaParziale
                posizione += 1

            else:
                stringaParziale == leggiDecine(listaReversed[4]) + 'mila' + stringaParziale
                posizione += 1


        # gestione centinaia di migliaia
        elif posizione == 5:
            # caso 0
            if listaReversed[posizione] == '0':
                posizione = posizione + 1
            elif listaReversed[5] == '1':
                if listaReversed[4] == '8':
                    stringaParziale = 'cent' + stringaParziale
                    posizione = posizione + 1
                else:
                    stringaParziale = 'cento' + stringaParziale
                    posizione = posizione + 1
            elif listaReversed[4] == '8':
                stringaParziale = leggiUnita(listaReversed[5])[:-1] + stringaParziale
                posizione = posizione + 1
            else:
                stringaParziale == leggiUnita(listaReversed[5]) + stringaParziale
                posizione = posizione + 1

        # gestione unità di milione
        elif posizione == 6:

            # caso 0
            if listaReversed[posizione] == '0':
                posizione = posizione + 1
            else:

                if listaReversed[6] == '1':
                    stringaParziale = 'unmilione' + stringaParziale
                else:
                    stringaParziale == leggiUnita(listaReversed[6]) + stringaParziale
                posizione += 1

        # gestione
        elif posizione == 7:
            if listaReversed[7] == '1':
                stringaParziale == leggiDecineParticolari(listaReversed[7]+listaReversed[6])
            else:
                stringaParziale == leggiDecine(listaReversed[7])
    return(stringaParziale)


