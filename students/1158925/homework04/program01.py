'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero	 e l'attributo della chiave e' la lista
(eventualmente vuota) degli identificativi dei	figli del nodo. Gli identificativi dei nodi
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
               |							|
              'c'				   ________'d'_______
               |				  |					 |
              'i'		  _______'e'_______			'l'
                         |		  |		   |
                        'f'		 'g'	  'h'


Implementare le seguenti funzioni:

1)
la funzione genera_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

produce	  il  dizionario-albero che rappresenta	  il sottoalbero  radicato
nell'identificativo x che si ottiene dal dizionario-albero d.
Il dizionario-albero ottenuto va registrato nel file fout.
Se l'identificativo x non e' tra i nodi di d allora	 il dizionario-albero prodotto
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

ricava	da d il sottoalbero radicato in x e lo salva nel file fout.
Se x non e' presente tra le chiavi di  d allora	 il dizionario-albero d non viene modificato.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di
cancella_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'a': ['b'], 'b': ['c'], 'c': ['i'], 'i':[]}


3)
la funzione dizionario_livelli(fnome, fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- il nome di un file json (fout)

costruisce il  dizionario che ha come  chiavi i livelli del dizionario-albero d. L'attributo di una
chiave di valore x e' la lista degli identificativi	 dei nodi che si trovano a livello x  nell'albero rappresentato da d.
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


def get_childs(tree, x, r):
    if x in tree:
        r[x] = tree[x]
        for child in r[x]:
            get_childs(tree, child, r)

def genera_sottoalbero(fnome,x,fout):

    with open(fnome, "r") as f:
        tree = json.load(f)
    r={}
    get_childs(tree,x,r)
    with open(fout, "w") as f:
        json.dump(r,f)
    return r

def del_childs(tree,x):
    if x in tree:
        for child in tree[x]:
            del_childs(tree,child)
        del tree[x]


def cancella_sottoalbero(fnome,x,fout):

    with open(fnome, "r") as f:
        tree = json.load(f)
    del_childs(tree,x)
    [l.remove(x) for l in tree.values() if x in l]


    with open(fout, "w") as f:
        json.dump(tree,f)

    return tree

def count_level(tree, x, r, i):
    r.setdefault(str(i), [])
    r[str(i)].append(x)

    for child in tree[x]:
        count_level(tree, child, r, i + 1)


def get_root(d,key):

    found = 1
    while found ==1:
        found =0
        for parent,childs in d.items():
            if key in childs:
                key = parent
                found =1
                break

    return key

def dizionario_livelli(fnome,fout):


    with open(fnome, "r") as f:
        tree = json.load(f)
    r={}

    root = get_root(tree,next(iter(tree)))

    count_level(tree,root,r,0)

    for l in r.values():
        l.sort()

    with open(fout, "w") as f:
        json.dump(r,f)
    return r

def count_grades(tree,x,r,y,z):
    r[x] = z
    if len(tree[x]) == y:
        z+=1
    for child in tree[x]:
        count_grades(tree,child,r,y,z)

def dizionario_gradi_antenati(fnome,y,fout):

    '''inserire qui il vostro codice'''
    from collections import OrderedDict
    with open(fnome, "r") as f:
        tree = json.load(f,object_pairs_hook=OrderedDict)

    r={}
    root = get_root(tree,next(iter(tree)))
    count_grades(tree,root, r,y,0)

    with open(fout, "w") as f:
        json.dump(r,f)
    return r

if __name__ == "__main__":
    # print(genera_sottoalbero('Alb10.json','d','tAlb10_1.json'))
    # print(cancella_sottoalbero('Alb10.json','d','tAlb10_2.json'))
    # print(dizionario_livelli('Alb10.json','tAlb10_3.json'))
    print(dizionario_gradi_antenati('Alb50000.json',2,'tAlb50000_4.json'))
    # with open('tAlb50000_4.json', "r") as f:
    # 	d1 = json.load(f)
    # 	with open('risAlb50000_4.json', "r") as f2:
    # 		d2 = json.load(f2)
    #
    # 		for key,value in d1.items():
    # 			if key not in d2 or d2[key] != value:
    # 				print(key, value, d2[key])
    #
    # 		for key,value in d2.items():
    # 			if key not in d1:
    # 				print(key, value)
    # 			elif d1[key] != value:
    # 				print(key, value, d1[key])

