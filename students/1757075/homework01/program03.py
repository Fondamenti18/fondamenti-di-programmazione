def codifica(chiave, testo):
    disordinata = disord(chiave)        # chiamo funzione
    ordinata = ordin(disordinata)       # chiamo funzione
    # preparo per codifica
    diz = {}           # dizionario in cui associare ordinata e disordinata
    i = 0               # contatore
    while i < len(ordinata):
        diz[ordinata[i]] = disordinata[i]   # creo associazione
        i += 1
    # codifico testo
    risultato = ''
    for c in testo:
        if diz.get(c) != None:              # se carattere in dizionario
           risultato += diz.get(c)          # codifico
        else:
            risultato += c
    return risultato

def decodifica(chiave, testo):
    disordinata = disord(chiave)            # chiamo funzione
    ordinata = ordin(disordinata)           # chiamo funzione
    # preparo per codifica
    diz = {}           # dizionario in cui associare ordinata e disordinata
    i = 0               # contatore
    while i < len(disordinata):
        diz[disordinata[i]] = ordinata[i]   # creo associazione
        i += 1
    # codifico testo
    risultato = ''
    for c in testo:
        if diz.get(c) != None:              # se carattere in dizionario
           risultato += diz.get(c)          # codifico
        else:
            risultato += c
    return risultato
    
def disord(chiave):
    # lista per eliminare caratteri
    elimina = []
    # metto caratteri da eliminare nella lista elimina
    for c in chiave:
        if c < 'a' or c > 'z':
            elimina.append(c)
    # elimino caratteri da chiave
    for c in elimina:
        chiave = chiave.replace(c, '') 
    # elimino le occorrenze e creo sequenza disordinata
    dis = set(chiave)               # creo set con singole occorrenze
    disordinata = ''                  # sequenza disordinata
    for c in reversed(chiave):        # itero chiave al contrario
        if c in dis:                # verifico se e' un occorrenza
            disordinata = c + disordinata       # modifico stringa
            dis.remove(c)           # rimuovo da set per evitare doppioni
    return disordinata

def ordin(disordinata):
    # creo sequenza ordinata
    ordi = []               # creo lista di comodo per ordinare elementi
    ordinata = ''                   # sequenza ordinata
    for c in disordinata:
        ordi.append(c)              # salvo in lista
    ordi.sort()                     # riordino
    for c in ordi:                  # salvo in stringa
        ordinata += c
    return ordinata
