def controlloLung(parola, codice):
    '''controllo se la parola rispetta la lunghezza del controllo'''
    if len(parola[0:-1]) == len(codice):
        return True
    return False

def controlloCod(parola, codice):
    '''controllo se le parole corrispondono alla struttura data'''
    diz = {}
    cod = ''
    parola = parola[0:-1]
    for pos,car in enumerate(codice):
        if car not in diz:
            if parola[pos] not in diz.values():
                diz[car] = parola[pos]
            else : return ('')
        cod = cod + diz[car]
    if cod == parola: return (parola)
    else : return ('')


def decod(pfile, codice):
    with open(pfile, encoding = 'utf-8') as file:
        parola = ''
        for f in file.readlines():
            f = f.lower()
            if controlloLung(f, codice):
                parola += controlloCod(f, codice) +' '
                
        parola = parola.split()
    return set(parola)