def post(fposts,insieme):
    '''funzione principale'''
    with open(fposts, 'r') as f:        # leggo il file 
        posts = f.read()
    lista = posts.split('<POST>')       # lo divido per ogni occorrenza di post
    ris = []                            # variabile per risultato
    # per ogni elemento nella lista
    for i in lista:
        # applico metodo
        ris.append(ricava(i, insieme))
    
    ris = set(ris)                      # trasformo la lista in insieme 
    ris.remove(None)                    # e rimuovo valori None
    
    return ris
    
def ricava(posts, insieme):
    ''' metodo che ottiene da una stringa solo le parole e l'identificativo '''
    # variabili dove salvare parole e numeri
    post = ''
    numeri = ''
    # per ogni carattere  nel post
    for i in posts:
        if i.isalpha():             # se lettera dell'alfabeto
            post += i
        elif i.isdecimal():         # se numero
            numeri += i
        else:                       # altrimenti aggiungo spazio
            post += ' '
            numeri += ' '
    
    post = post.lower().split()     # creo lista di parole da controllare
    numeri = numeri.split()         # creo lista con identificativo del post
    # applico metodo
    ris = occorrenze(post, numeri, insieme)
    
    return ris

def occorrenze(post, numeri, insieme):
    ''' metodo che calcola le occorrenze delle parole della lista nell'insieme '''
    mod = list(insieme)             # lista per modificare valori insieme per verifica
    insieme = []                    # nuova lista in cui aggiungere valori
    for i in mod:
        insieme.append(i.lower())   # metto la stringa con caratteri minuscoli per
                                    # non fare errori durante confronto
    insieme = set(insieme)          # faccio tornare set
    c = 0                           # contatore
    # finche' non scorro tutta la lista finche la parola non e' nell'insieme
    while c < len(post) and post[c] not in insieme:
        c += 1
    # se non sono arrivato a fine lista ho trovato occorrenza
    if len(post) - c > 0:
        return numeri[0]
