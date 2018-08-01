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

units = {
"0" : "",
"1" : "uno",
"2" : "due",
"3" : "tre",
"4" : "quattro",
"5" : "cinque",
"6" : "sei",
"7" : "sette",
"8" : "otto",
"9" : "nove"
}

ten_to_twenty = {
"11" : "undici",
"12" : "dodici",
"13" : "tredici",
"14" : "quattordici",
"15" : "quindici",
"16" : "sedici",
"17" : "diciassette",
"18" : "diciotto",
"19" : "diciannove"
}

dozens = {
"0" : "",
"1" : "dieci",
"2" : "venti",
"3" : "trenta",
"4" : "quaranta",
"5" : "cinquanta",
"6" : "sessanta",
"7" : "settanta",
"8" : "ottanta",
"9" : "novanta"
}
''' converte il numero dato in input in forma letterale'''
def conv(n):
    splitted_n = split(n)
    n_triads = len(splitted_n)
    final_num = ""
    if(n == 1): return "uno"
    for i, triad in enumerate(splitted_n):
        final_num += get_literal_triad(triad) + fix_unit(n_triads - (1+i),triad)
    return final_num

'''ottiene la versione letterale di una terna data in input'''
def get_literal_triad(triad):
    triad_value = ""
    literal_form = ""
    triad = str(triad)
    if(triad == "001"):
        return ""
    for i,digit in enumerate(triad):

        if (i == 0):
            if(digit != "0"):
                literal_form += "cento"
                if(triad[i+1] == "8"):
                    literal_form = literal_form[:-1]
                if(digit != "1"):
                    literal_form = units[digit] + literal_form
            triad_value += literal_form
        literal_form = ""

        if (i == 1):
            next_digit = triad[i+1]
            if(digit == "1"):
                if(next_digit != "0"):
                    literal_form = ten_to_twenty[digit + next_digit]
                else:
                    literal_form = dozens[digit]
            else:
                if(next_digit == "1" or next_digit == "8"):
                    literal_form = dozens[digit][:-1]
                else:
                    literal_form = dozens[digit]
            triad_value += literal_form

        if (i == 2 and triad[i-1] != "1"):
            triad_value += units[digit]
    return triad_value

'''aggiunge l'unita' corretta dopo la parte letterale di triad'''
def fix_unit(triad_index,triad):
    unit = ""
    if(triad_index == 1):
        if(triad == "001"):
            unit = "mille"
        elif(triad != "000"):
            unit =  "mila"
    elif(triad_index == 2):
        if(triad == "001"):
            unit = "unmilione"
        elif(triad != "000"):
            unit = "milioni"
    elif(triad_index == 3):
        if(triad == "001"):
            unit = "unmiliardo"
        elif(triad != "000"):
            unit = "miliardi"

    return unit

'''normalizza la stringa es: input [ 2341 ] -> output [ 002341 ]'''
def normalize(n):
    n = str(n)
    while(len(n) % 3 != 0):
        n = "0" + n
    return n

'''splitta la stringa in terne 4383593484  ---> [004,383,593,484] '''
def split(n):
    n = normalize(n)
    num_ls = []
    k = 0
    num = ""
    for digit in range(len(n)):
        num += n[digit]
        k += 1
        if(k % 3 == 0):
            num_ls.append(num)
            num = ""
    return num_ls
