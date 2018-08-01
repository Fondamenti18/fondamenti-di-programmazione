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




from json import load, dump
from copy import copy

def save(filename, data):
    with open(filename, 'w') as f:
        dump(data, f)
def loadFile(filename):
    with open(filename, encoding='utf-8') as f:
        return load(f)
    
def getRoot(diz):
    dic2 = set()
    for x in diz:
        for z in diz[x]: dic2.add(z)
    for c in diz:
        if c not in dic2: return c
    return None


def recursiveTree1(x, diz, tree):
    temp = []
    for c in diz[x]:
        temp.append(c)
        recursiveTree1(c, diz, tree)
    tree[x] = temp
    
def recursiveTree2(s, diz):        
    for c in diz[s]: 
        recursiveTree2(c, diz)
    del diz[s]
    
    
def recursiveTree3(s, diz, tree, lev):
    if len(diz[s]):
        temp = []
        for c in diz[s]:
            temp.append(c)
            recursiveTree3(c, diz, tree, lev+1)
        tree[lev] = tree.setdefault(lev,[]) + temp

def recursiveTree4(s, diz, tree, y, path):
    count = 0
    for i in path:
        if len(diz[i]) == y: count+=1
    tree[s] = count
    path.append(s)
    for c in diz[s]:
        recursiveTree4(c, diz, tree, y, copy(path))

def genera_sottoalbero(fnome,x,fout):
    diz, tree = loadFile(fnome), {}
    if x in diz:
        recursiveTree1(x, diz, tree)
        save(fout, tree)
        return
    save(fout, diz)
    
def cancella_sottoalbero(fnome,x,fout):
    diz = loadFile(fnome)
    if x in diz:
        recursiveTree2(x, diz)
        for i in diz:
            if x in diz[i]: diz[i].remove(x)
    save(fout, diz)

def dizionario_livelli(fnome,fout):
    diz = loadFile(fnome)
    fi = getRoot(diz)
    tree = {0:[fi]}
    recursiveTree3(fi, diz, tree, 1)
    for i in tree.keys():
        tree[i] = sorted(tree[i]) 
    save(fout, tree)

def dizionario_gradi_antenati(fnome,y,fout):
    diz, tree = loadFile(fnome), {}
    recursiveTree4(getRoot(diz), diz, tree, y, [])
    save(fout, tree)