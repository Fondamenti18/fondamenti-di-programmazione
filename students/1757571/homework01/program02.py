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

'''Dizionari utilizzati dalle diverse funzioni'''
particular={"1":"un", "2":"do", "3":"tre", "4":"quattor", "5":"quin", "6":"se", "7":"assette", "8":"otto", "9":"annove"}
firstDigit={"0":"zero", "1":"uno", "2":"due", "3":"tre", "4":"quattro", "5":"cinque", "6":"sei", "7":"sette", "8":"otto", "9":"nove"}
secondDigit={"2":"venti", "3":"trenta", "4":"quaranta", "5":"cinquanta", "6":"sessanta", "7":"settanta", "8":"ottanta", "9":"novanta"}



def gruppoCentinaia(MyNum):
    #Funzione che esprime separatamente numeri rientranti nel gruppo delle centinaia
    NumGroup=len(MyNum)
    #Solo unità
    if NumGroup==1:
        return firstDigit[MyNum]
    #Ordine delle decine
    elif NumGroup==2:
        #Caso particolare
        if MyNum[0]=="0":
            myNewNum=MyNum[1:2]
            return gruppoCentinaia(myNewNum)  
        elif MyNum[0]=="1":
            return partDecine(MyNum)
        #Caso generale
        else:    
            if MyNum[1]!="1" and MyNum[1]!="8" and MyNum[1]!="0":
                return secondDigit[MyNum[0]]+firstDigit[MyNum[1]]
            elif MyNum[1]=="0":
                return secondDigit[MyNum[0]] 
            else:
                myString=secondDigit[MyNum[0]]
                mynewString=myString[:-1]
                return mynewString+firstDigit[MyNum[1]]
    #Ordine delle centinaia
    elif NumGroup==3:
        if MyNum[0]=="0":
            myNewNum=MyNum[1:3]
            return gruppoCentinaia(myNewNum)
        #Caso generale
        if MyNum[0]!="1":
            if MyNum[1:3]=="00":
                return firstDigit[MyNum[0]]+"cento"
            elif MyNum[1]!="1":
                if MyNum[2]!="1" and MyNum[2]!="8" and MyNum[2]!="0":
                    return firstDigit[MyNum[0]]+"cento"+secondDigit[MyNum[1]]+firstDigit[MyNum[2]]
                elif MyNum[2]=="0":
                    return firstDigit[MyNum[0]]+"cento"+secondDigit[MyNum[1]]
                elif MyNum[1]=="0":
                    return firstDigit[MyNum[0]]+"cento"+firstDigit[MyNum[2]]
                elif MyNum[1]=="8":
                    if MyNum[2]=="8" or MyNum[2]=="1":
                        myString=secondDigit[MyNum[1]]
                        mynewString=myString[:-1]
                        return firstDigit[MyNum[0]]+"cent"+mynewString+firstDigit[MyNum[2]]
                    else:
                        return firstDigit[MyNum[0]]+"cent"+secondDigit[MyNum[1]]+firstDigit[MyNum[2]]
                else:
                    myString=secondDigit[MyNum[1]]
                    mynewString=myString[:-1]
                    return firstDigit[MyNum[0]]+"cento"+mynewString+firstDigit[MyNum[2]]
            elif MyNum[1]=="0":
                return firstDigit[MyNum[0]]+"cento"+firstDigit[MyNum[2]]
            elif MyNum[1]=="1":
                return firstDigit[MyNum[0]]+"cento"+partDecine(MyNum[1:3])
        #Caso particolare centinaia
        else:
            if MyNum=="100":
                return "cento"
            elif MyNum[1]=="0":
                return "cento"+firstDigit[MyNum[2]]
            elif MyNum[1]=="8":
                    if MyNum[2]=="8" or MyNum[2]=="1":
                        myString=secondDigit[MyNum[1]]
                        mynewString=myString[:-1]
                        return "cent"+mynewString+firstDigit[MyNum[2]]
                    else:
                        return "cent"+secondDigit[MyNum[1]]+firstDigit[MyNum[2]]
            elif MyNum[1]!="1":
                if MyNum[2]=="0":
                    return "cento"+secondDigit[MyNum[1]]
                elif MyNum[1]=="8" and MyNum[2]=="8":
                    return "cent"+secondDigit[MyNum[1]]+firstDigit[MyNum[2]]
                elif MyNum[2]=="1" or MyNum[2]=="8":
                    myString=secondDigit[MyNum[1]]
                    mynewString=myString[:-1]
                    return "cento"+mynewString+firstDigit[MyNum[2]]
                else:
                    return "cento"+secondDigit[MyNum[1]]+firstDigit[MyNum[2]]
            else:
                return "cento"+partDecine(MyNum[1:3])
                
def partDecine(MyNum):
    #Funzione che gestisce il caso particolare delle decine, ovvero la presenza di un dieci o di un "uno" come decina
    #(il numero in input è già in formato stringa)
    if MyNum=="10":
        return "dieci"
    elif MyNum[1]=="7" or MyNum[1]=="8" or MyNum[1]=="9":
        return "dici"+particular[MyNum[1]]
    else:
        return particular[MyNum[1]]+"dici"
    
