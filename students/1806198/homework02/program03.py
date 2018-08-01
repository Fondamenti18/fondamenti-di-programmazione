#controlla lettera x lettera la corr. nel codice
def controlla_parola(strutt,parola,codice):
    segnaposto=0
    for lettera in parola:
        for x,y in strutt.items():
            if check(parola,lettera,segnaposto,codice,x,y):
                return False
        segnaposto=parola.index(lettera,segnaposto)+1
    return True

def check(parola,lettera,segnaposto,codice,x,y):
    i=parola.index(lettera,segnaposto)
    z=codice[i]
    if (x!= lettera and y== z) or (x == lettera and y != z):
        return True
    return False

#prepara la parola al controllo
def elabora_parola(parola,codice):
    parola=parola[:-1]
    strutt={}
    for lettera in parola:
        if lettera not in strutt:
             strutt[lettera]=codice[parola.index(lettera)]
    return strutt,parola    
    
#funzione principale
def decod(pfile, codice):
    
    parole=leggi_file(pfile)

    insieme=set()
    l=len(codice)+1
    
    for parola in parole:
        if len(parola)==l:
            strutt,parola=elabora_parola(parola,codice)
            if controlla_parola(strutt,parola,codice):
                insieme.add(parola)
                
    return insieme

#restituisce una lista di parole
def leggi_file(pfile):
    file = open(pfile, "r")
    parole=file.readlines()
    file.close()
    return parole
