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

def read(file):
    f = open(file, "r")
    data = f.read()
    f.close()
    return data

def write(data, file):
    f = open(file, "w")
    json.dump(data, f)
    f.close()

def add(res, d, x):
    res[x] = d[x]
    for el in d[x]:
        res[el] = d[el]
        add(res, d, el)
    return res

def genera_sottoalbero(fnome, x, fout):
    '''inserire qui il vostro codice'''
    d = json.loads(read(fnome))
    res = dict()
    add(res, d, x)
    write(res, fout)

def delete(d, x):
    for el in d[x]:
        delete(d, el)
    del d[x]

def cancella_sottoalbero(fnome, x, fout):
    '''inserire qui il vostro codice'''
    d = json.loads(read(fnome))
    delete(d, x)
    for el in d:
        if x in d[el]:
            d[el].remove(x)
    write(d, fout)

def set_livelli(res, liv, el ,d):
    if d[el] == []:
        return
    if liv in res.keys():
        res[liv] += d[el]
    else:
        res[liv] = d[el]
    res[liv] = sorted(res[liv])
    liv += 1
    for x in d[el]:
        set_livelli(res, liv, x ,d)

def get_padre(d):
    chiavi = list(d.keys())
    valori = list(d.values())
    for child in valori:
        for el in child:
            chiavi.remove(el)
    return chiavi[0]

def dizionario_livelli(fnome, fout):
    '''inserire qui il vostro codice'''
    d = json.loads(read(fnome))
    res = dict()
    el = get_padre(d)
    res[0] = [el]
    set_livelli(res, 1, el, d)
    write(res, fout)

def prec(p, d, x, y):
    if x not in p.keys():
        return 0
    val = len(d[p[x]])
    if val == y:
        return prec(p, d, p[x], y) + 1
    else:
        return prec(p, d, p[x], y)

def dizionario_gradi_antenati(fnome, y, fout):
    '''inserire qui il vostro codice'''
    d = json.loads(read(fnome))
    res = dict()
    p = dict()
    for x in d:
        res[x] = 0
        sub = d[x]
        for el in sub:
            p[el] = x
    for x in d:
        res[x] += prec(p, d, x, y)
    write(res, fout)
