def post(fposts,insieme):
    ''' Riceve un file di testo e un insieme di parole e controlla se nei post contenuti nel file ci sia almeno
    una volta almeno una parola di input. Infine ritorna un insieme con gli ID dei post che contengono le parole '''
    f= open(fposts, mode='r', encoding='utf-8')  
    insieme = lower_insieme(insieme)
    risultato = set([])
    in_lettura = 'none'
    parola_presente= False
    for riga in f:
        risultato,in_lettura,parola_presente=applica_funzioni(riga,parola_presente,risultato,in_lettura,insieme)
    parola_presente, risultato = aggiunta_id(in_lettura,parola_presente,risultato)
    f.close()
    return risultato

def applica_funzioni(riga,parola_presente,risultato,in_lettura,insieme):
    if '<POST>' in riga:
        parola_presente, risultato = aggiunta_id(in_lettura,parola_presente,risultato)
        in_lettura=cerca_id(riga,in_lettura)
    elif not parola_presente:
        riga_alfabetica=alfa_riga(riga)
        parole_riga= set(riga_alfabetica.split())
        parola_presente=verifica_presenza(insieme, parole_riga, parola_presente)
    return risultato,in_lettura,parola_presente

def lower_insieme(insieme):
    for parola in insieme: 
        insieme.remove(parola)
        insieme.add(parola.lower())
    return insieme

def aggiunta_id(in_lettura,parola_presente, risultato):
    if not in_lettura == 'none' and parola_presente == True:
        risultato.add(in_lettura)
        parola_presente = False
    return parola_presente,risultato

def cerca_id(riga,in_lettura):
    in_lettura=''
    for carattere in riga:
        if ord('0')<=ord(carattere)<=ord('9'): in_lettura+=carattere
    return in_lettura

def alfa_riga(riga):
    riga_alfabetica=''
    for carattere in riga:
        carattere = carattere.lower()
        if not carattere.isalpha():
            carattere=' '
        riga_alfabetica+=carattere
    return riga_alfabetica

def verifica_presenza(insieme, parole_riga, parola_presente):
    for parola in insieme:
        if parola in parole_riga:
            parola_presente = True
            break
    return parola_presente