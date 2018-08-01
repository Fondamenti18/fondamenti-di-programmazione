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
La lista è ordinata lessicograficamente ed in modo crescente.
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

def getTree(fname):
    with open(fname, 'r') as f:
        tree = json.loads(f.read())
        return tree

def printTree(fname, tree):
    with open(fname, 'w') as f:
        f.write(json.dumps(tree))

def getSub(tree, x, subtree):
    subtree[x] = tree[x]
    for e in tree[x]:
        getSub(tree, e, subtree)

def genera_sottoalbero(fnome,x,fout):
    tree = getTree(fnome)
    subtree = {}
    getSub(tree, x, subtree)
    printTree(fout, subtree)

def getRoot(tree):
    notp = set()
    for x, v in tree.items():
        notp.update(set(v))
    for x in tree:
        if x not in notp:
            return x

def deleteSub(tree, act, x, newtree):
    if act == x: #handles x == root case
        return None
    newtree[act] = []
    for e in tree[act]:
        if e != x:
            newtree[act].append(e)
            deleteSub(tree, e, x, newtree)

def cancella_sottoalbero(fnome,x,fout):
    tree = getTree(fnome)
    root = getRoot(tree)
    newtree = {}
    deleteSub(tree, root, x, newtree)
    printTree(fout, newtree)

def buildLivelliTree(tree, x, lvl, levtree):
    if lvl not in levtree:
        levtree[lvl] = []
    levtree[lvl].append(x)
    for e in tree[x]:
        buildLivelliTree(tree, e, lvl+1, levtree)

def dizionario_livelli(fnome,fout):
    tree = getTree(fnome)
    root = getRoot(tree)
    lvltree = {}
    buildLivelliTree(tree, root, 0, lvltree)
    for x in lvltree:
        lvltree[x].sort()
    printTree(fout, lvltree)

def buildDegreeTree(tree, root, x, answ, degtree, y):
    degtree[x] = answ
    ydeg = 1 if (len(tree[x]) == y) else 0
    for e in tree[x]:
        buildDegreeTree(tree, root, e, answ + ydeg, degtree, y)

def dizionario_gradi_antenati(fnome,y,fout):
    tree = getTree(fnome)
    root = getRoot(tree)
    degtree = {}
    buildDegreeTree(tree, root, root, 0, degtree, y)
    printTree(fout, degtree)
