import json


def genera_sottoalbero(fnome,x,fout):
    '''richiamo una funzione sottoalbero che data una lista contrenente il nodo iniziale costruisce un albero avente per radice il nodo'''
    sottoalbero = {}
    diz = json.loads(open(fnome).read())
    if x in diz :
        lista = [x]
        sottoAlbero(diz,lista, sottoalbero)     
    with open(fout, mode='w') as file:
        json.dump(sottoalbero, file)
        
def sottoAlbero(diz, lista, sottoalbero):
    '''funzione ricorsiva con cui creo un sottoalbero'''
    if len(lista):
        for el in lista:
            lista += diz[el]
            sottoalbero[el] = diz[el]
            lista.remove(el)
        sottoAlbero(diz, lista, sottoalbero)
    else: 
        return (sottoalbero)


def cancella_sottoalbero(fnome,x,fout):
    '''richiamo la funzione ricorsiva per torvare il sottoalbero, dopodiche faccio una sorta di differenza tra l'albero generale e il sottoalbero'''
    diz = json.loads(open(fnome).read())
    sottoalbero = {}
    lista = [x]
    sottoAlbero(diz, lista, sottoalbero)
    for el in sottoalbero:
        del diz[el]
    for el in diz:
        if x in diz[el]: diz[el].remove(x)
    with open(fout, mode='w') as file:
        json.dump(diz, file)
 
    
    
def trova_livelli(diz, lista, dizN, lvl=0):
    '''funzione ricorsiva con cui associo i nodi ai livelli'''
    if len(lista):
        l = []
        dizN[str(lvl)] = lista
        lvl += 1
        for el in lista:
            l += diz[el]
        lista = l
        lista.sort()
        trova_livelli(diz, lista, dizN, lvl)
    else : return(dizN)
    
    
def dizionario_livelli(fnome,fout):
    '''richiamo la ricorsiva che crea i livelli dell'albero'''
    diz = json.loads(open(fnome).read())
    dizN = {}
    lista =[trovaRadice(diz)]
    trova_livelli(diz, lista, dizN)
    with open(fout, mode='w') as file:
        json.dump(dizN, file)

def convertiInLista(diz):
    '''trasformo il dizionario dei livelli in un lista composta liste con i nodi di ogni livello'''
    lvl = []
    for el in diz:
        lvl += [diz[el]]
    return (lvl)
 
def trovaRadice(diz):
    '''trovo la radice dell'albero'''
    figli = []
    padri = diz.keys()
    for el in diz.values():
        figli += el
    for el in padri :
        if el not in figli : return(el)
    

def dizionario_gradi_antenati(fnome,y,fout):
    diz = json.loads(open(fnome).read())
    livelli = {}
    lista = [trovaRadice(diz)]
    trova_livelli(diz, lista, livelli)
    livelli = convertiInLista(livelli)
    
    ris = {}
    ris[lista[0]] = 0
    n = 0
    for lvl in livelli:
        for el in lvl:
            ris[el] = 0
            for nodo in livelli[n-1]:
                if el in diz[nodo]:
                    ris[el] += ris[nodo]
                    if len(diz[nodo]) == y:
                        ris[el] += 1
                    break
        n += 1   
    with open(fout, mode='w') as file:
        json.dump(ris, file)
