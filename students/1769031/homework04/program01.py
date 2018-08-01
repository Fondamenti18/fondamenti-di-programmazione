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
import os

    
def albero_contrario(fnome,x,fout):
    with open(fnome,'r') as f:
        d=json.load(f)
    if os.path.exists(fout)==False:
        d1={}
    else:
        with open(fout,'r') as f:
            d1=json.load(f)
    for i in d:
        if x in d[i]:
            d1.update({i:0})
            with open(fout,'w') as f:
                json.dump(d1,f)
            albero_contrario(fnome,i,fout)
    if d1=={}:
        with open(fout,'w') as f:
            json.dump({},f)
            
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as f:
        d0=json.load(f)
    if os.path.exists(fout)==True:
        with open(fout,'r') as f:
            d1=json.load(f)
    if os.path.exists(fout)==False:
        d1={}
    lista=list(d1.items())
    if d0[x]==[]:
        lista.insert(0,(x,d0[x]))
        d2=dict(lista)
        with open(fout,'w') as f:
            json.dump(d2,f)
    else:
        if x not in lista:
            lista.insert(0,(x,d0[x]))
            d2=dict(lista)
            with open(fout,'w') as f:
                     json.dump(d2,f)
        for i in reversed(d0[x]):
            with open(fout,'r') as f:
                 d1=json.load(f)
                 lista=list(d1.items())
            lista.insert(0,(i,d0[i]))
            d2=dict(lista)
            with open(fout,'w') as f:
                json.dump(d2,f)
            genera_sottoalbero(fnome,i,fout)
    return fout
    

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open('outfile.json','w') as f:
        json.dump({},f)
    genera_sottoalbero(fnome,x,'outfile.json')
    with open('outfile.json','r') as f:
        d=json.load(f)
    with open(fnome,'r') as f:
        d1=json.load(f)
    lista=[]
    for i in d1:
        lista2=[]
        if i not in d:
            for k in d1[i]:
                if k not in d:lista2.append(k)
            lista.append((i,lista2))
    d2=dict(lista)
    with open(fout,'w') as f:
        json.dump(d2,f)

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as f:
        d0=json.load(f)
    if os.path.exists(fout)==False:
        d1={}
        lista=[list(d0.keys())[0]]
        d1.update({0:sorted(lista)})
        with open(fout,'w') as f:
            json.dump(d1,f)
    elif os.path.exists(fout)==True:
        with open(fout,'r') as f:
            d1=json.load(f)
            lista=[]
            cont=list(d1.keys())[-1]
            for i in d1[cont]:
                for j in d0[i]:
                    lista.append(j)
            cont=int(cont)
            d1.update({str(cont+1):sorted(lista)})
            with open(fout,'w') as f:
                json.dump(d1,f)
    for i in d1[list(d1.keys())[-1]]:
        if d0[i]!=[]:
            dizionario_livelli(fnome,fout)
            break
                    
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    d2={}
    with open(fnome,'r') as f:
        d=json.load(f)
    for i in d:
        cont2=0
        if os.path.exists('albero-cont.json')==True:
            with open('albero-cont.json','w') as f:
                json.dump({},f)
        albero_contrario(fnome,i,'albero-cont.json')
        with open('albero-cont.json','r') as f:
            try:d1=json.load(f)
            except:d1={}
        for j in d1:
            cont=0
            for k in d[j]:
                cont+=1
                if cont>y:break
            if cont==y:cont2+=1
        d2.update({i:cont2})
    with open(fout,'w') as f:
        json.dump(d2,f)