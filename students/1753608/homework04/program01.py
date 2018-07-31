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

{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}

{"0": ["a"], "1": ["b"], "2": ["c", "d"], "3": ["e", "i", "l"], "4": ["f", "g", "h"]}

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

def genera_sottoalbero(fnome,x,fout):
    tree = load(fnome)
    new_tree = {}
    for key in tree:
        if(key == x):
            new_tree.update({key:tree[key]})
            new_tree = _genera_sottoalbero(tree,key,new_tree)
            break
    write(new_tree,fout)

def _genera_sottoalbero(tree,key,new_tree):
    children = tree[key]
    for child in children:
        _genera_sottoalbero(tree, child, new_tree)
        new_tree.update({child:tree[child]})
    return new_tree

def cancella_sottoalbero(fnome,x,fout):
    tree = load(fnome)
    new_tree={}
    root = next(iter(tree))
    new_tree.update({root: tree[root]})
    new_tree = _cancella_sottoalbero(tree,root,x,new_tree)
    write(new_tree,fout)

def _cancella_sottoalbero(tree,key,x,new_tree):
    children = tree[key]
    for child in children:
        if(child == x):
            break
        values = tree[child]
        try:
            values.remove(x)
        except:
            pass
        new_tree.update({child:values})
        _cancella_sottoalbero(tree, child, x, new_tree)
    return new_tree

def dizionario_livelli(fnome,fout):
    tree = load(fnome)
    new_tree={}
    root = next(iter(tree))
    lvl = 0
    new_tree.update({lvl:[root]})
    new_tree = _dizionario_livelli(tree,tree[root],lvl+1,new_tree)
    write(new_tree,fout)

def _dizionario_livelli(tree,children,lvl,new_tree):
    for child in children:
        _dizionario_livelli(tree,tree[child],lvl+1,new_tree)
        try:
            elements = new_tree[lvl]
            elements.append(child)
            elements = sorted(elements)
        except:
            elements = []
            elements.append(child)
        new_tree.update({lvl:elements})
    return new_tree

def dizionario_gradi_antenati(fnome,y,fout):
    tree = load(fnome)
    new_tree = {}
    val = 0
    root = next(iter(tree))
    children = tree[root]
    new_tree.update({root:0})
    if(len(children) == y): val = 1
    new_tree = _antenati(y,tree,children,new_tree,val)
    write(new_tree,fout)

def _antenati(y,tree,children,new_tree,val):
    for child in children:
        len_figli = len(tree[child])
        new_tree.update({child: val})
        if(len_figli == y):
            _antenati(y, tree, tree[child], new_tree, val + 1)
        elif(len_figli != 0):
            _antenati(y,tree,tree[child],new_tree,val)
    return new_tree

def load(fnome):
    lines = _load_txt(fnome)
    tree = {}
    for line in lines:
        tree.update(json.loads(line))
    return tree

def _load_txt(File):
    txt = open(File)
    lines = txt.readlines()
    return lines

def write(updated,fout):
    my_file = open(fout,"w")
    my_file.write(json.dumps(updated))