def creaCentinaia(myCentinaia):
    #Funziona per creare le suddivisioni in centinaia del numero in input leggendola al contrario
    myNew=''
    for x in reversed(myCentinaia):
        myNew=myNew+x
    return myNew


def conv(n):
    if not 0<n<1000000000000:
        return "Inserisci un numero n valido compreso nell'intervallo"
    MyNum=str(n)
    NumLength=len(MyNum)
    #Ordine delle centinaia
    if 1<=NumLength<=3:
        return gruppoCentinaia(MyNum)
    #Ordine delle migliaia
    #Caso particolare delle migliaia
    elif NumLength==4:
        if MyNum[0]=="1":
            if MyNum[1:]=="000":
                return "mille"
            elif MyNum[1]=="0":
                myNewNum=MyNum[2:5]
                return "mille"+gruppoCentinaia(myNewNum)
            else:
                myNewNum=MyNum[1:5]
                return "mille"+gruppoCentinaia(myNewNum)
        else:
            if MyNum[1:]=="000":
                return firstDigit[MyNum[0]]+"mila"
            if MyNum[1]=="0":
                myNewNum=MyNum[2:5]
                return firstDigit[MyNum[0]]+"mila"+gruppoCentinaia(myNewNum)
            else:
                myNewNum=MyNum[1:5]
                return firstDigit[MyNum[0]]+"mila"+gruppoCentinaia(myNewNum)
    #Caso generale migliaia
    elif 4<NumLength<=6:
        centinaia=MyNum[NumLength:NumLength-4:-1]
        migliaia=MyNum[NumLength-4::-1]
        myMigliaia=creaCentinaia(migliaia)
        myCentinaia=creaCentinaia(centinaia)
        if myCentinaia=="000":
            return gruppoCentinaia(myMigliaia)+"mila"    
        else:
            return gruppoCentinaia(myMigliaia)+"mila"+gruppoCentinaia(myCentinaia)
    #Ordine milioni
    #Caso particolare milioni
    elif NumLength==7:
        centinaia=MyNum[NumLength:NumLength-4:-1]
        migliaia=MyNum[NumLength-4::-1]
        myMigliaia=creaCentinaia(migliaia)
        myCentinaia=creaCentinaia(centinaia)
        if MyNum[0]=="1":
            if MyNum[1:]=="000000":
                return "unmilione"
            else:
                return "unmilione"+gruppoCentinaia(myMigliaia)+"mila"+gruppoCentinaia(myCentinaia)
        else:
            return firstDigit[MyNum[0]]+"milioni"+gruppoCentinaia(myMigliaia)+"mila"+gruppoCentinaia(myCentinaia)
    #Caso generale milioni
    elif 7<NumLength<=9:
        centinaia=MyNum[NumLength:NumLength-4:-1]
        migliaia=MyNum[NumLength-4:NumLength-7:-1]
        milioni=MyNum[NumLength-7::-1]
        myMigliaia=creaCentinaia(migliaia)
        myCentinaia=creaCentinaia(centinaia)
        myMilioni=creaCentinaia(milioni)
        return gruppoCentinaia(myMilioni)+"milioni"+gruppoCentinaia(myMigliaia)+"mila"+gruppoCentinaia(myCentinaia)
    #Ordine miliardi
    #Caso particolare miliardi
    elif NumLength==10:
        centinaia=MyNum[NumLength:NumLength-4:-1]
        migliaia=MyNum[NumLength-4:NumLength-7:-1]
        milioni=MyNum[NumLength-7::-1]
        myMigliaia=creaCentinaia(migliaia)
        myCentinaia=creaCentinaia(centinaia)
        myMilioni=creaCentinaia(milioni)
        if MyNum=="1000000000":
            return "unmiliardo"
        else:
            if MyNum[0]=="1":
                return "unmiliardo"+gruppoCentinaia(myMilioni)+"milioni"+gruppoCentinaia(myMigliaia)+"mila"+gruppoCentinaia(myCentinaia)
            else:
                return firstDigit[MyNum[0]]+"miliardi"+gruppoCentinaia(myMilioni)+"milioni"+gruppoCentinaia(myMigliaia)+"mila"+gruppoCentinaia(myCentinaia)
    #Caso generale miliardi
    elif 10<NumLength<=12:
        centinaia=MyNum[NumLength:NumLength-4:-1]
        migliaia=MyNum[NumLength-4:NumLength-7:-1]
        milioni=MyNum[NumLength-7:NumLength-10:-1]
        miliardi=MyNum[NumLength-10::-1]
        myMigliaia=creaCentinaia(migliaia)
        myCentinaia=creaCentinaia(centinaia)
        myMilioni=creaCentinaia(milioni)
        myMiliardi=creaCentinaia(miliardi)
        return gruppoCentinaia(myMiliardi)+"miliardi"+gruppoCentinaia(myMilioni)+"milioni"+gruppoCentinaia(myMigliaia)+"mila"+gruppoCentinaia(myCentinaia)
        
