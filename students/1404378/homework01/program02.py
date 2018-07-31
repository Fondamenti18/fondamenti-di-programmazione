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


teens = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci",
         "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]

decine = ["", "dieci", "venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]

migliaia = ["", "mila", "milioni", "miliardi", "trilioni"]

speciale = ["", "mille", "unmilione", "unmiliardo", "untrilione"]

def is_problematic(n):
    num = str(n)
    if len(num) == 2:
        return "1" in num[-1] or "8" in num[-1]
    elif len(num) == 3:
        return "8" in num[-2]

def handle_decine(n):
    result = ""
    if n > 19:
        dec, uni = divmod(n, 10)
    else:
        dec, uni = 0, n

    if dec:
        if is_problematic(n):
            result += (decine[dec])[:-1]
        else:
            result += decine[dec]
    if uni:
        result += teens[uni]
    return result

def handle_centinaia(n):
    result = ""
    cent, dec = divmod(n, 100)

    if cent:
        if cent == 1 and is_problematic(n):
            result += "cent"
        elif cent == 1 and not is_problematic(n):
            result += "cento"
        elif cent > 1 and is_problematic(n):
            result += teens[cent]+"cent"
        else:
            result += (teens[cent] + "cento")
    if dec:
        result += handle_decine(dec)
    return result

def dividi(n):
    result = []
    while n > 0:
        n, resto = divmod(n, 1000)
        result.append(resto)
    return result

def conv(n):
    if n == 0:
        return "zero"
    result = []
    parti = dividi(n)
    for i, cf in enumerate(parti):
        if cf == 1:
            result.append(speciale[i])
        elif 1 < cf < 20:
            result.append(teens[cf] + migliaia[i])
        elif 20 <= cf < 100:
            result.append(handle_decine(cf) + migliaia[i])
        else:
            result.append(handle_centinaia(cf) + migliaia[i])
    return "".join(reversed(result))
    
    
