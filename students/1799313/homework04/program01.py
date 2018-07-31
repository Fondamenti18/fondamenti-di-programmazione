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
def risotto(diz,x,fdiz):
    for key in diz:
        if key==x:
            fdiz[key]=diz[key]
            for h in diz[key]:
                risotto(diz,h,fdiz)
    return fdiz

def genera_sottoalbero(fnome,x,fout):
    diz=json.load(open(fnome))
    fdiz={}
    if x in diz:
        fdiz=risotto(diz,x,fdiz)
    json.dump(fdiz,open(fout,'w'))
    
def cancella_sottoalbero(fnome,x,fout):
    diz=json.load(open(fnome))
    fdiz={}
    nuovodiz={}
    if x in diz:
        fdiz=risotto(diz,x,fdiz)
    for i in fdiz:
        del diz[i]
    nuovodiz=diz.copy()
    for o in diz:
        if x in diz.get(o):
            ls=diz.get(o)
            if x in ls:
                ls.remove(x)
            nuovodiz.pop(o,x)
            nuovodiz[o]=ls
    json.dump(nuovodiz,open(fout,'w'))
    
def levellino(diz,fdiz,ordina,radice):
    listone=[]
    listone+=[radice]
    if ordina in fdiz:
        listone+=fdiz[ordina]
        listone.sort()
        fdiz[ordina]=listone
    else:
        fdiz[ordina]=listone
    
    childrens=diz[radice]
    if len(childrens)>0:
        for children in childrens:
            fdiz=levellino(diz,fdiz,ordina+1,children)
    return fdiz

def dizionario_livelli(fnome,fout):
    diz=json.load(open(fnome))
    radice=chicercatrova(diz)
    ordina=0
    fdiz={}
    fdiz=levellino(diz,fdiz,ordina,radice)
    json.dump(fdiz,open(fout,"w"))    
 
def parents(diz,fdiz,ordina,y,radice):
    fdiz[radice]=ordina
    childrens=diz[radice]
    if len(childrens)==y:
        ordina+=1
    for children in childrens:
        fdiz=parents(diz,fdiz,ordina,y,children)
    return fdiz

def dizionario_gradi_antenati(fnome,y,fout):
    diz=json.load(open(fnome))
    fdiz={}
    radice=chicercatrova(diz)
    ordina=0
    fdiz=parents(diz,fdiz,ordina,y,radice)
    json.dump(fdiz,open(fout,"w"))   

def chicercatrova(diz):
    children=next(iter(diz.keys()))
    r=rad(diz,children)
    return r

def rad(diz,children): 
    risul=children
    for i,l in diz.items():
        if children in l:
            risul=rad(diz,i)
    return risul

