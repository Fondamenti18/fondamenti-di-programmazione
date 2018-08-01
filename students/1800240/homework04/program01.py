# -*- coding: utf-8 -*-
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

def genera(diz, sub_diz, x):
    
    if x in diz:
        sub_diz[x] = diz[x]
        for f in diz[x]:
            genera(diz, sub_diz, f)    
    
def genera_sottoalbero(fnome,x,fout):
        
    diz = json.load(open(fnome))  
    sub_diz = dict()
    
    genera(diz, sub_diz, x)
    
    with open(fout, 'w') as f:
        json.dump(sub_diz, f)
        
def canc(diz, c_diz, x):
            
    if x in diz:
        del c_diz[x]
        for f in diz[x]:
            canc(diz, c_diz, f)
    
def cancella_sottoalbero(fnome,x,fout):

    diz = json.load(open(fnome))
    
    c_diz = diz.copy()
    
    canc(diz, c_diz, x)
    
    for c in diz:
        if x in diz[c]:
            diz[c].remove(x)
       
    with open(fout, 'w') as f:
        json.dump(c_diz, f)
        
def valori(diz):
    
    values = set()
    
    for lista in list(diz.values()):
        if lista != []:
            for valore in lista:
                values.add(valore)
    
    return values

def get_rad(diz):
    
    insieme_valori = valori(diz)
    
    for chiave in diz.keys():
        if chiave not in insieme_valori:
            return chiave
    
def livelli(diz, chiave, diz_lvl, livello):
    
    if diz[chiave] != []:
        diz_lvl[livello] += diz[chiave]
        diz_lvl[livello].sort()
        livello += 1
        for figlio in diz[chiave]:
            livelli(diz, figlio, diz_lvl, livello)
    else:
        pass
        
def dizionario_livelli(fnome,fout):
    
    diz = json.load(open(fnome))
    diz_lvl = dict()
    risultato = dict()
    
    n = 0
    livello = 1
    radice = get_rad(diz)

    for lista in list(diz.values()):
        if lista != []:
            diz_lvl[n] = []
            n += 1
     
    diz_lvl[0] = [radice]
    
    livelli(diz, radice, diz_lvl, livello)

    for c in diz_lvl:
        if diz_lvl[c] != []:
            risultato[c] = diz_lvl[c]
    
    with open(fout, 'w') as f:
         json.dump(risultato, f)

def dizionario_gradi_antenati(fnome,y,fout):
    ''''''