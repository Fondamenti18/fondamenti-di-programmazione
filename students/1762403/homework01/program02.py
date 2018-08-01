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
    stringa = str(n)
    sottoStr = dividiCifra(stringa)
    sottoLet = []
    sufPlur = ['', 'mila', 'milioni', 'miliardi']
    sufSing = ['', 'mille', 'milione', 'miliardo']
    finale = ''
    for num in sottoStr:
        sottoLet.append(numToLett(num))
        
    for i in range(len(sottoLet)):
        indice = ((len(sottoLet) - 1) - i)
        if(int(sottoStr[i]) == 1):
            finale += sufSing[indice]
        else:
            finale += sottoLet[i] + sufPlur[indice]
    return finale
        
    
    
def dividiCifra(stringa):
    #DETERMINO INTERVALLI
    numIntFuoriIntervalli = len(stringa)%3
    if(numIntFuoriIntervalli == 2):
        intervalli = (round(len(stringa)/3)) - 1
    else:
        intervalli = round(len(stringa)/3)

    #DIVIDO LA CIFRA
    numLst = []
    if(intervalli == 0):
        numLst.append(stringa)
    elif(intervalli == 1 and numIntFuoriIntervalli == 0):
        numLst.append(stringa)
    else:
        if(numIntFuoriIntervalli != 0):
            numLst.append(stringa[:numIntFuoriIntervalli])
            
        for i in range(intervalli):
            indStart = ((numIntFuoriIntervalli) + (i*3))
            indEnd = indStart + 3
            numLst += [stringa[indStart:indEnd]]
    return numLst


def numToLett(stringa):
    lstStr = []
    unita = ['uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
    decine = ['dieci', 'venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta']
    decineIrregolari = ['undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    centinaia = ['cento', 'duecento', 'trecento', 'quattrocento', 'cinquecento', 'seicento', 'settecento', 'ottocento', 'novecento']
    if(len(stringa) == 1):
        numUni = int(stringa[0])
    elif(len(stringa) == 2):
        numUni = int(stringa[1])
        numDec = int(stringa[0])
    else:
        numUni = int(stringa[2])
        numDec = int(stringa[1])
        numCen = int(stringa[0])
    
    if(len(stringa) == 3):
        #Sistemo le centinaia
        if(numDec != 8 and numCen != 0):
            lstStr.append(centinaia[numCen - 1])
        elif(numCen != 0):
            ausiliaria = centinaia[numCen - 1]
            lstStr.append(ausiliaria[:len(ausiliaria)-1])
        #Sistemo le decine
        if(numDec == 1 and numUni != 0):
            lstStr.append(decineIrregolari[numUni - 1])
        elif(numDec == 1 and numUni == 0):
            lstStr.append(decine[numDec - 1])
        elif(numDec == 0 and numUni != 0):
            #Sistemo le unità
            lstStr.append(unita[numUni - 1])
        else:
            if(numUni != 1 and numUni != 8):
                lstStr.append(decine[numDec - 1])
            else:
                ausiliaria = decine[numDec - 1]
                lstStr.append(ausiliaria[:len(ausiliaria)-1])
            #Sistemo le unità
            lstStr.append(unita[numUni - 1])
    elif(len(stringa) > 1):
        #Sistemo le decine
        if(numDec == 1 and numUni != 0):
            lstStr.append(decineIrregolari[numUni - 1])
        elif(numDec == 1 and numUni == 0):
            lstStr.append(decine[numDec - 1])
        elif(numDec == 0 and numUni != 0):
            #Sistemo le unità
            lstStr.append(unita[numUni - 1])
        else:
            if(numUni != 1 and numUni != 8):
                lstStr.append(decine[numDec - 1])
            else:
                ausiliaria = decine[numDec - 1]
                lstStr.append(ausiliaria[:len(ausiliaria)-1])
            #Sistemo le unità
            lstStr.append(unita[numUni - 1])
    else:
        #Sistemo le unità
        lstStr.append(unita[numUni - 1])
    
    stringaFinale = ''.join(lstStr)
    return stringaFinale
