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
                                  |
                                 'i'


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
import bisect

def exploreSubTree(tree, node, newtree):
    newtree[node] = []

    children = tree[node]
    for child in children:
        exploreSubTree(tree, child, newtree)
        newtree[node].append(child)

def subTreeExclusion(tree, node, excluding, newtree):
    newtree[node] = []

    children = tree[node]
    for child in children:
        if child != excluding:
            subTreeExclusion(tree, child, excluding, newtree)
            newtree[node].append(child)

def enumerateByLayer(node, layer, newtree, tree):
    if layer not in newtree:
        newtree[layer] = [node]
    else:
        bisect.insort(newtree[layer], node)

    children = tree[node]
    for child in children:
        enumerateByLayer(child, layer+1, newtree, tree)

def gradoAntenati(node, count, target, tree, newtree):
    newtree[node] = count

    incrementor = 0
    if len(tree[node]) == target:
        incrementor = 1

    for child in tree[node]:
        gradoAntenati(child, count + incrementor, target, tree, newtree)

# def findRoot(tree, rawinput):
#     children = set()

#     for key in tree:
#         if key in children:
#             continue

#         index = rawinput.find(key)
#         index2 = rawinput.find(key, index+1)

#         if index2 == -1:
#             return key
#         else:
#             # every child of this node is not part of the root
#             for child in tree[key]:
#                 children.add(child)

def findRoot(tree, rawinput):
     children = set()

     for key in tree:
         if key in children:
             continue

         index = rawinput.find(key)
         index2 = rawinput.find(key, index+1)

         if index2 == -1:
             return key
         else:
             # every child of this node is not part of the root
             traverseappend(tree, key, children)

def traverseappend(tree, key, children):
    for child in tree[key]:
        children.add(child)
        traverseappend(tree, child, children)

    return














def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as jsonfile:
        tree = json.loads(jsonfile.read())
        
        newtree = {}
        exploreSubTree(tree, x, newtree)

        debug = 0

    
    with open(fout, 'w') as f:
        f.write(json.dumps(newtree))

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    # first key seems to always be the root, may change with updates
    # first key seems to always be the root, may change with updates
    # first key seems to always be the root, may change with updates
    with open(fnome) as jsonfile:
        raw = jsonfile.read()
        tree = json.loads(raw)
        root = findRoot(tree, raw)

        newtree = {}
        subTreeExclusion(tree, root, x, newtree)

        debug = 0

    with open(fout, 'w') as f:
        f.write(json.dumps(newtree))


def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    # first key seems to always be the root, may change with updates
    # first key seems to always be the root, may change with updates
    # first key seems to always be the root, may change with updates
    with open(fnome) as jsonfile:
        raw = jsonfile.read()
        tree = json.loads(raw)
        root = findRoot(tree, raw)

        newtree = {}
        enumerateByLayer(root, 0, newtree, tree)

        debug = 0
    
    with open(fout, 'w') as f:
        f.write(json.dumps(newtree))

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as jsonfile:
        raw = jsonfile.read()
        tree = json.loads(raw)
        root = findRoot(tree, raw)

        newtree = {}
        gradoAntenati(root, 0, y, tree, newtree)

        debug = 0

    with open(fout, 'w') as f:
        f.write(json.dumps(newtree))



# cancella_sottoalbero('Alb50000.json','zarzuela', "tAlb50000_2.json")