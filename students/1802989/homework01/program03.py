words = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

def codifica(chiave, testo):
    ordinata, disordinata = main(chiave)
    diz_dec = decode(ordinata, disordinata)
    tradotto = traduci(diz_dec, testo)
    return tradotto

def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    ordinata, disordinata = main(chiave)
    diz_cod = code(ordinata, disordinata)
    tradotto = traduci(diz_cod, testo)
    return tradotto

def main(chiave):
    pulita = clean(chiave)
    disordinata = no_doppie(pulita)
    ordinata = ordina(disordinata)
    return ordinata, disordinata

def clean(chiave):
    for char in chiave[:]:
        if char not in words:
            chiave = chiave.replace(char, '')
    return chiave

def no_doppie(chiave):
    c_chiave = ''
    for char in chiave[::-1]:
        if c_chiave.count(char) == 0:
            c_chiave += char
    return c_chiave[::-1]

def ordina(chiave):
    ordinata = ''.join(sorted(chiave))
    return ordinata

def code(ordinata, disordinata):
    diz = {}
    for i in range(len(ordinata)):
        diz[ordinata[i]] = disordinata[i]
    return diz

def decode(ordinata, disordinata):
    diz = {}
    for i in range(len(ordinata)):
        diz[disordinata[i]] = ordinata[i]
    return diz

def traduci(diz, testo):
    testo = list(testo)
    for i in range(len(testo))[:]:
        estrai_chiavi(diz, testo, i)
    return ''.join(testo)

def estrai_chiavi(diz, testo, i):
    for k,v in diz.items():
        if testo[i] == v:
            testo[i] = k
            break
    return