def codifica(chiave, testo):
    ''' Viene codificato e restituito un testo, fornito il testo stesso e una chiave di codifica'''
    codifica=codifica_chiave(chiave)
    for indice,carattere in enumerate(testo): 
        if carattere in codifica.keys(): testo = testo[:indice]+ testo[indice:].replace(testo[indice],codifica[carattere],1)
    return testo
    
def decodifica(chiave, testo):
    ''' Viene decodificato e restituito un testo, fornito il testo stesso e una chiave di codifica'''
    decodifica=decodifica_chiave(chiave)  
    for indice,carattere in enumerate(testo): 
        if carattere in decodifica.keys(): testo = testo[:indice]+ testo[indice:].replace(testo[indice],decodifica[carattere],1)
    return testo

def codifica_chiave(chiave):
    chiave=processa_chiave(chiave)
    chiave_ord=''.join(sorted(chiave))
    codifica={}
    for indice,carattere in enumerate(chiave_ord): codifica[carattere]=chiave[indice]    
    return codifica

def decodifica_chiave(chiave):
    chiave=processa_chiave(chiave)
    chiave_ord=''.join(sorted(chiave))
    decodifica={}
    for indice,carattere in enumerate(chiave): decodifica[carattere]=chiave_ord[indice]    
    return decodifica

def processa_chiave(chiave):
    for carattere in chiave:
        if ord(carattere)<ord('a') or ord(carattere)>ord('z'): chiave= chiave.replace(carattere,'')
    chiave=elimina_copie(chiave)
    return chiave

def elimina_copie(chiave):
    for carattere in chiave:
        if carattere in chiave[chiave.find(carattere)+1:]: chiave= chiave.replace(carattere,'',1)
    return chiave