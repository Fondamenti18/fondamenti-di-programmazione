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


Scrivere una funzione conv(n) che prende in input un intero n, con 000 000 000 0 00, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


unoVenti = ["","uno","due","tre","quattro","cinque","sei","sette","otto","nove","dieci","undici","dodici","tredici","quattordici","quindici","sedici","diciassette","diciotto","diciannove"]
ventiCento = ["","","venti","trenta","quaranta","cinquanta","sessanta","settanta","ottanta","novanta"]
posizioni = [1,2,5,8]
vocali = ["a","e","i","o","u"]
nomi = ["unmiliardo","miliardi","unmilione","milioni","mille","mila","cento","cento"]

def conv(n):

    stringa = str(n)[::-1]

    nuovaStringa = ""

    for i in range(12):

        if i < len(stringa):
            nuovaStringa += stringa[i]
        else:            
            nuovaStringa += "-"

        if i in posizioni:
            nuovaStringa += " "

                    
    nuovaStringa = nuovaStringa.split()
    nuovaStringa.reverse()

    for i in range(len(nuovaStringa)):
        nuovaStringa[i] = nuovaStringa[i][::-1]

    stringaFinale = ""

    for i in range(4):
        stringaFinale += potenze(nuovaStringa[i],nomi[(i + 1) * 2 - 2],nomi[(i + 1) * 2 - 1])

    stringaFinale += decina(nuovaStringa[-1])
    
    i = stringaFinale.find("centoottant")
    
    while i != -1:
        stringaFinale = stringaFinale[:i + 4] + stringaFinale[i + 5:]
        i = stringaFinale.find("centoottant")

    return stringaFinale


def decina(n):

    n = CheckNull(n)
    if n == "":
        return n

    if(n < 20):
        return unoVenti[n]

    if(100 > n >= 20):

        unita = n % 10
        decina = (n - unita) // 10
    
        if(unita == 0):
            return ventiCento[decina]
        else:
            stringaDecina = ventiCento[decina]

            if(stringaDecina[-1] in vocali and unoVenti[unita][0] in vocali):
            	return stringaDecina[:-1] + unoVenti[unita]
            else:
            	return stringaDecina + unoVenti[unita]


def CheckNull(string):
    if(string == "---" or string == "-"):
        return ""
    else:
        return int(string.replace("-",""))


def potenze(n,singolare,plurale):

    n = CheckNull(n)

    if n == "" or n == 0:
        return ""

    if(n > 1):
        return conv(n) + plurale
    else:
        return singolare

