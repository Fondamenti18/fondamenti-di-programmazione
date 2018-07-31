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

def trova(diz,x): #funzione che trova i nodi appartenenti al sottoalbero da cercare
    diz2={}
    if not x in diz:
        return diz2
    else:
        list= diz.get(x)
        diz2[x]=list
        if len(list)>0:
            for i in list:
                diz2.update(trova(diz,i))
    return diz2

def genera_sottoalbero(fnome,x,fout): #funzione che salva il dizionario contenente il sottoalbero ricercato
    with open(fnome,'r') as f:
        diz=f.read()
        diz=json.loads(diz)
    diz2=trova(diz,x)
    with open(fout,'w') as w:
        json.dump(diz2,w)

def canc(diz,x): #funzione che cancella il sottoalbero di un nodo
    if not x in diz:
        return diz
    else:
        list=diz.get(x)
        del diz[x]
        if len(list)>0:
            for i in list:
                canc(diz,i)

def cancella_sottoalbero(fnome,x,fout): #funzione che salva il dizionario senza il sottoalbero
    with open(fnome,'r') as f:
        diz=f.read()
        diz=json.loads(diz)
    canc(diz,x)
    for key in diz.keys():
        if x in diz[key]:
            lista=diz[key]
            lista.remove(x)
            diz[key]=lista
            break
    with open(fout,'w') as w:
        json.dump(diz,w)

def trova_rad(diz,key): #funzione che trova la radice dell'albero
    items=list(diz.items())
    c=key
    i=0
    while i<len(items):
        if c not in (items[i])[1]:
            i+=1
        else:
            c=trova_rad(diz,(items[i])[0])
    return c

def level(diz,radice): #funzione che indica il livello a cui si trova il nodo
    diz2={}
    l=0
    rad=diz.get(radice)
    diz2[l]=[radice]
    while len(rad)>0:
        lista=[]
        l+=1
        for i in rad:
            lista+=diz.get(i)
        diz2[l]=sorted(rad)
        rad=lista
    return diz2
    

def dizionario_livelli(fnome,fout): #funzione che torna il dizionario con i livelli dei nodi
    with open(fnome,'r') as f:
        diz = f.read()
        diz = json.loads(diz)
    chiavi=list(diz.keys())
    rad=trova_rad(diz,chiavi[round(len(chiavi)/2)])
    diz2=level(diz,rad)
    with open(fout,'w') as w:
        json.dump(diz2, w)

def conta_ant(diz,y,radice,n): #conta il numero di antenati con un certo grado
    diz2={}
    n=n
    diz2[radice] = n
    if len(diz.get(radice))==y:
        n+=1
    for i in diz.get(radice):
        diz2.update(conta_ant(diz,y,i,n))
    return diz2

def dizionario_gradi_antenati(fnome,y,fout): #funzione che torna il dizionario con il numero di antenati di un  certo grado dei nodi
    with open(fnome,'r') as f:
        diz= f.read()
        diz= json.loads(diz)
    chiavi = list(diz.keys())
    rad = trova_rad(diz, chiavi[round(len(chiavi)/2)])
    diz2=conta_ant(diz,y,rad,0)
    with open(fout,'w') as w:
        json.dump(diz2, w)
