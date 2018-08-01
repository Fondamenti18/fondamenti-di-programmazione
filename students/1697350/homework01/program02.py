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

'''
Caro prof, le chiedo scusa se il codice e' inguardabile... pero' mi capisca, avevo dei progetti da consegnare al lavoro quindi non ho potuto
fare un refactor decente...
'''
def decine(dictNumeri, n):
    if int(n) >= 20 and int(n) <= 99:
        secondNumber = str(n)[1:]
        firstNumber = str(n)[:-1] + str(0)
        for key, val in dictNumeri.items():
            if n in dictNumeri:
                finalNumber = dictNumeri[n]
                return finalNumber
            if key == int(firstNumber):
                if int(secondNumber) == 1 or int(secondNumber) == 8:
                    finalNumber = dictNumeri[key][:-1] + dictNumeri[int(secondNumber)]
                    return finalNumber
                else:
                    if int(secondNumber) == 0:
                        
                        finalNumber = dictNumeri[key]
                        return finalNumber
                    else:
                        finalNumber = dictNumeri[key] + dictNumeri[int(secondNumber)]
                        return finalNumber
    else:
        finalNumber = dictNumeri[int(n)]
        return finalNumber
                    

def centinaia(dictNumeri, n):
    firstNumber = str(n)[:-2]
    decineNumber = str(n)[1:]
    secondNumber = str(n)[1:][:-1]
    for key, val in dictNumeri.items():
            if n == 100:
                finalNumber = dictNumeri[100]
                return finalNumber
            
            if int(firstNumber) == 0:
                finalNumber = decine(dictNumeri, decineNumber)
                return finalNumber
            
            if decineNumber == '00':
                if int(firstNumber) == 1:
                    finalNumber = dictNumeri[100]
                    return finalNumber
                else:
                        
                    finalNumber = dictNumeri[int(firstNumber)] + dictNumeri[100]
                    return finalNumber
            
            if int(firstNumber) == 0:
                finalNumber = decine(dictNumeri, decineNumber)
                return finalNumber
            
            if int(firstNumber) == 1:
                finalNumber = dictNumeri[100] + decine(dictNumeri, decineNumber)
                return finalNumber
            else:
                if int(secondNumber) == 8:
                    finalNumber = dictNumeri[int(firstNumber)] + dictNumeri[100] + decine(dictNumeri, decineNumber)[1:]
                    return finalNumber
                else:
                    finalNumber = dictNumeri[int(firstNumber)] + dictNumeri[100] + decine(dictNumeri, decineNumber)
                    return finalNumber
                
            
            
def mila(dictNumeri, n):
    firstNumber = str(n)[:-3]
    secondNumber = str(n)[1:][:-1][:-1]
    thirdNumber = str(n)[2:]
    centinaiaNumber = str(n)[1:]
    decineNumber = str(n)[2:]
    variabileMila = 'mila'
    if len(str(n)) == 4:
        for key, val in dictNumeri.items():
            if n == 1000:
                finalNumber = dictNumeri[1000]
                return finalNumber
            
            if int(firstNumber) == 0:
                finalNumber = centinaia(dictNumeri, centinaiaNumber)
                return finalNumber
            
            
            if int(secondNumber) == 0 and thirdNumber == '00':
                finalNumber = dictNumeri[int(firstNumber)] + variabileMila
                return finalNumber
            
            if int(firstNumber) == 0:
                    finalNumber = centinaia(dictNumeri, n)
                    return finalNumber
            
            if int(firstNumber) == 1:
                if int(secondNumber) == 0:
                    finalNumber = dictNumeri[1000] + decine(dictNumeri, decineNumber)
                    return finalNumber
                else:
                    finalNumber = dictNumeri[1000] + centinaia(dictNumeri, centinaiaNumber)
                    return finalNumber
            else:
                if int(secondNumber) == 0:
                    finalNumber = dictNumeri[int(firstNumber)] + variabileMila + decine(dictNumeri, decineNumber)
                    return finalNumber
                else:
                    finalNumber = dictNumeri[int(firstNumber)] + variabileMila + centinaia(dictNumeri, centinaiaNumber)
                    return finalNumber   
            
            
