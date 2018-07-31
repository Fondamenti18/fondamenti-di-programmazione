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
import time


class memoize(dict):

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args):
        return self[args]

    def __missing__(self, args):
        self[args] = self.fn(*args)
        return self[args]


@memoize
def load_tree(file_name):
    with open(file_name) as f:
        tree = json.load(f, encoding='utf-8')
        return (tree, find_root(tree))

def save_tree(file_name, tree):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(tree))

def flatten_lists(lists):
    return [item for list_item in lists for item in list_item]

def find_root(tree):
    child_nodes = tree.values()
    root_node = (tree.keys() - flatten_lists(child_nodes)).pop()

    return root_node

def get_subtree(node, tree):
    subtree = {
        node: [n for n in tree[node]]
    }
    for child in tree[node]:
        subtree.update(get_subtree(child, tree))

    return subtree


def del_subtree(node_del, tree):
    subtree = get_subtree(node_del, tree)

    removed_keys = subtree.keys()
    new_keys = tree.keys() - removed_keys
    new_tree = {}
    for key in new_keys:
        new_tree[key] =  [n for n in tree[key] if n != node_del]

    return new_tree


def get_levels(node, tree, level=0, levels = None):    
    if level not in levels:
        levels[level] = [node]
    else:
        levels[level].append(node)

    for child in tree[node]:
        get_levels(child, tree, level + 1, levels)


def get_ancestors_count(node, tree, grade, parents=0):
    grades = {
        node: parents
    }
    
    if len(tree[node]) == grade:
        parents = parents + 1

    for child in tree[node]:
        grades.update(get_ancestors_count(child, tree, grade, parents))

    return grades


def genera_sottoalbero(fnome, x, fout):
    '''inserire qui il vostro codice'''

    tree, _ = load_tree(fnome)
    subtree = get_subtree(x, tree)

    save_tree(fout, subtree)

    return subtree


def cancella_sottoalbero(fnome, x, fout):
    '''inserire qui il vostro codice'''

    tree, _ = load_tree(fnome)
    new_tree = del_subtree(x, tree)

    save_tree(fout, new_tree)


    return new_tree


def dizionario_livelli(fnome, fout):
    '''inserire qui il vostro codice'''

    tree, root = load_tree(fnome)

    levels = {}
    get_levels(root, tree, levels=levels)

    for level in levels:
        levels[level] = sorted(levels[level])

    save_tree(fout, levels)

    return levels


def dizionario_gradi_antenati(fnome, y, fout):
    '''inserire qui il vostro codice'''

    tree, root = load_tree(fnome)
    grades = get_ancestors_count(root, tree, y)

    save_tree(fout, grades)

    return grades


if __name__ == '__main__':
    # print(genera_sottoalbero('Alb10.json','d','tAlb10_1.json'))
    print(cancella_sottoalbero('Alb10.json','d','tAlb10_2.json'))
    # print(dizionario_livelli('Alb10.json','tAlb10_1.json'))
    # print(dizionario_gradi_antenati('Alb20000.json', 2, 'tAlb20000_4.json'))
