def decod(pfile, codice):
    ''' funzione principale '''
    # leggo il file
    with open(pfile, 'r') as f:
        file = f.read().split()
    
    # creo una lista con parole su cui lavorare
    parole = []         # lista in cui inserire parole con lunghezza corretta
    for p in file:              # per ogni parola
        if len(p) == len(codice):
            parole.append(p)        # la aggiungo a lista
    
    ris = calcola(parole, codice)
    
    return set(ris)


def calcola(parole, codice):
    ''' metodo che controlla se la parola se la parola rispetta la codifica
    vedendo se e' stata decodificata completamente da calcolaW e se le lettere
    nel dizionario sono un numero pari a quello che ci si aspetterebbe '''
    ris = []                        # risultato
    # per ogni parola da analizzare
    for p in parole:
        diz, c = calcolaW(codice, p)        # applico metodo
        # se lunghezza e' corretta
        if len(p) == c and len(diz.values()) == len(set(diz.values())):
            ris.append(p)                   # aggiungo a risultato
    
    return ris

def calcolaW(codice, p):
    ''' metodo che crea un dizionario con le codifiche associate ad una
    parola e un contatore che indica se le codifiche sono attuabili per ogni
    lettera della parola'''
    diz = {}                # dizionario dove associare caratteri a codifica
    c = 0                   # contatore per scorrere caratteri parola
    # controllo ogni carattere e vedo se c ha la codifica corretta
    while c < len(p):       # scorro parola
        # se numero non e' ancora in dizionario
        if codice[c] not in diz:
            diz[codice[c]] = p[c]           # aggiungi codifica
            c += 1                          # incremento
        # se la lettera associata al numero e' corretta
        elif diz.get(codice[c]) == p[c]:
            c += 1                          # incremento
        # altri casi codifica sbagliata:
        else: break
    
    return diz, c