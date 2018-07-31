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

def carica(fnome):
    ''' Funzione che carica un file json'''
    with open(fnome) as json_data:
        diz_alb = json.load(json_data)
        json_data.close()
    return(diz_alb)

def salva(fout,diz):
    ''' Funzione che salva un file in json'''
    with open(fout, 'w') as f:
        json.dump(diz, f)

def trova_radice(diz):
    '''Preso un albero-dizionario ne ritorna la radice'''
    figli = []
    for valore in diz.values():
        for v in valore:
            figli.append(v)
    s_radice = diz.keys() - figli #sottrazione tra 'insiemi'
    s_radice = list(s_radice)
    return s_radice[0]

def trova_nodi(diz,x,ris):
    '''Trova i nodi del sottoalbero radicato in x'''
    while x in diz.keys():
        ris[x] = diz[x]
        if ris[x] == []:
            break
        for el in ris[x]:
            x = el
            ris = trova_nodi(diz,x,ris)
    return ris

def trova_livelli(diz,levels,i,livelli):
    if livelli != []:
        livelli2 = []
        i += 1
        for el in livelli:
            elem = diz[el]
            for e in elem:
                livelli2.append(e)
        levels[i] = livelli2
        levels = trova_livelli(diz,levels,i,livelli2)
    else:
        return levels
    return levels

def trova_grado(diz,diz_ant,n_grado,nodo,y):
    '''Preso in input il numero di antenati di grado y, i nodi figli hanno stesso n_grado del padre se il
    padre ha numero di figli diverso da y, altrimenti n_gradoo dei figli aumenta di 1. La
    funzione lavora ricorsivamente su tutto l'albero'''
    if diz[nodo] == []:
        return diz_ant
    else:
        if len(diz[nodo]) == y:
            n_grado += 1
        for child in diz[nodo]:
            diz_ant[child] = n_grado
            diz_ant = trova_grado(diz,diz_ant,n_grado,child,y)
    return diz_ant

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    ris = {} # dizionario di ritorno
    diz = carica(fnome)
    sotto_alb = trova_nodi(diz,x,ris)
    sotto_alb = salva(fout,ris)

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    ris = {}
    diz = carica(fnome)
    sotto_alb = trova_nodi(diz,x,ris)
    deleted = []
    for k,v in sotto_alb.items():
        if diz[k] == v:
            deleted.append(k) # aggiungo alla lista tutte le chiavi che vengono eliminate
            diz.pop(k) # elimino la chiave del dizionario corrispondente all'elemento che deve essere eliminato
    for val in diz.values(): # elimino anche gli elementi nei valori associati alle chiavi che stanno in deleted (che quindi ho rimosso)
        for el in val:
            if el in deleted:
                val.remove(el)
    new_diz = salva(fout,diz)

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    levels = {}
    diz = carica(fnome)
    i = 0
    radice = trova_radice(diz)
    livelli = [radice]
    levels[i] = livelli
    levels = trova_livelli(diz,levels,i,livelli)
    levels2 = {}
    for k,v in levels.items():
        if v != []:
            v.sort()
            levels2[k] = v
    levels = salva(fout,levels2)

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    diz = carica(fnome)
    radice = trova_radice(diz)
    diz_ant = {}
    n_grado = 0
    nodo = radice
    diz_ant[nodo] = 0
    diz_ant = trova_grado(diz,diz_ant,n_grado,nodo,y)
    antenati = salva(fout,diz_ant)
