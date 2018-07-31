"""
In determinate occasioni ci capita di dover scrivere i numeri in lettere,
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
"""

BASE_NUMS = {
    1: "uno",       2: "due",
    3: "tre",       4: "quattro",
    5: "cinque",    6: "sei",
    7: "sette",     8: "otto",
    9: "nove"
}

TEN_2_TWELVE = {
    11: "undici",        12: "dodici",
    13: "tredici",       14: "quattordici",
    15: "quindici",      16: "sedici",
    17: "diciassette",    18: "diciotto",
    19: "diciannove"
}

BASE_10_NUMS = {
    1: "dieci",        2: "venti",
    3: "trenta",       4: "quaranta",
    5: "cinquanta",    6: "sessanta",
    7: "settanta",     8: "ottanta",
    9: "novanta"
}

HUNDRED = "cento"         # 10 ** 2
THOUSAND = "mille"        # 10 ** 3
THOUSAND_BASE = "mila"
MILLION = "milione"       # 10 ** 6
BILLION = "miliardo"      # 10 ** 9


def convert_hundreds(n):
    c = n // 100
    if c:
        q = n % 100
        return (
            (convert_hundreds(c) if c != 1 else "")
            + (HUNDRED if q // 10 != 8 else HUNDRED[:-1])
            + convert_hundreds(q)
        )

    d = n // 10
    if d:
        q = n % 10
        return (
            TEN_2_TWELVE[n] if 10 < n < 20 else (
                BASE_10_NUMS[d] if d == 1 else (
                    (BASE_10_NUMS[d] if q not in {1, 8} else BASE_10_NUMS[d][:-1])
                    + (BASE_NUMS[q] if q else "")
                )
            )
        )

    return BASE_NUMS[n] if n != 0 else ""


def conv(n):
    response = ""
    for e in [9, 6, 3]:
        q = n // 10 ** e
        if not q:
            continue

        n = n % 10 ** e

        if e == 9:
            response += (convert_hundreds(q) if q != 1 else "un ") \
                        + (BILLION if q == 1 else (BILLION[:-1] + "i"))  # Miliardi

        elif e == 6:
            response += ("un" + (" " if not len(response) else "") if q == 1 else convert_hundreds(q)) \
                        + (MILLION if q == 1 else (MILLION[:-1] + "i"))  # Milioni

        else:
            response += THOUSAND if q == 1 else convert_hundreds(q) + THOUSAND_BASE  # Mille

    response += convert_hundreds(n)
    return response
