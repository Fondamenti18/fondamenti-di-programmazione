'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero  e l'attributo della chiave e' la lista
(eventualmente vuota) degli identificativi dei  figli del nodo. Gli identificativi dei nodi
all'interno delle liste sono in ordine lessicografico crescente.



Ecco un esempio di dizionario d che rappresenta un dizionario-albero

d={
'a':['b'],
'b':['c','d'],
'c':['i'],
'd':['e','l'],
'e':['f','g','h'],
'f':[],
'g':[],
'h':[],
'i':[],
'l':[]
}

L'albero rappresentato da d e'

                             'a'
                              |
                _____________'b'____________
               |                            |
              'c'                  ________'d'_______
               |                  |                  |
              'i'         _______'e'_______         'l'
                         |        |        |
                        'f'      'g'      'h'


Implementare le seguenti funzioni:

1)
la funzione genera_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

produce   il  dizionario-albero che rappresenta   il sottoalbero  radicato
nell'identificativo x che si ottiene dal dizionario-albero d.
Il dizionario-albero ottenuto va registrato nel file fout.
Se l'identificativo x non e' tra i nodi di d allora  il dizionario-albero prodotto
deve essere vuoto.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di
genera_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'f': [], 'g': [], 'h': [], 'e': ['f', 'g', 'h'], 'l': [], 'd': ['e', 'l']}



2)
la funzione cancella_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

ricava  da d il sottoalbero radicato in x e lo salva nel file fout.
Se x non e' presente tra le chiavi di  d allora  il dizionario-albero d non viene modificato.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di
cancella_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'a': ['b'], 'b': ['c'], 'c': ['i'], 'i':[]}


3)
la funzione dizionario_livelli(fnome, fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- il nome di un file json (fout)

costruisce il  dizionario che ha come  chiavi i livelli del dizionario-albero d. L'attributo di una
chiave di valore x e' la lista degli identificativi  dei nodi che si trovano a livello x  nell'albero rappresentato da d.
La lista e' ordinata lessicograficamente ed in modo crescente.
Il dizionario cosi' costruito va registrato nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di
dizionario_livelli(fname,fout)
il file fout conterra' il dizionario
{0: ['a'], 1: ['b'], 2: ['c', 'd'], 3: ['e','i','l'], 4: ['f', 'g', 'h']}

4)
la funzione dizionario_gradi_antenati(fnome,y,fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- un intero y
- il nome di un file json (fout)

costuisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero
rappresentato dal dizionario-albero d, Attributo di una chiave di valore x e' il numero
di antenati di grado y che ha il nodo con identificativo x nell'albero.
Registra il dizionario costruito nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di
dizionario_gradi_antenati(fnome,2,fout)
il file fout conterra' il dizionario
{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.
'''




import json

def deleteTree(tree, x):
    #Attraverso una funzione di supporto, cancella il sottoalbero del nodo x
    #in input durante la visita
    
    def foo(tree, nodo, diz):
        del diz[nodo]

    diz = tree.copy()
    visitTree(tree, x, diz, foo)
    for i in diz.keys():
        if x in diz[i]:
            diz[i].remove(x)
            break
    return diz

def findRoot(tree):
    #Trova la radice dell'albero dato in input attraverso la continua cancellazione
    #dei sottoalberi dei nodi
    diz = tree.copy()
    while diz != {}:
        root = list(diz.keys())[0]
        diz = deleteTree(diz, root)
    return root

def visitTree(tree, nodo, diz, func):
    #Visita l'albero ricorsivamente con una funzione 'func' di supporto
    #Non ritorna nulla in input
    func(tree, nodo, diz)
    for x in tree[nodo]:
        visitTree(tree, x, diz, func)

def visitTreeLevel(tree, nodo, diz, liv = 0):
    #Visita l'albero tenendo traccia del livello dei nodi visitati
    if liv not in diz.keys():
        diz[liv] = []
    diz[liv].append(nodo)
    diz[liv] = sorted(diz[liv])
    liv += 1
    for i in tree[nodo]:
        visitTreeLevel(tree, i, diz, liv)
        
def getElders(tree, nodo, elderlst):
    #Crea una lista contenente tutti gli avi del nodo in input
    for i in tree:
        if nodo in tree[i]:
            elderlst.append(i)
            getElders(tree,i,elderlst)
    return elderlst


def genera_sottoalbero(fnome, x, fout):
    def foo(tree, nodo, diz):
        diz[nodo] = tree[nodo]

    with open(fnome, 'r') as f:         #Apertura del file JSON
        tree = json.load(f)

    diz = {}
    visitTree(tree, x, diz, foo)
    
    with open(fout, 'w') as f:          #Scrittura del file JSON
        json.dump(diz, f)

def cancella_sottoalbero(fnome, x, fout):
    with open(fnome, 'r') as f:         #Apertura del file JSON
        tree = json.load(f)

    diz = deleteTree(tree, x)
   
    with open(fout, 'w') as f:          #Scrittura del file JSON
        json.dump(diz, f)

def dizionario_livelli(fnome,fout):
    with open(fnome, 'r') as f:         #Apertura del file JSON
        tree = json.load(f)

    root = findRoot(tree)
    diz = {}
    visitTreeLevel(tree, root, diz)
    
    with open(fout, 'w') as f:          #Scrittura del file JSON
        json.dump(diz, f)

def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome, 'r') as f:         #Apertura del file JSON
        tree = json.load(f)
    
    diz={}
    for i in tree:
        eldlst=getElders(tree,i,[])
        if eldlst==[]:
            diz[i]=0
        else:
            counter=0
            for j in eldlst:
                if len(list(tree[j]))==y:
                    counter+=1
                diz[i]=counter
    
    with open(fout, 'w') as f:          #Scrittura del file JSON
        json.dump(diz, f)
    
    
    
    