def dieciMila(dictNumeri, n):
    firstNumber = str(n)[:-4]
    firstTwoNumbers = str(n)[:-3]
    centinaiaNumbers = str(n)[2:]
    decineNumbers = str(n)[3:]
    thirdNumber = str(n)[2:][:-2]
    lastNumber = str(n)[4:]
    milaNumbers = str(n)[1:]
    variabileMila = 'mila'
    if len(str(n)) == 5:
        for key, val in dictNumeri.items():

            if milaNumbers == '0000':
                finalNumber = decine(dictNumeri, firstTwoNumbers) + variabileMila
                return finalNumber
            
            if int(firstNumber) == 0:
                finalNumber = mila(dictNumeri, milaNumbers)
                return finalNumber
            
            if centinaiaNumbers == '000':
                finalNumber = decine(dictNumeri, firstTwoNumbers) + variabileMila
                return finalNumber
            
            if decineNumbers == '00':
                finalNumber = decine(dictNumeri, firstTwoNumbers) + variabileMila + centinaia(dictNumeri, centinaiaNumbers)
                return finalNumber
            
            if int(thirdNumber) == 0:
                finalNumber = decine(dictNumeri, firstTwoNumbers) + variabileMila + decine(dictNumeri, decineNumbers)
                return finalNumber
                
            if int(lastNumber) == 0:
                finalNumber = decine(dictNumeri, firstTwoNumbers) + variabileMila + centinaia(dictNumeri, centinaiaNumbers)
                return finalNumber
            else:
                finalNumber = decine(dictNumeri, firstTwoNumbers) + variabileMila + centinaia(dictNumeri, centinaiaNumbers)
                return finalNumber


def centoMila(dictNumeri, n):
    firstNumber = str(n)[:-5]
    dieciMilaNumbers = str(n)[1:]
    thirdNumber = str(n)[2:][:-3]
    milaNumbers = str(n)[2:]
    firstCentinaiaNumbers = str(n)[:-3]
    lastCentinaiaNumbers = str(n)[3:]
    decineNumbers = str(n)[4:]
    lastNumber = str(n)[5:]
    milaDecineNumbers = str(n)[3:][:-1]
    fourthNumber = str(n)[3:][:-2]
    variabileMila = 'mila'
    if len(str(n)) == 6:
        for key, val in dictNumeri.items():
            
            if int(firstNumber) == 0:
                finalNumber = dieciMila(dictNumeri, dieciMilaNumbers)
                return finalNumber
            
            if dieciMilaNumbers == '00000':
                finalNumber = centinaia(dictNumeri, firstCentinaiaNumbers) + variabileMila
                return finalNumber
            
            
            if milaNumbers == '0000':
                finalNumber = centinaia(dictNumeri, firstCentinaiaNumbers) + variabileMila
                return finalNumber
            
            if lastCentinaiaNumbers == '000':
                finalNumber = centinaia(dictNumeri, firstCentinaiaNumbers) + variabileMila
                return finalNumber
                
            if decineNumbers == '00':
                finalNumber = centinaia(dictNumeri, firstCentinaiaNumbers) + variabileMila + centinaia(dictNumeri, lastCentinaiaNumbers)
                return finalNumber    
            
            if milaDecineNumbers == '00':
                finalNumber = centinaia(dictNumeri, firstCentinaiaNumbers) + variabileMila + decine(dictNumeri, decineNumbers)
                return finalNumber
            
            if int(thirdNumber) == 0:
                if int(fourthNumber) == 0 and int(lastNumber) != 0:
                    finalNumber = centinaia(dictNumeri, firstCentinaiaNumbers) + variabileMila + decine(dictNumeri, decineNumbers)
                    return finalNumber
                
                
            else:
                if int(fourthNumber) == 0 and int(lastNumber) != 0:
                    finalNumber = centinaia(dictNumeri, firstCentinaiaNumbers) + variabileMila + decine(dictNumeri, decineNumbers)
                    return finalNumber
                
                finalNumber = centinaia(dictNumeri, firstCentinaiaNumbers) + variabileMila + centinaia(dictNumeri, lastCentinaiaNumbers)
                return finalNumber
            
            if lastNumber == '0':
                finalNumber = centinaia(dictNumeri, firstCentinaiaNumbers) + variabileMila + centinaia(dictNumeri, lastCentinaiaNumbers)
                return finalNumber
            else:
                finalNumber = centinaia(dictNumeri, firstCentinaiaNumbers) + variabileMila + centinaia(dictNumeri, lastCentinaiaNumbers)
                return finalNumber
            
            
