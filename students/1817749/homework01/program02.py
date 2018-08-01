unita = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove",
         "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto",
         "diciannove"]

cent_unit = ["", "", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove"]

decine = ["", "", "venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]

states = ["", "", "mille", "mila", "unmilione", "milioni", "unmiliardo", "miliardi"]


def get_cent(c, d):
    if c >= 1:
        if d == 8:
            return cent_unit[c] + "cent"
        return cent_unit[c] + "cento"
    return cent_unit[c]


def complex_number(num):
    c, d, u = num // 100, num // 10 % 10, num % 10
    if d == 1:
        return get_cent(c, d) + unita[u + 10]
    if u == 1 or u == 8:
        return get_cent(c, d) + decine[d][:-1] + unita[u]
    return get_cent(c, d) + decine[d] + unita[u]


def convert(num, state):
    if num == 0:
        return ""
    if num == 1:
        if state == 0:
            return "uno"
        else:
            return states[state]
    return complex_number(num) + states[state + 1]


def conv(num):
    number = ""
    state = 0
    while num > 0:
        number = convert(num % 1000, state) + number
        num //= 1000
        state += 2
    return number
