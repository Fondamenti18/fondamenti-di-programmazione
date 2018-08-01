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

- il nome di un file json contenente un dizionario-albero  d (fnome)
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

- il nome di un file json contenente un dizionario-albero  d (fnome)
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
from collections import OrderedDict
import sys

class lv:
    def __init__(self,val):
        self.val = val
        self.lv = 0
        self.antenati = 0

def gen_alberodiz(d, x):
    dreturn = {}
    dreturn[x] = sorted(d[x])
    if d[x] == []: 
        return dreturn
    for i in d[x]:
        dtemp = gen_alberodiz(d, i)
        for key in dtemp:
            dreturn[key] = dtemp[key] 
    return dreturn

def contalivello(d, x, dlv = {}):
    y = lv(x)  
    for i in d:
        if x in d[i]:
            if i in dlv:
                y.lv = 1 + dlv[i].lv
                dlv[x] = y
                return y.lv
            y.lv += 1 + contalivello(d, i, dlv)
    dlv[x] = y
    return y.lv

def ricorsione(lista,ins = set()):
    if lista:
        ins.add(lista[0])
        ins.update(ricorsione(lista[1:], ins))
    return ins

def genera_sottoalbero(fnome, x, fout = None):
    with open(fnome) as json_data:
        d = json.load(json_data)
    
    dr = gen_alberodiz(d, x)

    with open(fout, 'w') as outfile:
        json.dump(dr, outfile)
    
        

def cancella_sottoalbero(fnome, x, fout):
    with open(fnome) as json_data:
        d = json.load(json_data)
    
    dcanc = gen_alberodiz(d, x)
    for i in dcanc:
        del d[i]
    for i in d:
        if x in d[i]:
            d[i].remove(x)

    with open(fout, 'w') as outfile:
        json.dump(d, outfile)
    

def dizionario_livelli(fnome, fout):
    sys.setrecursionlimit(1500)
    with open(fnome) as json_data:
        d = json.load(json_data)
    dreturn = {}
    ins = ricorsione(list(d.keys()))
    flag = False
    if len(next(iter(ins))) > 1:
        flag = True 
    for i in ins:
        if contalivello(d, i) in dreturn:
            if flag:
                if len(i) == 1:
                    continue
            dreturn[contalivello(d, i)] += [i]
        else:
            if flag:
                if len(i) == 1:
                    continue
            dreturn[contalivello(d, i)] = [i]
        dreturn[contalivello(d, i)] = sorted(dreturn[contalivello(d, i)])
    
    dreturn = dict(OrderedDict(sorted(dreturn.items())))

    with open(fout, 'w') as outfile:
        json.dump(dreturn, outfile)
 

def dizionario_gradi_antenati(fnome, y, fout):
    sys.setrecursionlimit(1500)
    with open(fnome) as json_data:
        d = json.load(json_data)

    dreturn = {}
    ins = ricorsione(list(d.keys()))
    flag = False
    if len(next(iter(ins))) > 1:
        flag = True 
    for i in ins:
        if flag:
            if len(i) == 1:
                continue
        contatore = 0
        genitori = set()
        figlio = i
        while True:
            flag = False
            for x in d:
                if figlio in d[x]:
                    genitori.add(x)
                    figlio = x
                    flag = True
                    break
            if flag == False:
                break    
        for x in d:
            if len(d[x]) == y and x in genitori:
                contatore += 1
            dreturn[i] = contatore

    dreturn = dict(OrderedDict(sorted(dreturn.items())))

    with open(fout, 'w') as outfile:
        json.dump(dreturn, outfile)
