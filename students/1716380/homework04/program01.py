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
dic={}
d={}
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    tree=find_tree(fnome,x)           #ricorsione
    with open(fout,'w') as fo:
        json.dump(tree,fo)
    global dic
    dic={}
def find_tree(fnome,x):                #ricorsione
    global dic
    with open(fnome) as f:
        info=json.load(f)
        for i in info:
            if i == x:
                dic.update({i:info[i]})
                for w in info[i]:
                    find_tree(fnome,w)      #ricorsione
    return dic

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    tree=cancel_tree(fnome,x)
    with open(fout,'w') as f:
        json.dump(tree,f)
    global d
    d={}    
def cancel_tree(fnome,x):                     #ricorsione
    global d
    with open(fnome) as fl:
        info=json.load(fl)
        cinfo=info.copy()
        for i in cinfo:
            if x in cinfo[i]:
                info[i].remove(x)
                info.update({i:info[i]})
        if info[x]==[]:
            d.update({x:info[x]})
        else:
            d.update({x:info[x]})
            for i in info[x]:
                cancel_tree(fnome,i)           #ricorsione
        for i in cinfo:
            if i in d:
                info.pop(i)
    return info
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    global n
    d=[]
    dl={}
    with open(fnome) as f:
        data=json.load(f)
        for i in data:
            nu=count_node(data,i)   #ricorsione
            d.append((nu,i))
            n=0
    for k,v in d:
        dl.setdefault(k,[]).append(v)
    for i in dl:
        dl[i].sort()
    with open(fout,'w') as fo:
        json.dump(dl,fo)
n=0
def count_node(data,i):          #ricorsione
    global n
    for k,v in data.items():
        if i in v:
            n+=1
            count_node(data,k)   #ricorsione
    return n
        
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    global n
    dl={}
    with open(fnome) as f:
        data=json.load(f)
        for k in data:
            nu=find_ancestors(data,k,y)
            dl.update({k:nu})
            n=0
    with open(fout,'w') as fo:
        json.dump(dl,fo)
def find_ancestors(data,i,x):
    global n
    for k,v in data.items():
        if i in v:
            if len(data[k])==x:
                n+=1
            find_ancestors(data,k,x)
    return n