def milione(dictNumeri, n):
    variabileMilione = 'milioni'
    if len(str(n)) == 7:
        for key, val in dictNumeri.items():
            
            firstNumber = str(n)[:-6]
            centoMilaNumbers = str(n)[1:]
            decineNumber = str(n)[5:]
            centinaiaNumber = str(n)[4:][:-2]
            centinaiaNumbers = str(n)[4:]
            secondNumber = str(n)[1:][:-5]
            
            if int(firstNumber) == 0:
                finalNumber = centoMila(dictNumeri, centoMilaNumbers)
                return finalNumber
            
            if int(firstNumber) == 1:
                dizionarioMilione = dictNumeri[1000000]
            else:
                dizionarioMilione = dictNumeri[int(firstNumber)] + variabileMilione
                
            if centoMilaNumbers == '000000':
                finalNumber = dictNumeri[1000000]
                return finalNumber
            
            else:
                if int(secondNumber) == 0:
                    finalNumber = dizionarioMilione + centoMila(dictNumeri, centoMilaNumbers)
                    return finalNumber
                else:
                    finalNumber = dizionarioMilione + centoMila(dictNumeri, centoMilaNumbers)
                    return finalNumber
                
                
                if int(centinaiaNumber) == 0:
                    finalNumber = dizionarioMilione + decine(dictNumeri, decineNumber)
                    return finalNumber
                
                else:
                    finalNumber = dizionarioMilione + centinaia(dictNumeri, centinaiaNumbers)
                    return finalNumber
                
                
                if decineNumber == '00':
                    finalNumber = dizionarioMilione + centinaia(dictNumeri, centinaiaNumbers)
                    return finalNumber
                
                else:
                    finalNumber = dizionarioMilione + centoMila(dictNumeri, centoMilaNumbers)
                    return finalNumber
                    
                    
def milaMilioni(dictNumeri, n):
    variabileMilione = 'milioni'
    if len(str(n)) == 8 :
        for key, val in dictNumeri.items():
            firstTwoNumbers = str(n)[:-6]
            milioneNumbers = str(n)[1:]
            firstNumber = str(n)[:-7]
            centoMilaNumbers = str(n)[2:]
            if firstTwoNumbers == '00':
                finalNumber = centoMila(dictNumeri, centoMilaNumbers)
                return finalNumber
            
            if int(firstNumber) == 0:
                finalNumber = milione(dictNumeri, milioneNumbers)
                return finalNumber
            
            if centoMilaNumbers == '000000':
                finalNumber = decine(dictNumeri, firstTwoNumbers) + variabileMilione
                return finalNumber
            else:
                finalNumber = decine(dictNumeri, firstTwoNumbers) + variabileMilione + centoMila(dictNumeri, centoMilaNumbers)
                return finalNumber

def centoMilioni(dictNumeri, n):
    variabileMilione = 'milioni'
    if len(str(n)) == 9 :
        for key, val in dictNumeri.items():
            firstTwoNumbers = str(n)[:-6]
            firstThreeNumbers = str(n)[:-6]
            milioneNumbers = str(n)[1:]
            firstNumber = str(n)[:-8]
            centoMilaNumbers = str(n)[3:]
            milaMilioniNumbers = str(n)[1:]
            if firstTwoNumbers == '00':
                finalNumber = milione(dictNumeri, milioneNumbers)
                return finalNumber
            
            if firstThreeNumbers == '000':
                finalNumber = centoMila(dictNumeri, centoMilaNumbers)
                return finalNumber
            
            if int(firstNumber) == 0:
                finalNumber = milaMilioni(dictNumeri, milaMilioniNumbers)
                return finalNumber
            
            if centoMilaNumbers == '000000':
                finalNumber = centinaia(dictNumeri, firstThreeNumbers) + variabileMilione
                return finalNumber
            else:
                finalNumber = centinaia(dictNumeri, firstThreeNumbers) + variabileMilione + centoMila(dictNumeri, centoMilaNumbers)
                return finalNumber
            
            
