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

numeri_lettere = {
        1: "uno",
        2: "due",
        3: "tre",
        4: "quattro",
        5: "cinque",
        6: "sei",
        7: "sette",
        8: "otto",
        9: "nove",
        10: "dieci",
        11: "undici",
        12: "dodici",
        13: "tredici",
        14: "quattordici",
        15: "quindici",
        16: "sedici",
        17: "diciassette",
        18: "diciotto",
        19: "diciannove",
        20: "venti",
        30: "trenta",
        40: "quaranta",
        50: "cinquanta",
        60: "sessanta",
        70: "settanta",
        80: "ottanta",
        90: "novanta",
        100: "cento",
        1000: "mille",
        1000000: "milione",
        1000000000: "miliardo"
        }

def elisione_uno_otto(stringa, i, pot_cp, ris, val):
    stringa_ap = numeri_lettere[int(stringa[i])*pot_cp] +val
    return stringa_ap[:len(stringa_ap)-1] +ris

def converti_prime_cifre_0pos(stringa, i, pot, ris):
    if i == len(stringa)-1 and int(stringa[i]) != 0:
        if len(stringa) == 1:
            ris = str(numeri_lettere[int(stringa[i])*pot]) +ris
        elif int(stringa[i-1]) != 1:
            ris = str(numeri_lettere[int(stringa[i])*pot]) +ris
    ris = converti_prime_cifre_1pos(stringa, i, pot, ris)
    ris = converti_prime_cifre_2pos(stringa, i, pot, ris)
    return ris
    
def converti_prime_cifre_1pos(stringa, i, pot, ris):
    if i == len(stringa)-2 and int(stringa[i]) != 0:
        if int(stringa[i]) == 1:
            ris = str(numeri_lettere[int(stringa[i]+stringa[i+1])]) +ris
        elif (int(stringa[i+1]) == 1 or int(stringa[i+1]) == 8):
            ris = elisione_uno_otto(stringa, i, pot, ris, '')
        else:
            ris = str(numeri_lettere[int(stringa[i])*pot]) +ris
    return ris

def converti_prime_cifre_2pos(stringa, i, pot, ris):
    if i == len(stringa)-3 and int(stringa[i]) != 0:
        pot_cp = pot/100
        if int(stringa[i]) == 1:
            ris = "cento" +ris
        elif int(stringa[i+1]) == 8:
            stringa_ap = numeri_lettere[int(stringa[i])*pot_cp]
            ris = stringa_ap +"cent" +ris
        else:
            ris = str(numeri_lettere[int(stringa[i])*pot_cp]) +"cento" +ris
    return ris

def converti_numero_0pos(stringa, i, pot, ris, pos, div_pot, val1, val2, val3, val4):
    if i == len(stringa)-pos and int(stringa[i]) != 0:
        pot_cp = pot/div_pot
        if int(stringa[i]) == 1 and len(stringa) == pos:
            ris = val1 +ris
        else:
            ris = converti_numero_0pos1(stringa, i, pot_cp, ris, pos, val2)
    ris = converti_numero_1pos(stringa, i, pot, ris, pos, div_pot, val2, val3, val4)
    ris = converti_numero_2pos(stringa, i, pot, ris, pos, div_pot, val3, val4)
    return ris

def converti_numero_0pos1(stringa, i, pot_cp, ris, pos, val2):
    if int(stringa[i]) != 1 and len(stringa) == pos:
        ris = str(numeri_lettere[int(stringa[i])*pot_cp]) +val2 +ris
    elif int(stringa[i-1]) != 1:
        ris = str(numeri_lettere[int(stringa[i])*pot_cp]) +val2 +ris
    return ris

def converti_numero_1pos(stringa, i, pot, ris, pos, div_pot, val2, val3, val4):
    if i == len(stringa)-(pos+1) and int(stringa[i]) != 0:
        pot_cp = pot/div_pot
        if int(stringa[i+1]) == 0:
            ris = str(numeri_lettere[int(stringa[i])*pot_cp]) +val2 +ris
        else:
            ris = converti_numero_1pos1(stringa, i, pot_cp, ris, pos, val2)
    return ris

def converti_numero_1pos1(stringa, i, pot_cp, ris, pos, val2):
    if int(stringa[i]) == 1:
        ris = str(numeri_lettere[int(stringa[i]+stringa[i+1])]) +val2 +ris
    elif int(stringa[i+1]) == 1 or int(stringa[i+1]) == 8:
        ris = elisione_uno_otto(stringa, i, pot_cp, ris, '')
    else:
        ris = str(numeri_lettere[int(stringa[i])*pot_cp]) +ris
    return ris

def converti_numero_2pos(stringa, i, pot, ris, pos, div_pot, val3, val4):
    if i == len(stringa)-(pos+2) and int(stringa[i]) != 0:
        pot_cp = pot/(div_pot*100)
        if int(stringa[i]) == 1 and int(stringa[i+1]) == 0 and int(stringa[i+2]) == 0:
            ris = val3 +ris
        else:
            ris = converti_numero_2pos1(stringa, i, pot_cp, ris, pos, val3, val4)
    return ris

def converti_numero_2pos1(stringa, i, pot_cp, ris, pos, val3, val4):
    if int(stringa[i]) != 1 and int(stringa[i+1]) != 0 and int(stringa[i+2]) != 0:
        if  (int(stringa[i+1]) == 1 or int(stringa[i+1]) == 8):
            ris = elisione_uno_otto(stringa, i, pot_cp, ris, val4)
        else:
            ris = str(numeri_lettere[int(stringa[i])*pot_cp]) +val4 +ris
    else:
        ris = converti_numero_2pos2(stringa, i, pot_cp, ris, pos, val3, val4)
    return ris

def converti_numero_2pos2(stringa, i, pot_cp, ris, pos, val3, val4):
    if int(stringa[i]) == 1 and int(stringa[i+1]) != 0 and int(stringa[i+1]) != 0:
        ris = val4 +ris
    elif int(stringa[i]) != 1 and (int(stringa[i+1]) != 0 or int(stringa[i+2]) != 0):
        ris = str(numeri_lettere[int(stringa[i])*pot_cp]) +val4 +ris
    else:
        if int(stringa[i]) == 1:
            ris = val4 +ris
        else:
            ris = str(numeri_lettere[int(stringa[i])*pot_cp]) +val3 +ris
    return ris

def conv(n):
    '''trasformare un numero nel formato a parole'''
    ris = ''
    stringa = str(n)
    pot = 1
    for i in range(len(stringa)-1, -1, -1):
        if i >= len(stringa)-3:
            ris = converti_prime_cifre_0pos(stringa, i, pot, ris)
        else:
            ris = converti_numero_0pos(stringa, i, pot, ris, 4, 1000, "mille", "mila", "centomila", "cento")
            ris = converti_numero_0pos(stringa, i, pot, ris, 7, 1000000, "unmilione", "milioni", "centomilioni", "cento")
            ris = converti_numero_0pos(stringa, i, pot, ris, 10, 1000000000, "unmiliardo", "miliardi", "centomiliardi", "cento")
        pot *= 10
    return ris