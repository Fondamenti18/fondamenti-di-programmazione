

import json

def genera_sottoalbero(fnome,x,fout):
    ''' Funzione che legge file, controlla se e' presente albero con nodo x
        scrive in fout il sottoalbero, se x non c'e' restituisce []
    '''
    alb = leggiFile(fnome)              # leggo flie

    ris = {}                            # dizionario risultato
    # controllo se nodo x e' presente
    if x not in alb:
        salvaFile(ris, fout)            # scrivo su file
        return None                     # interrompo
    
    ris[x]=alb[x]                   # primo elemento di dizionario
    ls = alb[x].copy()              # creo una copia per non modificare diz
    calcola(alb, ls, ris)           # elementi da inserire
    salvaFile(ris, fout)
    

def cancella_sottoalbero(fnome,x,fout):
    ''' Funzione che controlla se nodo x e' presente in albero in caso elimina
        tutti x e i suoi figli altrimenti non fa modifiche
    '''
    alb = leggiFile(fnome)              # leggo file
    
    # se nodo e' presente
    if x in alb:
        ris = {}                        # dizionario nodi da eliminare
        ris[x]=alb[x]                   # primo elemento di dizionario
        ls = alb[x].copy()              # creo una copia per non modificare diz
        calcola(alb, ls, ris)           # elementi da inserire
        
        # per ogni nodo da eliminare
        for n in ris:
            del alb[n]                  # elimino nodo
        # per ongi chiave in albero
        for k in list(alb.keys()):
            # se x contenuta in nodo
            if alb[k].count(x) > 0:
                alb[k].remove(x)        # elimono figlio x da nodo
                break
    salvaFile(alb, fout)

def dizionario_livelli(fnome,fout):
    ''' Funzione che associa livello dell'albero a tutti i nodi che contiene '''
    alb = leggiFile(fnome)
    ris = {}
    # inzializzo livelli
    for n in range(0, 50):
        ris[n]=[]
    c = 0               # contatore
    rad = radice(alb)   # ricavo radice
    livello(alb, ris, rad.pop(), c)
    
    elimina = []
    # per ogni livello
    for liv in ris:
        # se e' vuoto
        if ris[liv] == []:
            elimina.append(liv)         # aggiungo a lista da eliminare
        ris[liv].sort()                 # riordino valori
    # per ogni chiave da eliminare
    for liv in elimina:
        del ris[liv]                    # la elimino
    
    salvaFile(ris, fout)

def dizionario_gradi_antenati(fnome,y,fout):
    ''' Funzione che associa nodo a numero di antenati di grado y '''
    alb = leggiFile(fnome)
    grado = {}
    ris = {}
    
    # per ogni chiave
    for k in alb:
        grado[k]=len(alb[k])            # associo grado a chiave
    
    c = 0               # contatore
    rad = radice(alb)   # ricavo radice
    antenati(alb, grado, ris, y, rad.pop(), c)
    
    salvaFile(ris, fout)

def radice(alb):
    ''' metodo che trova radice dell'albero '''
    figli = set()
    for nodo in alb:
        for f in alb[nodo]:
            figli.add(f)
    return set(alb) - figli
    
def antenati(alb, grado, ris, y, nodo, c):
    ''' funzione che associa ad ogni chiave il numero di antenati di grado y '''
    ris[nodo]=c         # associo nodo a numero di antenati di grado y
    # se nodo ha figli
    if alb[nodo] != []:
        # per ogni figlio
        for n in alb[nodo]:
            # se e' di grado y
            if grado[nodo] == y:
                antenati(alb, grado, ris, y, n, c+1)
            else:
                antenati(alb, grado, ris, y, n, c)


def livello(alb, ris, nodo, c):
    ''' funzione che associa nodi a livello rispettivo '''
    # associo nodo a livello
    ris[c].append(nodo)
    
    # se nodo ha figli
    if alb[nodo] != []:
        # ricorsione
        for nodo in alb[nodo]:
            livello(alb, ris, nodo, c+1)

def calcola(alb, ls, ris):
    ''' funzione che inserisce nel dizionario ris nodo x e i suoi figli '''
    if ls == []:                    # nel caso la lista fosse vuota
        return None
    # se nodo non ha figli
    if alb[ls[0]] == []:
        ris[ls[0]]=[]               # salvo nodo con lista vuota
    else:
        ris[ls[0]]=alb[ls[0]]       # salvo nodo con figli
        # per ogni figlio
        for n in alb[ls[0]]:
            ls.append(n)            # aggiungo nodo da visionare a lista
    ls.remove(ls[0])                # elimino nodo visto
    # finche' lista non e' vuota
    if ls != []:
        calcola(alb, ls, ris)
            
def salvaFile(ris, file):
    ''' Funzione che salva dizionario in formato json '''
    with open(file, 'w') as f:
        json.dump(ris, f)

            
def leggiFile(file):
    ''' Funzine che legge file e ritorna la sua rappresentazione '''
    with open(file) as j:
        f = json.load(j)
    return f
