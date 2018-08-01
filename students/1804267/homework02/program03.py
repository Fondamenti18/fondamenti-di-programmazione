def prova(codice, line):
    dic = {}
    for index in range(len(line)):
        if codice[index] in dic and dic[codice[index]] != line[index]:
            return True
        dic[codice[index]] = line[index]
    return False

def decod(pfile, codice):
    file = open(pfile, "r")
    lista_parole = set()
    for parola in file:
        lista_parole.add(parola[:-1])
    insieme2 = lista_parole.copy()
    for parola in insieme2:
        if len(parola) != len(codice):
            lista_parole.remove(parola)
            continue
        if len(set(codice)) != len(set(parola)):
            lista_parole.remove(parola)
            continue
        if prova(codice, parola):
            lista_parole.remove(parola)
            continue
    return lista_parole