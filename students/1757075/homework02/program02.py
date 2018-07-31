import json

def pianifica(fcompiti,insi,fout):
    ''' metodo principale '''
    # leggo il file
    with open(fcompiti, 'r') as f:              # leggo il file 
        comp = f.read()
    # applico metodo
    comp, num = ricava(comp)                    # trasformo file
    comp, num = comp.split(), num.split()       # divido compiti e numeri
    # applico metodo
    ris = calcola(comp, num, insi)
    # scrivo file in formato json
    with open(fout, 'w') as f:
        json.dump(ris, f)

def calcola(comp, num, insi):
    ''' funzione che associa ciascun compito al suo subordinato, sensa calcolare
    vari gradi di subordinazione '''
    diz = {}                        # dizionario 
    c = 0                           # contatore
    #per ogni compito
    while c < len(comp):
        if c == len(comp)-1 or comp[c] == comp[c+1] : # se compito e' seguito da compito
            diz[num[c]] = []                    # compito primario
            c += 1                              # incremento per vedere se dopo ci sono altri comp
        else:
            diz[num[c]] = [num[c+1]]        # compito subordinato
            c += 2                          # dopo c'e' sub quindi posso saltarne due
    
    return calcola2(insi, diz)
    
    
def calcola2(insi, diz):
    ''' metodo che calcola per ogni comp nell'insieme i compiti a cui e' subordinato '''
    ris = {}                                # risultato
    # per ogni compito nell'insieme
    for comp in insi:
        num = comp                          # varibile numero su cui lavorare
        ls = []                             # lista compiti sub
        
        # finche' ci sono comp sub
        while True:
            # se il compito cercato e' nel diz
            if num in diz:
                # se e' primario fine ricerca
                if diz.get(num) == []:
                    ls.reverse()
                    ris[comp] = ls # associo compito iniziale a risultato di ls
                    break
                else:
                    ls.append(diz.get(num)[0]) # aggiungo compito a cui e' subordinato a lista
                    num = diz.get(num)[0]   # il numero su cui lavorare e' 
                                            # uguale al compito a cui era subordinato
            else:
                break
    return ris    

def ricava(compiti):
    ''' metodo che divide compiti e numeri '''
    # variabili dove salvare compiti e numeri
    comp = ''
    num = ''
    # per ogni carattere  nel file
    for i in compiti:
        if i.isalpha():             # se lettera dell'alfabeto
            comp += i
        elif i.isdecimal():         # se numero
            num += i
        else:                       # altrimenti aggiungo spazio
            comp += ' '
            num += ' '
    
    return comp, num