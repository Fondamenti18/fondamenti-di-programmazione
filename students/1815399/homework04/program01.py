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
    d= json.load(open(fnome))
    diz={}
    diz= genera(d,x,diz)
    with open(fout,'w') as f:
        json.dump(diz,f)

    

def cancella_sottoalbero(fnome,x,fout):
    d= json.load(open(fnome))
    diz= cancella(d,x)
    for k in diz.keys():

        i=0
        while i < len(d[k]):

            if d[k][i] == x:
                d[k].pop(i)

            i+=1    
    with open(fout,'w') as f:
        json.dump(diz,f)


def dizionario_livelli(fnome,fout):
    d= json.load(open(fnome))

    diz={}
    radice= rad(d)
    lv= livelli(d,radice,diz)
    for x in lv.keys():
        lv[x]=sorted(lv[x])
    with open(fout,'w') as f:
        json.dump(lv,f)    
  


def dizionario_gradi_antenati(fnome,y,fout):
    d= json.load(open(fnome))

    diz={}
    cont=0
    radice= rad(d)
    diz=antenati(d,radice,cont,diz,y)
    with open(fout,'w') as f:
        json.dump(diz,f)
    
def genera(d,x,albdiz):
    
    albdiz[x] = d[x]
    k=0
    while k < len(d[x]):
        d[k] = genera(d,d[x][k],albdiz)
        k+=1
    return albdiz    

def cancella(d,x):
    k=0
    while k < len(d[x]):
        cancella(d,d[x][k])
        k+=1
    d.pop(x)    
    return d

def livelli(d,x,diz,livello=0):
    if str(livello) not in diz:
        diz[str(livello)]= []

    diz[str(livello)].append(x)

    i=0
    while i < len(d[x]):
      
             livelli(d,d[x][i],diz,livello+1)
             i+=1
    return diz          
            
def antenati(d,x,cont,diz,y):
    diz[x] = cont
    '''print(diz[x])'''
    for figlio in d[x]:
        if len(d[x]) == y:
            antenati(d,figlio,cont+1,diz,y)
        else:
            antenati(d,figlio,cont,diz,y) 
    return diz   
        
def rad(d):
    ins= set()
    for x in d.values():
        for y in x:
            ins.add(y)
    radice=0
    for z in d.keys():
        if z not in ins:
            radice= z
    return radice  



