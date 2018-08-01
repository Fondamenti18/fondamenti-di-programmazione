def remove_last_dec(rest, word):
    if rest == 1 or rest == 8:
        word = word[:-1]
    return word

def remove_last_cent(rest, word):
    if rest == 8:
        word = word[:-1]
    return word

def resto_dec(val):
    return val%10

def resto_cent(val):
    return int(val%100/10)

def suffix_un():
    return "un"

def conv(val):

    arr1 = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]

    arr2 = ["", "", "venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]

    arr3 = ["cento", "mille", "mila", "milione", "milioni", "miliardo", "miliardi"]

    if val < 20:
        return arr1[val]
    elif val < 100:
        word = arr2[int(val/10)]
        resto = resto_dec(val)
        word = remove_last_dec(resto,word)
        return word + conv(val%10)
    elif val < 200:
        return arr3[0] + conv(val%100)
    elif val < 1000:
        resto = resto_cent(val)
        return conv(int(val/100)) + remove_last_cent(resto,arr3[0]) + conv(val%100)
    elif val < 2000:
        return arr3[1] + conv(val % 1000)
    elif val < 1000000:
        return conv(int(val/1000)) + arr3[2] + conv(val%1000)
    elif val < 2000000:
        return suffix_un() + arr3[3] + conv(val % 1000000)
    elif val < 1000000000:
        return conv(int(val/1000000)) + arr3[4] + conv(val%1000000)
    elif val < 2000000000:
        return arr3[5] + conv(val % 1000000000)
    elif val < 1000000000000:
        return conv(int(val / 1000000000)) + arr3[6] + conv(val % 1000000000)