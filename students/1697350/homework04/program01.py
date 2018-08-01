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
from collections import defaultdict

'''
def dfs(v, graph):
    seen = set()
    vs = set([v])
    while vs:
        v = vs.pop()
        seen.add(v)
        vs |= set(graph[v]) - seen
    return seen
'''
def dfs(v, graph, vs, seen):
    if not vs:
        return seen
    else:
        v = vs.pop()
        seen.add(v)
        vs |= set(graph[v]) - seen
        dfs(v, graph, vs, seen)
    return seen
    


def findLevel(graph):
    set_childs = set()
    for _, values in graph.items():
        for v in values:
            set_childs.add(v)
    return sorted(list(set(graph.keys() - set_childs)))


def findParents(graph):
    newGraph = dict()
    for key, value in graph.items():
        for v in value:
            newGraph[v] = key
    return newGraph


def findAntenati(nodo, parents):
    setAntenati = set()
    while True:
        parent = parents.get(nodo, None)
        if not parent: break
        setAntenati.add(parent)
        nodo = parent
    return setAntenati


def findNodesOfGrade(grade, graph):
    set_nodes = set()
    for key, value in graph.items():
        if len(value) == grade:
            set_nodes.add(key)
    return set_nodes


def genera_sottoalbero(fnome, x, fout):
    with open(fnome, encoding='utf-8') as f:
        graph = json.loads(f.read())
    if x not in graph:
        return {}
    keys = dfs(x, graph, set([x]), set())
    newGraph = {k: v for k, v in graph.items() if k in keys}
    with open(fout, 'w') as fp:
        json.dump(newGraph, fp)
    return newGraph


def cancella_sottoalbero(fnome, x, fout):
    with open(fnome, encoding='utf-8') as f:
        graph = json.loads(f.read())
    if x not in graph:
        return {}
    keys = dfs(x, graph, set([x]), set())
    copy_graph = graph.copy()
    for key, value in copy_graph.items():
        if key in keys:
            del graph[key]
        if x in value:
            newValue = value.copy()
            newValue.remove(x)
            graph[key] = newValue
    with open(fout, 'w') as fp:
        json.dump(graph, fp)
    return graph


def dizionario_livelli(fnome, fout, graph=None):
    newGraph = defaultdict(list)
    if not graph:
        with open(fnome, encoding='utf-8') as f:
            graph = json.loads(f.read())

    i = 0
    k = list(graph.keys())[0]
    keys = dfs(k, graph, set([k]), set())
    while True:
        level_elements = findLevel(graph)
        for elem in level_elements:
            del graph[elem]

        if len(level_elements) == 0: break
        newGraph[i] = level_elements
        i += 1
    with open(fout, 'w') as fp:
        json.dump(newGraph, fp)
    return newGraph

def dizionario_gradi_antenati(fnome, y, fout):
    with open(fnome, encoding='utf-8') as f:
        graph = json.loads(f.read())
    k = list(graph.keys())[0]
    keys = dfs(k, graph, set([k]), set())
    parents = findParents(graph)
    newDict = {}
    nodesOfGrade = findNodesOfGrade(y, graph)

    for node in graph:
        antenati = findAntenati(node, parents)
        numGradeY = len(list(set.intersection(antenati, nodesOfGrade)))
        newDict[node] = numGradeY
    with open(fout, 'w') as fp:
        json.dump(newDict, fp)
    return newDict





if __name__ == "__main__":
    # genera_sottoalbero('Alb10.json','d','tAlb10_1.json')
    # cancella_sottoalbero('Alb10.json','d','tAlb10_2.json')
    # dizionario_livelli('Alb10.json','tAlb10_3.json')
    dizionario_gradi_antenati('Alb10.json', 2, 'tAlb10_4.json')
