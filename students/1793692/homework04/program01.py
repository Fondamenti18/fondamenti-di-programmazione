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

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    diz=json.load(open(fnome))
    sottoalbero={}
    sottoalbero=subtree(diz,x,sottoalbero) #chiamata funzione ricorsiva
    with open(fout, 'w') as outfile:  
        json.dump(sottoalbero, outfile)

def subtree(tree,x,new):
    new[x]=tree[x]
    if tree[x]==[]:
        new[x]=[]
    for v in tree[x]:
        subtree(tree,v,new) #ricorsione
        new[v]=tree[v]
    return new
    
    

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    diz=json.load(open(fnome))
    sottoalbero={}
    albero={}
    sottoalbero=subtree(diz,x,sottoalbero) #chiamata funzione ricorsiva
    for k in diz:
        if k not in sottoalbero:
            albero[k]=diz[k]
        if x in diz[k]:
            albero[k].remove(x)
    with open(fout, 'w') as outfile:  
        json.dump(albero, outfile)

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    diz=json.load(open(fnome))
    radice=trova_radice(diz)
    alb={}
    livelli={}
    count=0
    livelli[count]=[radice]
    livelli=genera_livelli(diz,radice,alb,count,livelli)#chiamata funzione ricorsiva
    ordina(livelli)
    with open(fout, 'w') as outfile:  
        json.dump(livelli, outfile)
    
def trova_radice(albero):
    chiavi=set(albero.keys())
    valori=set()
    for x in albero.values():
        for y in x:
            valori.add(y)
    rad=chiavi.difference(valori)
    return ''.join(rad)

def genera_livelli(tree,x,new,count,livelli):
    new[x]=tree[x]
    count+=1
    if tree[x]==[]:
        count+=1
        new[x]=[]
    for v in tree[x]:
        genera_livelli(tree,v,new,count,livelli) #ricorsione
        new[v]=tree[v]
        if not count in livelli:
            livelli[count]=[v]
        else:
            livelli[count].append(v)
    return livelli
def ordina(albero):
    for x in albero:
        if x!=0:
            albero[x]=sorted(albero[x])
 

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    diz=json.load(open(fnome))
    radice=trova_radice(diz)
    newalbero={}
    antenati={}
    count=0
    antenati[radice]=count
    antenati=trova_antenati(diz,radice,newalbero,y,antenati,count) #chiamata funzione ricorsiva
    with open(fout, 'w') as outfile:  
        json.dump(antenati, outfile)
    
def trova_antenati(tree,x,new,y,antenati,count):
    new[x]=tree[x]
    if len(new[x])==y:
        count+=1
    if tree[x]==[]:
        if len(new[x])==y:
            count+=1
        new[x]=[]
    for v in tree[x]:
        trova_antenati(tree,v,new,y,antenati,count) #ricorsione
        new[v]=tree[v]
        antenati[v]=count
    return antenati