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
import math

def conv(n):
    simple = ["uno", "due", "tre", "quatro", "cinque", "sei", "sette", "otto", "nove", "dieci",
              "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette",
              "diciotto", "dicianove"]
    #dictionary for doubles. 0 and 1 are added to avoid errors during a loop
    dhjetshet = { 0: "",1: "", 2 : "venti", 3: "trenta", 4:"quaranta",5:"cinquanta", 6:"sessanta",
              7:"settanta", 8:"ottanta",9: "novanta"}
    #1 is empty because cento is right after the first number
    tripp = {1:"", 2:"mila", 3: "milioni", 4: "miliardi", 5: "biliardi"}

    digits = len(str(n)) #find how long is the number
    tripples = math.ceil(digits/3) #calc how many block of 3 we have
    word = []
    # for example 234 534 876
    tempNum = n
    #3 tripples: (234) (534) (876)
    for tipple in reversed(range(1, tripples+1)):
        divider = 10**(3*(tipple-1)) #depends from the tripple 3, 2, 1
        num = tempNum // divider #take each tripple ex: (234)
        tempNum = tempNum % divider #becomes 534 876
        max = len(str(num))+1 #3
        first = 0
        second = 0
        third = 0
        print("Number: ", num)
        mille = False
        printThirdNum = True  # we dont print third number in case of 117, 213 bc 17 and 13 are simple numbers
        for i in reversed(range(1, max)):
            pjs = 10**(i-1) #calculate divider of 234 i=3 => pjs = 100
            if i is 3:
                first = num//pjs #2
            if i is 2:
                num = num%(pjs*10)
                second = num//pjs #3
            if i is 1:
                num = num % (pjs * 10)
                third = num//pjs #4
        print(first, " - ", second, " - ", third)
        #here goes the logic of the checks based on the rules of numbers
        #Checks for first
        if first is not 0:
            if first is not 1:
                word.append(simple[first - 1])
            if second is 8:
                word.append("cent")
            else:
                word.append("cento")
        #Checks for second
        if second is not 0:
            if second is 1:
                word.append(simple[10+third-1])
                printThirdNum = False
            else:
                if third is 1 or third is 8:
                    d = dhjetshet[second]
                    word.append(d[:-1])
                else:
                    word.append(dhjetshet[second])
        if third is not 0:
            if printThirdNum:
                if third is not 1 or second is not 0 or first is not 0:
                    word.append(simple[third - 1])
                else:
                    mille = True
        if tipple is not 1:
            if tipple is 2 and mille is True:
                word.append("mille")
            else:
                word.append(tripp[tipple])
    word = ''.join(str(num) for num in word) #joins elements of the array using ''
    print(word)
    return word
