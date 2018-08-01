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

def load(fnome):
    #funzione che carica un file di formato .json
    with open(fnome) as json_data:
        d=json.load(json_data)
        json_data.close()
    return d

def save(fout, d):
    #funzione che salva in un file in formato .json
    with open(fout, 'w') as f:
        json.dump(d, f)

def sub(diz, x, s):
    #funzione che calcola il sottoalbero radicato in x RICORSIVAMENTE
    l=[]
    for key in diz:
        for v in diz[x]:
            l.append(v)
            s=sub(diz, v, s)
        if len(l) <= len(diz[x]):
            s[x]=l
            break
    return s

def level(key, diz, lev, dict_level, l):
    #funzione che calcola i livelli dei nodi
    l=[]
    for value in diz[key]:
        l.append(value)
        if len(l)!=len(diz[key]):
            dict_level[lev]=l
            dict_level=level(value, diz, lev, dict_level, l)
        else:
            lev+=1
            dict_level[lev]=l
            dict_level=level(value, diz, lev, dict_level, l)
    #trovare il modo di non cancellare la lista contenente i cugini dalla lista
    return dict_level

def father(diz, k):
    for key in diz.keys():
        if k in diz[key]:
            return key
    return None

'''def level(key, diz, lev, dict_level, l):
    if diz[key]==[]:
        return dict_level
    else:
        for value in diz[key]:
            f=father(diz, value)
            if lev in dict_level:
                lev += 1
            dict_level[lev]=diz[key]
            dict_level=level(value, diz, lev, dict_level, l)
    return dict_level'''

def grade(diz, y, key, conta, i):
    if len(diz[key])==y:
        i+=1
    for value in diz[key]:
        conta[value]=i
        conta=grade(diz, y, value, conta, i)
    return conta

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    dict_tree=load(fnome)
    s={}
    subtree=sub(dict_tree, x, s)
    return save (fout, subtree)

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    dict_tree=load(fnome)
    s={}
    subtree = sub(dict_tree, x, s)
    final_tree={}
    l=[]
    for key in dict_tree:
        if key not in subtree:
            for value in dict_tree[key]:
                if value not in subtree:
                    l.append(value)
            final_tree[key]=l
            l=[]
    return save (fout, final_tree)

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    dict_tree=load(fnome)
    dict_level={}
    lev=0
    l=[]
    for k in dict_tree:
        key=k
        break
    dict_level[lev]=[key]
    lev+=1
    subtree=level(key, dict_tree, lev, dict_level, l)
    return save (fout, subtree)

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    dict_tree=load(fnome)
    i=0
    conta={}
    for k in dict_tree:
        key=k
        break
    conta[key]=i
    conta_antenati=grade(dict_tree, y, key, conta, i)
    return save (fout, conta_antenati)

#dizionario_livelli('Alb10.json','tAlb10_3.json')