def verifica(struttura, riga):
    dizionario = {}
    for indice in range(len(riga)):
        if struttura[indice] in dizionario and dizionario[struttura[indice]] != riga[indice]:
            return False
        dizionario[struttura[indice]] = riga[indice]
    return True


def decod(pfile, struttura):
    return set([riga[:-1] for riga in open(pfile) if len(struttura) == len(riga[:-1]) and len(set(struttura)) == len(set(riga[:-1])) and verifica(struttura, riga[:-1])])
