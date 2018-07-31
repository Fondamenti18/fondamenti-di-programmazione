"""
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
"""
import json


def find_root(tree):
    element_set = set()
    for e in tree:
        element_set.update(tree[e])

    return list(set(tree.keys()) - element_set)[0]


def create_subtree(node, tree, subtree):
    subtree.update({node: tree[node]})
    for c in tree[node]:
        subtree = create_subtree(c, tree, subtree)

    return subtree


def find_children(node, tree):
    c = [node]
    for subnode in tree[node]:
        c += find_children(subnode, tree)

    return c


def find_father(node, last_father, tree, result):
    if not last_father:
        result.update({node: []})

    for e in tree[node]:
        result.update({e: [node] + result[node]})
        result = find_father(e, node, tree, result)

    return result


def find_level(node, tree, level, result):
    if level not in result:
        result.update({level: [node]})
    else:
        result[level].append(node)

    for subnode in tree[node]:
        result = find_level(subnode, tree, level + 1, result)

    return result


def genera_sottoalbero(fnome, x, fout):
    tree = json.load(open(fnome))
    sub_tree = create_subtree(x, tree, {})
    json.dump(sub_tree, open(fout, "w"))


def cancella_sottoalbero(fnome, x, fout):
    tree = json.load(open(fnome))
    esclude = find_children(x, tree) if x in tree else []
    new_tree = {k: v if x not in v else [c for c in v if c != x]
                for k, v in tree.items() if k not in esclude}
    json.dump(new_tree, open(fout, "w"))


def dizionario_livelli(fnome, fout):
    tree = json.load(open(fnome))
    result = find_level(find_root(tree), tree, 0, {})
    for k in result:
        result[k].sort()

    json.dump(result, open(fout, "w"))


def dizionario_gradi_antenati(fnome, y, fout):
    tree = json.load(open(fnome))
    children_tree_set = {x for x in {k: len(v) for k, v in tree.items() if len(v) == y}.keys()}
    father_tree = find_father(find_root(tree), None, tree, {})
    result = {}

    for node in tree:
        result.update({node: len(children_tree_set & set(father_tree[node]))})

    json.dump(result, open(fout, "w"))
