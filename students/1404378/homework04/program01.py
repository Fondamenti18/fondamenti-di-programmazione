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

from collections import defaultdict
import json

def load(file):
    with open(file, 'r') as f:
        return json.load(f)

def write(dic, fout):
    with open(fout, 'w') as f:
        f.write(json.dumps(dic))
        
def find_root(dic):
    keyset = set()
    childset = set()
    for k in dic.keys():
        keyset.add(k)
    for v in dic.values():
        for c in v:
            childset.add(c)
    return (keyset - childset).pop()
     
def find_subtree(k, dic, res):
    if k not in dic:
        return {}
    res[k] = dic[k]
    for c in dic[k]:
        find_subtree(c, dic, res)
    return res

def map_by_level(dic, x, res, level = 1):
    if dic[x]:
      res[level] += dic[x]
      for el in dic[x]:
          map_by_level(dic, el, res, level +1 )
      return res                    

def map_by_degree(dic, x, deg, res, mas=0):
    if len(dic[x]) == deg:
        mas += 1
    for el in dic[x]:
        res[el] = mas
        map_by_degree(dic, el, deg, res, mas)
    return res
        
def genera_sottoalbero(fnome,x, fout):
    res = {}
    dic = load(fnome)
    write(find_subtree(x, dic, res), fout)


def cancella_sottoalbero(fnome,x,fout):
    res = {}
    dic = load(fnome)
    sub = find_subtree(x, dic, res)
    for v in dic.values():
        if x in v:
           v.remove(x)
           break
    write({key: dic[key] for key in dic.keys() - sub.keys()}, fout)


def dizionario_livelli(fnome,fout):
    d = load(fnome)
    res = defaultdict(list)
    root = find_root(d)
    res[0].append(root)
    by_level = {k: sorted(v) for k, v in map_by_level(d, root, res).items()}
    write(by_level, fout)


def dizionario_gradi_antenati(fnome,y,fout):
    d = load(fnome)
    res = {}
    root = find_root(d)
    res[root] = 0
    write(map_by_degree(d, root, y, res), fout)
