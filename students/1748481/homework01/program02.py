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
    'Scrivete qui il codice della funzione'
    ok=0
    numero_conv=""
    lc=[] #lista contenente i numeri convertiti in intero
    k=0
    numero_dipartenza= str(n) #ho convertito il numero di partenza in stringa per poter lavorare con le singole cifre
    listacifre=list(numero_dipartenza)
    for elemento in listacifre: #converti gli elementi da stringhe a interi
        lc.append(int(elemento))
    lc=indici3(lc)
    lunghezza = len(lc)

    da1a20=['','uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici', 'tredici','quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    da10a20=['dieci', 'undici', 'dodici', 'tredici','quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    unita=['','','due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
    decine=['', '', 'vent', 'trent', 'quarant', 'cinquant', 'sessant', 'settant', 'ottant', 'novant']
    per_ogni_tripla=['miliardi', 'milioni', 'mila', '']

    if lunghezza/3==4:
        k=12
    elif lunghezza/3==3:
        k=9
    elif lunghezza/3==2:
        k=6
    elif lunghezza/3==1:
        k=3
    for i in range (len(lc)):
        if i%3==0: #ordine dei centinaia
            if lc[i]==0:
                pass
            elif lc[i]==1:
                numero_conv+=""
                numero_conv+="cento"
            elif 1<lc[i]<10:
                numero_conv+=unita[lc[i]]
                numero_conv+="cento"
        if int(i%3)==1: #ordine delle decine
            if n<20:
                numero_conv+=da1a20[n] #il numero viene associato all'lc della lista da1a20 con indice n, cioè il numero
            else:
                if lc[i]==0:
                    if lc[i+1]==1 and lc[i-1]==0:
                        ok=1
                    else:
                        numero_conv += da1a20[lc[i+1]]
                elif lc[i]==1:
                    numero_conv+=da10a20[lc[i+1]]
                elif lc[i]==2:
                    numero_conv+="vent"
                    if lc[i+1]==0:
                        numero_conv+="i"
                    elif lc[i+1]==1:
                        numero_conv+="uno"
                    elif lc[i+1]==8:
                        numero_conv+="otto"
                    else:
                        numero_conv+='i'+da1a20[lc[i]] #inserisco il rispettivo verbale dell'indice da una nuova lista
                elif lc[i]==8:
                    if lc[i-1]!=0:
                        numero_conv+="ttant"
                    else:
                        numero_conv +="ottant"
                    if lc[i+1]==0:
                        numero_conv+="a"
                    elif lc[i+1]==1:
                        numero_conv+="uno"
                    elif lc[i+1]==8:
                        numero_conv+="otto"
                else:
                    numero_conv+=decine[lc[i]]
                    if lc[i+1]==0:
                        numero_conv+="a"
                    elif lc[i+1]==1:
                        numero_conv+="uno"
                    elif lc[i+1]==8:
                        numero_conv+="otto"
                    else:
                        numero_conv+="a"+da1a20[lc[i]]
        if k==10:
            if ok==1:
                numero_conv+="un miliardo"
            else:
                numero_conv+=per_ogni_tripla[0]
            k -= 1
        elif k==7:
            if ok==1:
                numero_conv+="un milione"
            else:
                numero_conv+=per_ogni_tripla[1]
            k -= 1
        elif k==4:
            if ok==1:
                numero_conv+="mille"
            else:
                numero_conv+=per_ogni_tripla[2]
            k-= 1
        elif k==0:
            break
        else:
            k-=1
    print (numero_conv)
    return (numero_conv)

def indici3(lc): #funzione che aumenta la lunghezza della lista fino a che la sua lunghezza/3 da resto 0
    while len(lc)%3!=0:
        lc.insert(0, 0)
    return (lc)

'''devo cercare di dividere il numero in una lista di cifre, in modo tale da
poter gestire il numero in triple. la tripla meno significativa sarà nell'ordine
delle centinaia, la seconda tripla nell'ordine delle migliaia (considerando che
arriviamo ai centomila etc) la seconda tripla dei milioni e l'ultima nelle migliaia.
ogni tripla è divisa in centinaia, decine e unità.'''
