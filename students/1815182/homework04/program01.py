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

def partenza(fnome):
    f=open(fnome, 'r')
    diz=json.load(f)
    f.close()
    l1=set()
    l2=set()
    for v in diz.values():
        for j in v:
            l1.add(j)
    for k in diz.keys():
        if k not in l1:
            l2=k
    return l2

def level_dict(adj_list,curr_elems,order=0):
    f=open(adj_list, 'r')
    diz=json.load(f)
    f.close()
    if not curr_elems:
        return {}
    d = {}
    new_elems = []
    for elem in curr_elems:
        d.setdefault(order,[]).append(elem)
        new_elems.extend(diz.get(elem,[]))
    d.update(level_dict(adj_list,new_elems,order+1))
    d2 = {x:sorted(d[x]) for x in d.keys()}
    return d2   

def figli(ret, x, diz):
    for j in diz[x]:
        ret[x]=diz[x]
        ret[j]=[]
        figli(ret, j, diz)
    return ret
    
def figli1(ret, x, y, diz, cont=0):
    ret[x]=cont
    for j in diz[x]:
        if len(diz[x])==y:
            figli1(ret, j, y, diz, cont+1)
        else:
            figli1(ret, j, y, diz, cont)
    return ret

def figli3(ret, x, diz):
    for j in diz[x]:
        ret[x]=diz[x]
        ret[j]=[]
        figli(ret, j, diz)
    n={k: v for k, v in diz.items() if k not in ret}
    return n
            
def genera_sottoalbero(fnome,x,fout):
    f=open(fnome, 'r')
    diz=json.load(f)
    f.close()
    ret={}
    figli(ret, x, diz)
    j=open(fout, 'w')
    json.dump(ret, j)
    j.close()
    return ret


def cancella_sottoalbero(fnome,x,fout):
    f=open(fnome, 'r')
    diz=json.load(f)
    f.close()
    ret={}
    ret[x]=diz[x]
    k=figli3(ret, x, diz)
    l=k.values()
    for el in l:
        for j in el:
            if j==x:
                el.remove(j)
    j=open(fout, 'w')
    json.dump(k, j)
    j.close()
    return k


def dizionario_livelli(fnome,fout):
    x=[partenza(fnome)]
    l=level_dict(fnome, x, order=0)
    j=open(fout, 'w')
    json.dump(l, j)
    j.close()
    return l      

def dizionario_gradi_antenati(fnome,y,fout):
     f=open(fnome, 'r')
     diz=json.load(f)
     f.close()
     ret={}
     p=partenza(fnome)
     figli1(ret, p, y, diz)       
     j=open(fout, 'w')
     json.dump(ret, j)
     j.close()
     return ret