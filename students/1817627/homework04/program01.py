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
- il nome di un file json contenente un dizionario-albero  d (fnome)
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
- il nome di un file json contenente un dizionario-albero  d (fnome)
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

def genera(dizioalb,x):
    dicto={x:dizioalb[x]}
    for k in dizioalb[x]:
        dicto.update(genera(dizioalb,k))
    return dicto

def genera_sottoalbero(fnome,x,fout):
    dizioalb=open(fnome)
    dizioalb=json.load(dizioalb)
    dicto=genera(dizioalb,x)
    with open(fout, 'w') as f:
        json.dump(dicto,f)

    
def cancella_sottoalbero(fnome,x,fout):
    dizioalb=open(fnome)
    dizioalb=json.load(dizioalb)
    dicto=genera(dizioalb,x)
    for p in dicto:
        dizioalb.pop(p)
    for el in dizioalb:
        if x in dizioalb[el]:
            dizioalb[el].remove(x)
    with open(fout, 'w') as f:
        json.dump(dizioalb,f)


def levels(dizioalb,elemento,livello,dizio):
    chiavi=dizio.keys()
    if livello not in chiavi:
        dizio[livello]=[]
    dizio[livello]=dizio[livello]+[elemento]
    for k in dizioalb[elemento]:
        levels(dizioalb,k,str(int(livello)+1),dizio)
    return dizio
        

def dizionario_livelli(fnome,fout):
    dizioalb=open(fnome)
    dizioalb=json.load(dizioalb)
    rad=radice(dizioalb)
    dicto=levels(dizioalb,rad,'0',{})
    for a,b in dicto.items():
        dicto[a]=sorted(dicto[a])
    with open(fout, 'w') as f:
        json.dump(dicto,f)
    
    
    
def antenati(dizio,el,y,cont,dicto):
    dicto[el]=cont
    for k in dizio[el]:
        
        if len(dizio[el])==y:
            dicto=antenati(dizio,k,y,cont+1,dicto)
        else:
            dicto=antenati(dizio,k,y,cont,dicto)
    return dicto
    
def dizionario_gradi_antenati(fnome,y,fout):
    lista=[]
    dizio=open(fnome)
    dizio=json.load(dizio)
    for x in dizio.keys():
        lista.append(x)
    cont=0
    rad=radice(dizio)
    dicto=antenati(dizio,rad,y,cont,{})
    with open(fout, 'w') as f:
        json.dump(dicto,f)


            
def radice(dizio):
    a=list(dizio.values())
    insieme=set()
    for y in range(len(a)):
        for x in range(len(a[y])):
            insieme.add(a[y][x])
    for key in dizio:
        if key not in insieme:
            return key            
