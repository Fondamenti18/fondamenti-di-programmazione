def decod(pfile, codice):
    f = open(pfile, "r")
    listaParole = f.readlines()
    
    f.close()
    lista = set()
    lunghezza = len(codice)
    numDist = len(set(codice))
    for parola in listaParole:
        dizionario = {}
        parola = parola.replace("\n", "")
        if len(parola)==lunghezza and len(set(parola))==numDist:
            bene = 1
            for i in range(0, lunghezza):
                if parola[i] not in dizionario:
                    dizionario[parola[i]] = codice[i]
                else:
                    if dizionario[parola[i]] != codice[i]:
                        bene = 0
                        break
            if bene:
                lista.add(parola)
                
    return lista