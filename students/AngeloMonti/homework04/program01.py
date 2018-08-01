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


#with open('Alb100.json') as f: d1=json.load(f)
#with open('Alb10.json','w') as f: json.dump(d,f)

#-------------------------------------------------



#1
#prende albero d e suo nodo a,  restituisce albero  che e' una copia del  sottoalbero radicato in a

def genera_sottoalbero(fnome,x,fout):
    with open(fnome) as f: d=json.load(f)
    d1={}
    if x in d:
        sotto2(d,x,d1)
    with open(fout,'w') as f: json.dump(d1,f)

        
def sotto2(d,a,d1):
    for x in d[a]:
        sotto2(d,x,d1)
    d1[a]=d[a][:]  

#genera_sottoalbero('Alb10.json','d','risAlb10_1.json')
#---------------------------------
#2
#prende albero d e suo nodo a, cancella da d il sottoalbero radicato in a
# usa dato albero d e suo nodo a restituisce padre di a (lui stesso se e' il nodo radice)
 
def padre(d,x):
    for y in d:
        if x in d[y]: return y
    return x 

def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as f: d=json.load(f)
    if x in d:

        sotto1(d,x)
        y=padre(d,x)
        if x!=y:
            d[y].remove(x)
    with open(fout,'w') as f: json.dump(d,f)

def cancella_sottoalbero1(fnome,x,fout):
    with open(fnome) as f: d=json.load(f)
    if x in d:
        y=padre(d,x)
        if x!=y:
            d[y].remove(x)
        sotto1(d,x)
    with open(fout,'w') as f: json.dump(d,f)
        
def sotto1(d,a):
    for x in d[a]:
        sotto1(d,x)
    del d[a] 
    
#cancella_sottoalbero('Alb10.json','d','risAlb10_2.json')  
#-----------------------------------------
#3
#prende albero d e suo nodo e genera dizionario con parola chiave i livelli 
# dell'albero ed associati i nodi che appartengono  a quel livello   
#usa funzione che trova la   radice dell'albero


def dizionario_livelli(fnome,fout):
    with open(fnome) as f: d=json.load(f)
    d1={}
    p=radice(d)
    invoca(d1,d,p,0)
    for x in d1:
        d1[x]=sorted(d1[x])
    with open(fout,'w') as f: json.dump(d1,f)
 
def invoca(d1,d,x,i):
    if i in d1:d1[i]+=[x]
    else:d1[i]=[x]
    for y in d[x]:invoca(d1,d,y,i+1) 

#dizionario_livelli('Alb10.json','risAlb10_3.json')       
#-------------------------------------------------------------
#4
#genera dizionario d1 dove ad ogni nodo e' associato il numero di antenati di grado y  che si incontrano nel risalire alla la radice:
#usa  prende albero d e genera p:dizionario dei padri: ogni nodo ha a associato suo padre la radice se stessa 
#usa anche radice 

def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as f: d=json.load(f)
    d1={}
    rad=radice(d)
    calcola(0,rad,d1,d,y)
    with open(fout,'w') as f: json.dump(d1,f)   
        
def calcola(ant,r,d1,d,y):
    d1[r]=ant
    if len(d[r])==y: 
        for x in d[r]: calcola(ant+1,x,d1,d,y)
    elif len(d[r])>0: 
        for x in d[r]: calcola(ant,x,d1,d,y)



#-------------------------------------
def ordina(fnome,fout):
    with open(fnome) as f: d=json.load(f)
    for x in d:
        d[x]=sorted(d[x])
        
#--------------------------------------------

def radice(d):
    a=list(d.items())
    rad=a[0][0]
    for i in range(len(a)):
        if rad in a[i][1]:
            rad=a[i][0]
    return rad
    for x in d.values(): b.union(set(x))
    return  (a-b).pop()
    b=set(list(d.values()))
    return (a-b).pop()