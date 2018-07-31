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


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1 000 000 000 000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''
#gestione diretta numeri

def set_0_9 (nStr):
    arr_0_9 = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
    return arr_0_9[int(nStr)]

def set_10_19 (nStr):
    arr_10_19 = ['dieci', 'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    return arr_10_19[int(nStr[1])] 

def set_20_99 (nStr):
    arr_20_90 = [0, 0, 'venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta']
    if(nStr[1] == '0'):
        return arr_20_90[int(nStr[0])]
    elif(nStr[1] == '1' or nStr[1] == '8'): #caso di elisione
        return arr_20_90[int(nStr[0])][:-1] + set_0_9(int(nStr[1]))
    else:
        return arr_20_90[int(nStr[0])] + set_0_9(int(nStr[1]))

def set_100_900 (nStr):
    pref = 'cento'
    if nStr[0] == '1':
        return pref
    else:
        return set_0_9(nStr) + pref

#gestione tipologia numeri

def setU (nStr):
    return set_0_9(nStr)

def setD (nStr):
    n = int(nStr)
    if(n >= 10 and n <= 19):
        return set_10_19(nStr)
    else:
        return set_20_99(nStr)

def setC(nStr):
    n = ''
    if(int(nStr[0]) >= 1):
        n = set_100_900(nStr[0])
    if(int(nStr[1]) >= 1):
        if(int(nStr[1]) == 8): #caso di elisione
            n = n[:-1]
            n += setD( (nStr[1]+nStr[2]) )
        else:
            n += setD( (nStr[1]+nStr[2]) )
    elif(int(nStr[2]) >= 1):
        n+= setU(nStr[2])
    return n
    
def setUDC (nStr):    
    if(len(nStr) == 1):
        return setU(nStr)
    elif(len(nStr) == 2):
        return setD(nStr)
    else:
        return setC(nStr)
            
def conv(n):
    'Scrivete qui il codice della funzione'
    ns = str(n)
    nsLen = len(ns)
    
    i = nsLen-1
    arrN = []
    finalN = []
    while i >= 0: #scorro tutti i numeri
        currentN = ''
        while (len(currentN) < 3 and i >=0): #scorro i numeri a gruppi di tre
            if (i >= 0):
                currentN+=ns[i]
                i-=1
        currentN = currentN[::-1] #inverte la stringa
        currentNStr = setUDC(currentN)
        arrN.append(currentN)
        if(currentNStr != '' and len(arrN) > 1): #verifico che non abbia un numero nullo (0) e stia oltre le centinaia
            if len(arrN) == 2:
                if currentNStr == 'uno':
                    currentNStr = 'mille'
                else:
                    currentNStr+= 'mila'
            elif len(arrN) == 3:
                if currentNStr == 'uno':
                    currentNStr = 'unmilione'
                else:
                    currentNStr+= 'milioni'
            elif len(arrN) == 4:
                if currentNStr == 'uno':
                    currentNStr = 'unmiliardo'
                else:
                    currentNStr+= 'miliardi'
        finalN.append(currentNStr)
    
    finalStr = ''
    for i in range(0, len(finalN)):
        finalStr = finalN[i] + finalStr
    
    return finalStr