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
def convertiUnita(n):
    numeriLettereUnita = {1 : "uno", 2 : "due", 3 : "tre", 4: "quattro", 5 : "cinque", 6 : "sei", 7 : "sette", 8: "otto", 9 : "nove"}
    if (n in numeriLettereUnita):
        return numeriLettereUnita[n]
    else:
        return ""


def convertiDecine(n, elisione=False):
    numeriLettereDecine = {2 : "venti", 3 : "trenta", 4 : "quaranta", 5 : "cinquanta", 6 : "sessanta", 7 : "settanta", 8 : "ottanta", 9 : "novanta"}
    if (n in numeriLettereDecine):
        if (elisione):
            return numeriLettereDecine[n][0:-1]
        else:
            return numeriLettereDecine[n]
        
    else:
        return ""
    

def convertiDal10A19(n):
    numeriLettereTraDieciEVenti = {10 : "dieci", 11 : "undici", 12 : "dodici", 13 : "tredici", 14 : "quattordici", 15 : "quindici", 16 : "sedici", 17 : "diciassette", 18 : "diciotto", 19 : "diciannove"}
    if (n in numeriLettereTraDieciEVenti):
        return numeriLettereTraDieciEVenti[n]
    else:
        return ""


def convertiCentinaia(n, elisione=False):
    
    stringaDaRitornare=""
    if (n==0):
        return ""
    elif (n>1):
        stringaDaRitornare = convertiUnita(n)
    
    stringaDaRitornare += "cento"
    
    if (elisione):
        return stringaDaRitornare[0:-1]
    else:
        return stringaDaRitornare
  
    
def converti0_999(n):
    
    decineEUnita = n % 100
    elisione80 = ((decineEUnita//10)==8)
    
    stringaDaRitornare = convertiCentinaia(n//100, elisione80)

    if (10 <= decineEUnita < 20):
        stringaDaRitornare += convertiDal10A19(decineEUnita)
    else:
        elisione=((decineEUnita % 10) == 1) or ((decineEUnita % 10) == 8)
        stringaDaRitornare += convertiDecine(decineEUnita//10, elisione)
        
        stringaDaRitornare += convertiUnita(decineEUnita % 10)
        
    return stringaDaRitornare


   
def conv(n):
    stringaDaRitornare=""

    dict1 = {0:"miliardi", 1:"milioni", 2:"mila"}
    dict2 = {0:"unmiliardo", 1:"unmilione", 2:"mille"}
    
    slasher = 1000000000
    for i in range(0,3):
        testoneAttuale = n//slasher
        if (testoneAttuale > 1):
            stringaDaRitornare += converti0_999(testoneAttuale)
            stringaDaRitornare += dict1[i]
        elif (testoneAttuale == 1):
            stringaDaRitornare += dict2[i]
        n=n % slasher
        slasher = slasher//1000
        
    n=n % 1000
    stringaDaRitornare += converti0_999(n)
    
    return stringaDaRitornare    
   
     


