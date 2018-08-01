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
class AlberoDiz:
    def __init__(self,nome,livello):
        self.nome=nome
        self.livello=livello
        self.figli=[]
        
    def __str__(self):
        return "Nodo: "+self.nome

import json
from json import *

def genera_sottoalbero(fnome,x,fout):
    f=open(fnome)
    diz=load(f)
    f.close()
    
    albero=genera(diz,x)
    sottoalbero={}
    converti(albero,sottoalbero)
    
    f=open(fout,'w')
    dump(sottoalbero,f)
    f.close()
    

def cancella_sottoalbero(fnome,x,fout):
    f=open(fnome)
    diz=load(f)
    f.close()
    
    cancella(diz,x)
    
    f=open(fout,'w')
    dump(diz,f)
    f.close()
    

def dizionario_livelli(fnome,fout):
    f=open(fnome)
    diz=load(f)
    f.close()
    
    k=[]
    k+=diz.keys()
    albero=genera(diz,k[0])
    inverso={}
    inverti(albero,inverso)
    
    f=open(fout,'w')
    dump(inverso,f)
    f.close()

def dizionario_gradi_antenati(fnome,y,fout):
    f=open(fnome)
    diz=load(f)
    f.close()
    
    k=[]
    k+=diz.keys()
    albero=genera(diz,k[0])
    antenati={}
    trova_antenato(albero,antenati,y)
    
    f=open(fout,'w')
    dump(antenati,f)
    f.close()

def genera(diz,x,liv=0):
    nodo=None
    if x in diz:
        nodo=AlberoDiz(x,liv)
        for ele in diz[x]:
            if ele in diz:
                nodo.figli+=[genera(diz,ele,liv+1)]
    return nodo

def converti(nodo,diz):
    diz[nodo.nome]=[]
    for figlio in nodo.figli:
        diz[nodo.nome]+=[converti(figlio,diz)]
    return nodo.nome

def cancella(diz,x):
    if x in diz:
        eliminati=diz.pop(x)
        for ele in eliminati:
            cancella(diz,ele)
        for key in diz:
            if x in diz[key]:
                diz[key].remove(x)
                
def inverti(nodo,diz):
    if nodo.livello in diz:
        diz[nodo.livello]+=[nodo.nome]
        diz[nodo.livello].sort()
    else:
        diz[nodo.livello]=[nodo.nome]
    for figlio in nodo.figli:
        inverti(figlio,diz)
        
def trova_antenato(nodo,diz,y,padre=None):
    diz[nodo.nome]=0
    if padre!=None:
        diz[nodo.nome]+=diz[padre.nome]
        if len(padre.figli)==y:
            diz[nodo.nome]+=1
    for figlio in nodo.figli:
        trova_antenato(figlio,diz,y,nodo)