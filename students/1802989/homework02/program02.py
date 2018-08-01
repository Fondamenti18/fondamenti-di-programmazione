import json
        
def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    with open(fcompiti) as f:
        diz = crea_strut(fcompiti, f)
    ris = search(insi, diz)
    save_json(ris, fout)
    return

def crea_strut(fcompiti, f):
    'Crea un dizionario in cui inserire chiavi-valore'
    dizio = {}
    for line in f:
        num = ''
        if 'comp' in line:
            k = ''
            k = itera(line)
        else:
            num = itera(line)
        dizio[k] = num
    return dizio

def itera(linea):
    'Funzione usata per raccogliere gruppi di operazioni ripetute'
    val = ''
    for c in linea:
        if c.isnumeric():
            val += c
    return val

def search(insi, diz):
    "Cerca all'interno del dizionario ogni elemento dell'insieme"
    risultato = {}
    for el in insi:
        if el in diz:
            lista = list()
            lista = research(el, lista, diz)
            risultato [el] = lista
    return risultato

def research(chiave, lista, diz):
    'Funzione che cerca in maniera "ricorsiva" chiavi-valori'
    while diz[chiave]:
        lista.append(diz[chiave])
        chiave = diz[chiave]
    return lista[::-1]

def save_json(dati, fout):
    'Funzione usata per salvare il file in formato JSON nel path specificato'
    with open(fout, 'w') as file_json:
        json.dump(dati, file_json)
    return