def miliardo(dictNumeri, n):
    variabileMiliardo = 'miliardi'
    if len(str(n)) == 10 :
        for key, val in dictNumeri.items():
            firstTwoNumbers = str(n)[:-8]
            firstNumber = str(n)[:-9]
            centoMilioniNumbers = str(n)[1:]
            if centoMilioniNumbers == '000000000':
                if int(firstNumber) == 1:
                    finalNumber = dictNumeri[1000000000]
                    return finalNumber   
                else:
                    finalNumber = dictNumeri[int(firstNumber)] + variabileMiliardo
                    return finalNumber 
                
            if int(firstNumber) == 1:
                dizionarioMiliardo = dictNumeri[1000000000] + centoMilioni(dictNumeri, centoMilioniNumbers)
            else:
                dizionarioMiliardo = dictNumeri[int(firstNumber)] + variabileMiliardo + centoMilioni(dictNumeri, centoMilioniNumbers)

            
            if firstTwoNumbers == '00':
                finalNumber = centoMilioni(dictNumeri, centoMilioniNumbers)
                return finalNumber
            
            
            if int(firstNumber) == 0:
                finalNumber = centoMilioni(dictNumeri, centoMilioniNumbers)
                return finalNumber
            else:
                finalNumber = dizionarioMiliardo
                return finalNumber
            
def dieciMiliardi(dictNumeri, n):
    variabileMiliardo = 'miliardi'
    if len(str(n)) == 11 :
        for key, val in dictNumeri.items():
            firstTwoNumbers = str(n)[:-9]
            firstNumber = str(n)[:-10]
            centoMilaNumbers = str(n)[2:]
            centoMilioniNumbers = str(n)[2:]
            miliardoNumbers = str(n)[1:]
            
            if centoMilaNumbers == '000000000':
                finalNumber = decine(dictNumeri, firstTwoNumbers) + variabileMiliardo
                return finalNumber
            else:
                finalNumber = decine(dictNumeri, firstTwoNumbers) + variabileMiliardo + centoMilioni(dictNumeri, centoMilioniNumbers)
                return finalNumber
            
            
            if firstTwoNumbers == '00':
                finalNumber = centoMilioni(dictNumeri, centoMilioniNumbers)
                return finalNumber
            
            if int(firstNumber) == 0:
                finalNumber = miliardo(dictNumeri, miliardoNumbers)
                return finalNumber


def centoMiliardi(dictNumeri, n):
    variabileMiliardo = 'miliardi'
    if len(str(n)) == 12 :
        for key, val in dictNumeri.items():
            firstTwoNumbers = str(n)[:-10]
            firstNumber = str(n)[:-11]
            centoMilaNumbers = str(n)[2:]
            miliardoNumbers = str(n)[2:]
            dieciMiliardiNumbers = str(n)[1:]
            firstThreeNumbers = str(n)[:-9]
            centoMilioniNumbers = str(n)[3:]
            
            if firstThreeNumbers == '000':
                finalNumber = centoMilioni(dictNumeri, centoMilioniNumbers)
                return finalNumber
            
            if firstTwoNumbers == '00':
                finalNumber = miliardo(dictNumeri, miliardoNumbers)
                return finalNumber
            
            if int(firstNumber) == 0:
                finalNumber = dieciMiliardi(dictNumeri, dieciMiliardiNumbers)
                return finalNumber
            
            if centoMilaNumbers == '0000000000':
                finalNumber = centinaia(dictNumeri, firstThreeNumbers) + variabileMiliardo
                return finalNumber
            else:
                finalNumber = centinaia(dictNumeri, firstThreeNumbers) + variabileMiliardo + centoMilioni(dictNumeri, centoMilioniNumbers)
                return finalNumber

