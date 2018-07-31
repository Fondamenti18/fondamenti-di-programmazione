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

def genera_sottoalbero(fnome, x, fout):
    '''inserire qui il vostro codice'''
    with open(fnome,encoding ='utf-8') as f: #open json
        diz = json.load(f)
    if x in diz.keys(): #if key x in json dict
        diz0 = genera_sottoalberoNS(diz, x,dizF=dict()) #create tree with that key // must specify dizF = empty
    with open(fout, 'w') as g: #save it
        json.dump(diz0, g)


def genera_sottoalberoNS(diz, x, dizF = {}):
    dizF[x] = diz[x] #funct that create a tree without save it
    child = diz[x]
    if len(child) > 0:
        for c in child:
            genera_sottoalberoNS(diz,c, dizF)  # recursive call on single child
    return dizF


def cancella_sottoalbero(fnome, x, fout):
    '''inserire qui il vostro codice'''
    with open(fnome, encoding='utf-8') as f:
        diz = json.load(f)
    if x not in diz.keys():
        with open(fout, 'w') as g:
            json.dump(diz, g)  # there isnt x ==> dont mod fnome/tree
    else:
        root_org = find_root(diz)
        diz_org = genera_sottoalberoNS(diz, root_org, dizF=dict()) #original tree
        dizD = genera_sottoalberoNS(diz,x, dizF=dict())  # subtree to delete
        keyO = sorted(diz_org.keys()) #list key original dict
        keyD = sorted(dizD.keys()) #list key dict to delete
        for k in keyD: #remove k
            del diz_org[k]
        for v in diz_org.values():
            if x in v:
                v.remove(x)  # remove leaf
        with open(fout, 'w') as g:  # save new dict/tree
            json.dump(diz_org, g)


def dizionario_livelli(fnome, fout):
    '''inserire qui il vostro codice'''
    with open(fnome, encoding='utf-8') as f:
        diz = json.load(f)
    c = -1
    if c == -1:  # must find the root
        root = find_root(diz)
    diz1 = lvl(diz, root, c, dizR=dict())
    with open(fout, 'w') as g:
        json.dump(diz1, g)


def lvl(diz, root, c, dizR={}):
    c += 1 #funct that save the lvl of a node and,in case ,increase it by one
    if c not in dizR.keys():
        dizR[c] = [root]
    else:
        dizR[c].append(root)
        dizR[c].sort()
    for k in diz[root]:
        lvl(diz, k, c, dizR)
    return dizR


def dizionario_gradi_antenati(fnome, y, fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        diz = json.load(f)
    ROOT = find_root(diz)
    diz_gradi = gradi(diz, ROOT, y, r=dict())
    with open(fout, 'w') as g:
        json.dump(diz_gradi, g)


def find_root(diz):
    setK = set()
    for values in diz.values():  # set with keys
        for v in values:
            setK.add(v)
    for key in diz.keys():  # root
        if key not in setK:
            ROOT = key
    return ROOT


def gradi(diz_input, root, grado, r={}, v=0):
    if len(r) == 0:  # set root
        r[root] = 0
    else:
        if (len(diz_input[root]) > 0) and (len(diz_input[root]) == grado):  # recursive case for other child
            r[root] = v
            v += 1 #if a leaf has child increase
        else:
            r[root] = v  # if child is a leaf dont touch V
    for k in diz_input[root]:
        gradi(diz_input, k, grado, r, v)
    return r

