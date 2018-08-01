def nocc(chiave):   
    for char in chiave:
        if char.isupper() or not char.isalpha():
            chiave = chiave.replace(char,'')
        if chiave.count(char)>1:
            chiave = chiave.replace(char,'',1)
    print(chiave)
    return chiave
def dizionario(key,value,decodifica):
    matrice = {}
    for i in range(len(key)):
        if decodifica:
            matrice[value[i]]=key[i]
        else:
            matrice[key[i]] = value[i]
    return matrice
def codifica(key,s):
    keySenzaocc = nocc(key) 
    keyOrdinata = ''.join(sorted(keySenzaocc))
    codificaTc = dizionario(keyOrdinata,keySenzaocc,False)
    stringaCodificata = ''
    iteratore = 0
    while iteratore<len(s):
        if s[iteratore] in codificaTc.keys():
            stringaCodificata = stringaCodificata + codificaTc[s[iteratore]]
        else:
            stringaCodificata = stringaCodificata + s[iteratore]
        iteratore+=1
    return stringaCodificata
def decodifica(key, s):
    keySenzaocc = nocc(key) 
    keyOrdinata = ''.join(sorted(keySenzaocc))
    decodificaTc = dizionario(keyOrdinata,keySenzaocc,True)
    stringaDecodificata = ''
    iteratore = 0
    while iteratore<len(s):
        if s[iteratore] in decodificaTc.keys():
            stringaDecodificata = stringaDecodificata + decodificaTc[s[iteratore]]
        else:
            stringaDecodificata = stringaDecodificata + s[iteratore]
        iteratore+=1
    return stringaDecodificata
                          
