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

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        D = json.load(f)
    D2 = dict()
    D2 = genera(D, D2, x)

    with open(fout,'w') as f:
        json.dump(D2,f)       

def genera(D, D2, x):
    if x in D:
        D2[x] = D[x]
        for y in D2[x]:
            D2 = genera(D, D2, y)
    return D2
             
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        D = json.load(f)
    D = cancella(D, x)
    for y in D:
        if x in D[y]:
            i = D[y].index(x)
            D[y].pop(i)
            break

    with open(fout,'w') as f:
        json.dump(D,f)
        
def cancella(D, x):
    if x in D:
        L = D.pop(x)
        for y in L:
            D = cancella(D, y)
    return D


def dizionario_livelli(fnome,fout):
    with open(fnome) as f:
        D = json.load(f)
      
    D2 = dict()
    liv = 0
    while len(D)>0:
        K = set(D.keys())
        H = list()
        for L in D.values():
            for x in L:
                H.append(x)
        M = K - set(H)
    
    
        D, D2 = aggiorna(D, D2, liv, M)
        liv = liv + 1
    
    with open(fout,'w') as f:
        json.dump(D2,f)
    

def aggiorna(A, B, n, C):
    """ aggiunge al diz B key n tutti gli elementi del set C trasformati in lista ordinata. Elimina key tutte le key contenute
    in C dal diz A"""
    B[n] = []
    for x in C:
        B[n].append(x)
     
        A.pop(x)
    B[n].sort()
    return A, B
       
def dizionario_gradi_antenati(fnome,y, fout):
    '''inserire qui il vostro codice'''

    with open(fnome) as f:
        D1 = json.load(f)
    
    D2 = figlioDi(D1)
    D3 = dict()
    for x in D1:
        D3[x] = 0
        L = antenati(D2, x)
        for j in L:
            if len(D1[j])==y:
                D3[x] = D3[x] + 1
    
    with open(fout,'w') as f:
        json.dump(D3,f)    

                      
def figlioDi(D):
    """ Partendo dal dizionario albero D, restituisce un dizionario con key un nodo e item il suo genitore"""
    D2 = dict()
    for x in D:
        for y in D[x]:
            D2[y] = x
    return D2
    
def antenati(D, n):
    """ Nel dizionario D la key e' il nodo e l'item il suo genitore. Il dizionari D si ottiene applicando la funzione figlioDi al dizionario-albero.
    ATTENZIONE: antenati non richiama la funzione figlioDi, il dizionario D e' GIA' nel formato nodo:genitore.
    La funzione restituisce la lista degli antenati di n """
    L = list()    
    while n in D:
        L.append(D[n])
        n = D[n]
    return L


    
