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

{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}
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
    j=open(fnome,'r',encoding='utf-8')
    dizionario=json.load(j)
    j.close()
    diz2={}
    for el in creainsieme(dizionario,x):
        diz2[el]=dizionario[el]
    f=open(fout,'w',encoding='utf-8')
    json.dump(diz2,f)
    f.close()


def creainsieme(dizionario,x):
    lista=[x]
    for el in dizionario[x]:
        lista+=creainsieme(dizionario,el)  
    return lista

def cancella_sottoalbero(fnome,x,fout):
    j=open(fnome,'r',encoding='utf-8')
    dizionario=json.load(j)
    j.close()
    diz2={}
    try:
        for el in dizionario:
            if el not in creainsieme(dizionario,x):
                if x not in dizionario[el]:
                    diz2[el]=dizionario[el]
                else:
                    lista=dizionario[el]
                    lista.remove(x)
                    diz2[el]=lista
        f=open(fout,'w',encoding='utf-8')
        json.dump(diz2,f)
        f.close()
    except KeyError:
        f=open(fout,'w',encoding='utf-8')
        json.dump(dizionario,f)
        f.close()
        

    

def dizionario_livelli(fnome,fout):
    j=open(fnome,'r',encoding='utf-8')
    dizionario=json.load(j)
    j.close()
    diz2={}
    diz2[0]=list(start(dizionario))
    ndiz=creadiz(dizionario, diz2, 1)
    f=open(fout,'w',encoding='utf-8')
    json.dump(ndiz,f)
    f.close()

def creadiz(dizionario, diz2, cont):
    lista=[]
    for el in diz2[cont-1]:
        lista+=dizionario[el]
    if lista==[]:
        return diz2
    else:
        diz2[cont]=sorted(lista)
        return creadiz(dizionario, diz2, cont+1)

def start(d):
    insieme=set()
    insieme3=set()
    for k in d:
        v=d[k]
        insieme3.add(k)
        for el in v:
            insieme.add(el)       
    return insieme3-insieme
    

 

def dizionario_gradi_antenati(fnome,y,fout):
    j=open(fnome,'r',encoding='utf-8')
    dizionario=json.load(j)
    j.close()
    diz2={}
    for r in dizionario:
        diz2[r]=0
    for el in dizionario_lunghezza(dizionario,y):
        z=discendenti(dizionario,el, [])
        z.remove(el)
        for i in z:
            diz2[i]+=1
    f=open(fout,'w',encoding='utf-8')
    json.dump(diz2,f)
    f.close()

def dizionario_lunghezza(dizionario,y):
    diz3={}
    for el in dizionario:
        if len(dizionario[el])==y:
            diz3[el]=dizionario[el]
    return diz3

def creadiz_finale(dizionario,y):
    diz2={}
    for r in dizionario:
        diz2[r]=0
    for el in dizionario_lunghezza(dizionario,y):
        z=discendenti(dizionario,el, [])
        z.remove(el)
        for i in z:
            diz2[i]+=1
    return diz2

def discendenti(dizionario, elemento,lista):
    lista.append(elemento)
    for i in dizionario[elemento]:
        discendenti(dizionario, i, lista)
    return lista
        
