def initDict(word, codice):
    diz = {}
    for i in range(len(word)):
        diz[codice[i]] = word[i]
    return diz

def check(word, codice):
    if len(word) != len(codice) or len(set(word)) != len(set(codice)):
        return False
    diz = initDict(word, codice)
    for i in range(len(word)):
        if diz[codice[i]] != word[i]:
            return False
    return True

def decod(pfile, codice):
    with open(pfile, encoding='utf-8') as fi:
        lines = [line[:-1] for line in fi]
        
    validWords = set()
    for word in lines:
        if check(word, codice):
            validWords.add(word)
    return validWords