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



from json import load
import json
from copy import deepcopy
from collections import defaultdict
from itertools import chain

def genera_sottoalbero(fnome,x,fout):
    from json import load
    d = {}
    with open(fnome) as f :
        a = load(f)
    r = calcolo(a,x,d)
    data = json.dumps(r)
    with open(fout , "w") as f :
        f.write(data)
def calcolo(a,x,d):
    if x in a.keys() :
        v = a[x]
        d[x] = v
        for i in v :
            calcolo(a,i,d)
    return d
            
    
def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as f :
        a = load(f)
        d = deepcopy(a)
        for k,v in d.items():
            if x in v :
                v.remove(x)
                break
    d = elimina(a,x,d)
    data = json.dumps(d)
    with open(fout , "w") as f :
        f.write(data)
def elimina(a,x,d):
    if x in a.keys():
        v = a[x]
        d.pop(x)
        for i in v :
            elimina(a,i,d)
    return d
            
            
def dizionario_livelli(fnome,fout):
    from json import load
    c = 0
    diz={}
    i=[]
    with open(fnome) as f :
        a = load(f)
        roots = set(a).difference(chain.from_iterable(a.values()))
        b = "".join(list(roots))
        i.append(b)
    d = livelli(a,diz,i,c)
    data = json.dumps(d)
    with open(fout , "w") as f :
        f.write(data)
def livelli(a,d,i,c):
    l=[]
    if len(i)==0:
        return d
    else:
        d[c]=[]
        for x in i:
            d[c].append(x)
            l+=a[x]
        d[c].sort()
        livelli(a,d,l,c+1)
    return d
    
    
 

def dizionario_gradi_antenati(fnome,y,fout):
    from json import load
    d = {}
    c = 0
    with open(fnome) as f :
        a = load(f)
        roots = set(a).difference(chain.from_iterable(a.values()))
        i = "".join(list(roots))
        d[i] = 0
    r = albero(a,y,c,d,i)
    data = json.dumps(r)
    with open(fout , "w") as f :
        f.write(data)
def albero(a,y,c,d,i):
    v = a[i]
    if len(v) == y :
        c = c + 1
    for x in v :
        d[x] = c
        albero(a,y,c,d,x)
    return d

        
                
            
        
