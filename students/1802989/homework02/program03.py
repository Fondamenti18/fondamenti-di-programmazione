def decod(pfile, struttura):
    '''inserire qui il codice'''
    ins = set()
    lst = open_file(pfile)
    for parola in lst:
        if len(parola) == len(struttura) and len(set(parola)) == len(set(struttura)):
            dizio = {}
            calcolo(parola, dizio, struttura, ins)
    return ins

def open_file(pfile):
    'Funzione utilizzata per aprire il file in UTF-8'
    with open(pfile, 'r', encoding='utf-8') as f:
        lst = f.read().split()
    return lst

def calcolo(parola, dizio, struttura, ins):
    'Funzione che controlla la corrispondenza char <--> cifra'
    for i in range(len(parola)):
        if struttura[i] in dizio and dizio[struttura[i]] != parola[i]:
            return False
        dizio[struttura[i]] = parola[i]
    return ins.add(parola)