def biliardo(dictNumeri, n):
    variabileBiliardo = 'biliardi'
    if len(str(n)) == 13 :
        for key, val in dictNumeri.items():
            firstNumber = str(n)[:-12]
            centoMiliardiNumbers = str(n)[1:]
            
            if centoMiliardiNumbers == '000000000000':
                if int(firstNumber) == 1:
                    finalNumber = dictNumeri[1000000000000]
                    return finalNumber   
                else:
                    finalNumber = dictNumeri[int(firstNumber)] + variabileBiliardo
                    return finalNumber 
            
            if int(firstNumber) == 1:
                dizionarioBiliardo = dictNumeri[1000000000000] + centoMiliardi(dictNumeri, centoMiliardiNumbers)
            else:
                dizionarioBiliardo = dictNumeri[int(firstNumber)] + variabileBiliardo + centoMiliardi(dictNumeri, centoMiliardiNumbers)
            
            
            if int(firstNumber) == 0:
                finalNumber = centoMiliardi(dictNumeri, centoMiliardiNumbers)
                return finalNumber
            else:
                finalNumber = dizionarioBiliardo
                return finalNumber
            
           
def conv(n):
    dictNumeri = dict()
    dictNumeri[1] = 'uno'
    dictNumeri[2] = 'due'
    dictNumeri[3] = 'tre'
    dictNumeri[4] = 'quattro'
    dictNumeri[5] = 'cinque'
    dictNumeri[6] = 'sei'
    dictNumeri[7] = 'sette'
    dictNumeri[8] = 'otto'
    dictNumeri[9] = 'nove'
    dictNumeri[10] = 'dieci'
    dictNumeri[11] = 'undici'
    dictNumeri[12] = 'dodici'
    dictNumeri[13] = 'tredici'
    dictNumeri[14] = 'quattordici'
    dictNumeri[15] = 'quindici'
    dictNumeri[16] = 'sedici'
    dictNumeri[17] = 'diciassette'
    dictNumeri[18] = 'diciotto'
    dictNumeri[19] = 'diciannove'
    dictNumeri[20] = 'venti'
    dictNumeri[30] = 'trenta'
    dictNumeri[40] = 'quaranta'
    dictNumeri[50] = 'cinquanta'
    dictNumeri[60] = 'sessanta'
    dictNumeri[70] = 'settanta'
    dictNumeri[80] = 'ottanta'
    dictNumeri[90] = 'novanta'
    dictNumeri[100] = 'cento'
    dictNumeri[1000] = 'mille'
    dictNumeri[1000000] = 'unmilione'
    dictNumeri[1000000000] = 'unmiliardo'
    dictNumeri[1000000000000] = 'unbiliardo'
    
    
    if len(str(n)) == 1:
        return dictNumeri[n]
        
    if len(str(n)) == 2:
        return decine(dictNumeri, n)
        
    if len(str(n)) == 3:
        return centinaia(dictNumeri, n)
    
    if len(str(n)) == 4:
        return mila(dictNumeri, n)
                
    if len(str(n)) == 5:
        return dieciMila(dictNumeri, n)    
        
    if len(str(n)) == 6:
        return centoMila(dictNumeri, n)  
    
    if len(str(n)) == 7:
        return milione(dictNumeri, n)   
        
    if len(str(n)) == 8:
        return milaMilioni(dictNumeri, n)     
    
    if len(str(n)) == 9:
        return centoMilioni(dictNumeri, n)     
    
    if len(str(n)) == 10:
        return miliardo(dictNumeri, n)     
    
    if len(str(n)) == 11:
        return dieciMiliardi(dictNumeri, n)    
    
    if len(str(n)) == 12:
        return centoMiliardi(dictNumeri, n)
    
    if len(str(n)) == 13:
        return biliardo(dictNumeri, n)

