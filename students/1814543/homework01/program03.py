def costruisciDizionario(chiave):
    chiaveOrdinata=[]
    chiaveDisordinata=[]
    for C in reversed(chiave):
        if(C<'a' or C>'z'):
            continue
        else:
            if C not in chiaveDisordinata:
                chiaveDisordinata.append(C)
    chiaveDisordinata.reverse()     
    chiaveOrdinata = sorted(chiaveDisordinata)
    dizChiave = {}
    
    for keyOrd, keyDisord in zip(chiaveOrdinata, chiaveDisordinata):
        dizChiave[keyOrd] = keyDisord
    
    return dizChiave

def codifica(chiave, testo):
    risultato=[]
    dizChiave = costruisciDizionario(chiave)
    for item in testo:
        if item in dizChiave:
            risultato.append(dizChiave[item])
        else:
            risultato.append(item)
            
    return ''.join(risultato)

def decodifica(chiave,testo):
    risultato=[]
    dizChiave = costruisciDizionario(chiave)
    nuovoDiz = dict (zip(dizChiave.values(),dizChiave.keys()))

    for item in testo:
        if item in nuovoDiz:
            risultato.append(nuovoDiz[item])
        else:
            risultato.append(item)
            
    return ''.join(risultato)