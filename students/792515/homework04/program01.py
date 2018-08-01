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
#import datetime

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as f:
        dzFailetto=json.load(f)
    dzOut={}
    dzOut=sotto_albero(x,dzFailetto,dzOut)
    with open(fout,'w') as f:
        json.dump(dzOut,f)
    return

def sotto_albero(x,dz,dzs):
    if not x in dz.keys():
        return dzs
    else:
        dzs[x]=dz[x]
        for elemento in dz[x]:
            sotto_albero(elemento,dz,dzs)
    return dzs

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as f:
        dzFailetto=json.load(f)
    dzOut=dzFailetto
    dzOut=genera_sopra_albero(x,dzOut)
    dzOut=pulisci_sopra_albero(x,dzOut)
    with open(fout,'w') as f:
        json.dump(dzOut,f)
    return

def genera_sopra_albero(x,dz):
    if not x in dz.keys():
        return dz
    else:
        lsrimuovere=dz[x]
        del(dz[x])
        for elemento in lsrimuovere:
            genera_sopra_albero(elemento,dz)
    return dz

def pulisci_sopra_albero(x,dz):
    for chiave in dz.keys():
        if x in dz[chiave]:
            dz[chiave].remove(x)
            return dz

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as f:
        dzFailetto=json.load(f)
    dzOut={}
    
    radice=ricerca_radice(dzFailetto)
    dzOut=calcola_livello(0,radice,dzFailetto,dzOut)
    
    with open(fout,'w') as f:
        json.dump(dzOut,f)
    return 
    
def ricerca_radice(dz):    
    lselementi=[]
    for elemento in dz.items(): #ricerca radice
        lselementi+=elemento[1]
    return list(set(dz.keys())-set(lselementi))[0]

def calcola_livello(livello,nodi,dz,dzl):
    if not livello in dzl.keys():
        dzl[livello]=[nodi]
    else:
        dzl[livello]+=[nodi]
        dzl[livello].sort()
    lsricerca=dz[nodi]
    for r in lsricerca:
        calcola_livello(livello+1,r,dz,dzl)
    return dzl

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as f:
        dzFailetto=json.load(f)
    dzOut={}
    dzgenitori={}
    lsfoglie=[]
    
    radice=ricerca_radice(dzFailetto)

    #ora=datetime.datetime.now()
    dzOut[radice]=0
    calcola_grado(dzFailetto,dzOut,radice,y,0)
    with open(fout,'w') as f:
        json.dump(dzOut,f)
    return

def calcola_grado(dzI,dzO,r,y,avi):
    newavi=avi
    if len(dzI[r])==y:
        newavi+=1
    for d in dzI[r]:
        dzO[d]=newavi
        calcola_grado(dzI,dzO,d,y,newavi)
    return dzO