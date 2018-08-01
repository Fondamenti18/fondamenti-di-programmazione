# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:18:01 2017

@author: aless
"""

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

import json

def genera_sottoalbero(fnome,x,fout):
    inserire qui il vostro codice
    

def cancella_sottoalbero(fnome,x,fout):
    inserire qui il vostro codice
    

def dizionario_livelli(fnome,fout):
    inserire qui il vostro codice
 

def dizionario_gradi_antenati(fnome,y,fout):
    inserire qui il vostro codice'''
import json
def genera_figli(diz2,x,diz):
    if x not in diz: return None
    else:
        diz2[x]=diz[x]
        for el in diz[x]:
            diz2[el]=[]
            genera_figli(diz2,el,diz)
    
def genera_sottoalbero(fnome,x,fout):
    diz={}
    with open(fnome,'r') as f:
        diz=json.loads(f.read())
    diz2={}
    genera_figli(diz2,x,diz)
    with open(fout,'w') as f1:
        f1.write(json.dumps(diz2))

def cancella_sottoalbero(fnome,x,fout):
    diz={}
    x1=x
    with open(fnome,'r') as f:
        diz=json.loads(f.read())
    diz2={}
    genera_figli(diz2,x,diz)
    for x in diz2:
        del diz[x]
    for el in diz:
        if x1 in diz[el]:
            diz[el].remove(x1)
    with open(fout,'w') as f1:
        f1.write(json.dumps(diz))
        
def genera_livelli(diz2,x,diz,liv):
    if x not in diz: return None
    else:
        if liv in diz2:
            diz2[liv]+=[x]
        else:
            diz2[liv]=[]    
            diz2[liv]+=[x]
        for el in diz[x]:
                genera_livelli(diz2,el,diz,liv+1)
                
def dizionario_livelli(fnome,fout):
    diz={}
    diz2={}
    with open(fnome,'r') as f:
        diz=json.loads(f.read())
    ins=set(diz.keys())
    for x in diz.keys():
        for j in diz[x]:
            ins.remove(j)
    rad=list(ins)[0]
    genera_livelli(diz2,rad,diz,0)
    for h in diz2:
        diz2[h]=sorted(diz2[h])
    with open(fout,'w') as f1:
        f1.write(json.dumps(diz2))
        
def conta_numeroantenati(n,s,diz,diz2,y):
    diz2[n]=s
    for j in diz[n]:
        if len(diz[n])==y:
            conta_numeroantenati(j,s+1,diz,diz2,y)
        else:
            conta_numeroantenati(j,s,diz,diz2,y)
            
def dizionario_gradi_antenati(fnome,y,fout):
    diz={}
    diz2={}
    with open(fnome,'r') as f:
        diz=json.loads(f.read())
    ins=set(diz.keys())
    for x in diz.keys():
        for j in diz[x]:
            ins.remove(j)
    rad=list(ins)[0]
    conta_numeroantenati(rad,0,diz,diz2,y)
    with open(fout,'w') as f1:
        f1.write(json.dumps(diz2))
        
#dizionario_gradi_antenati('Alb10.json',2,'fout')
