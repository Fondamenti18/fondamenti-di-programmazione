# coding=utf-8
# In determinate occasioni ci capita di dover scrivere i numeri in lettere, ad
# esempio quando dobbiamo compilare un assegno. Puo' capitare che alcuni numeri
# facciano sorgere in noi qualche dubbio.
#
# Le perplessita' nascono soprattutto nella scrittura dei numeri composti con 1
# e 8. Tutti i numeri come venti, trenta, quaranta, cinquanta, ecc... elidono la
# vocale finale (la "i" per 20, la "a" per tutti gli altri) fondendola con la
# vocale iniziale del numero successivo; scriveremo quindi ventuno, ventotto,
# trentotto, cinquantuno ecc...
# Il numero cento, nella formazione dei numeri composti con uno e otto, non si
# comporta cosi'; il numero "cento" e tutte le centinaia (duecento, trecento,
# ecc...), infatti, non elidono la vocale finale. Dunque non scriveremo centuno,
# trecentotto ma centouno, trecentootto, ecc...
#
# I numeri composti dalle centinaia e dalla decina "ottanta" invece tornano ad
# elidere la vocale finale; scriveremo quindi centottanta, duecentottanta,
# ecc..., non centoottanta, duecentoottanta, ...
#
# Il numero "mille" non elide in nessun numero composto la vocale finale;
# scriveremo quindi milleuno,  milleotto, milleottanta, ecc...
#
# Scrivere una funzione conv(n) che prende in input un intero n, con
# 0<n<1000000000000, e restituisce in output una stringa con il numero espresso
# in lettere
#
# ATTENZIONE: NON USATE LETTERE ACCENTATE.
# ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio
# dell'esercizio è zero.

single_digits = {
    0   : "",
    1   : "uno",
    2   : "due",
    3   : "tre",
    4   : "quattro",
    5   : "cinque",
    6   : "sei",
    7   : "sette",
    8   : "otto",
    9   : "nove"
}

def get_hundred_piece(number):
    '''Ritorna il pezzo relativo alle centinaia.'''
    hundred_suffix = { False : '', True : 'cento' }

    hundred = number // 100

    # Converte la cifra singola ed accoda il "cento". Se la cifra e' zero allora
    # bool(hundred) e' false, quindi non accoda il cento, ossia torna una
    # stringa vuota.
    return single_digits[hundred] + hundred_suffix[bool(hundred)]

def get_two_digits(number):
    '''Ritorna il pezzo relativo alle decine ed unità.'''
    two_digits = {
        0   : '',
        10  : "dieci",
        11  : "undici",
        12  : "dodici",
        13  : "tredici",
        14  : "quattordici",
        15  : "quindici",
        16  : "sedici",
        17  : "diciassette",
        18  : "diciotto",
        19  : "diciannove",
        20  : "venti",
        30  : "trenta",
        40  : "quaranta",
        50  : "cinquanta",
        60  : "sessanta",
        70  : "settanta",
        80  : "ottanta",
        90  : "novanta",
    }

    number %= 100
    piece = ''

    if number in two_digits: # Numero speciale (es. 12, 13, ...).
        piece += two_digits[number]
    else: # Abbiamo una decina ed una unità separata.
        tens = number % 100 // 10 * 10
        unit = number % 10

        piece += two_digits[tens]
        piece += single_digits[unit]

    return piece

def get_power(power, is_one=False):
    '''Ritorna l'indicatore di potenza (es. mille, milioni, ...).'''
    powers = {
        True : { 0 : '', 1 : 'mille', 2 : 'unmilione', 3 : 'unmiliardo' },
        False : { 0 : '', 1 : 'mila', 2 : 'milioni', 3 : 'miliardi' }
    }

    # Gli identificatori sono diversi se la cifra e' 1, cosa comunicata
    # dall'argomento "is_one".
    return powers[is_one][power]

def normalize(piece, number):
    '''Normalizza la stringa rimuovendo i casi speciali (vedere il testo
    dell'esercizio.
    '''
    cases = {
        ("oottant", "ottant"),
        ("ventiuno", "ventuno"),
        ("ventiotto", "ventotto"),
        ("auno", "uno"), # trentAUno -> trentuno
        ("aott", "ott"), # quarantAOtto -> quarantotto
        ("unocento", "cento") # Perchè get_hundred_piece non lo normalizza.
    }
    hundred = number // 100
    tens = number % 100
    unit = number % 10

    for case in cases:
        piece = piece.replace(case[0], case[1])

    return piece

def get_piece(raw_piece, power):
    number = int(''.join(map(str, raw_piece))) # Converte in numero.

    # Se il numero da convertire è semplicemente 1, si lascia solo la potenza.
    if number == 1:
        return get_power(power, is_one=True)

    piece = ''

    # Converte la prima cifra (delle centinaia).
    piece += get_hundred_piece(number)

    # Converte la seconda e terza cifra (decine ed unità).
    piece += get_two_digits(number)

    # Aggiunge eventuali potenze alla fine (es. 'mille' o 'milione').
    piece += get_power(power)

    # Normalizza la stringa (es. ventIOtto -> ventotto).
    return normalize(piece, number)

def conv(n):
    n = list(str(n))
    n.reverse()

    number = []
    power = 0
    # Il ciclo spezza il numero ogni tre cifre, quindi ogni pezzo viene
    # convertito separatamente.
    for index in range(0, len(n), 3):
        raw_piece = n[index:index + 3]
        raw_piece.reverse()
        number.append(get_piece(raw_piece, power))
        power += 1

    number.reverse()

    return ''.join(number)
