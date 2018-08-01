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

def aprijson(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    
def creajson(filename, cont):
    with open(filename, 'w') as file:
        json.dump(cont, file)
    
def cercalo(alb, x):
    ret={}
    if x not in alb:
        return {}
    ret[x]=alb[x]
    for i in alb[x]:
        ret.update(cercalo(alb,i))
    return ret    
    
def genera_sottoalbero(fnome, x, fout):
    alb = aprijson(fnome)
    ris = cercalo(alb,x)
    creajson(fout, ris)
    
def sottrai(alb, datogl):
    for i in datogl:
        alb.pop(i)
    for k,v in alb.items():
        alb[k]=[item for item in v if item not in datogl.keys()]      
    return alb

def cancellalo(alb, x):
    if x not in alb:
        return alb
    ris=cercalo(alb,x)
    return sottrai(alb,ris)       
    
def cancella_sottoalbero(fnome,x,fout):
    alb = aprijson(fnome)
    ris = cancellalo(alb,x)
    creajson(fout, ris)

def livelli(alb, ret={}):
    lista=[]
    albo={}
    if not alb:
        return ret
    for i in alb:
        if alb[i]==[]:
            q = segui(alb, i)
            lista.append(i)
            if q not in ret:
                ret[q]=[i]
            else:
                ret[q].append(i)
    for k,v in alb.items():
        if alb[k]!=[]:
            albo[k]=[item for item in v if item not in lista]
    return livelli(albo, ret)

def segui(alb, elem, liv=0):
    for k,v in alb.items():
        if elem in v:
            return segui(alb, k, liv+1)
    return liv

def segui2(alb, elem, x, ant=0):
    for k,v in alb.items():
        if elem in v and len(v)!=x:
            return segui2(alb, k, x, ant)
        if elem in v and len(v)==x:
            return segui2(alb, k, x, ant+1)
    return ant

def sort(diz):
    ordi={}
    for k,v in sorted(diz.items()):
        ordi[k]=sorted(v)
    return checkdiz(ordi)

def checkdiz(diz):
    rito={}
    for k,v in diz.items():
        ls=[]
        for i in v:
            if len(i)!=1:
                ls.append(i)
        rito[k]=ls
    return rito
        
def dizionario_livelli(fnome,fout):
    alb = aprijson(fnome)
    res = livelli(alb)
    creajson(fout, sort(res))
    
def gradiant(alb,y):
    ret={}
    for i in alb.keys():
        m = segui2(alb, i, y)
        ret[i]=m
    return ret


def dizionario_gradi_antenati(fnome,y,fout):
    alb=aprijson(fnome)
    res=gradiant(alb,y)
    creajson(fout, res)