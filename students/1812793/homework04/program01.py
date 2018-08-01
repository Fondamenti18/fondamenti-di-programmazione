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




from json import *

#            PRIMA FUNZIONE
def genera_sottoalbero(fnome,x,fout):
    f=open(fnome,"r")
    d=load(f)
    f.close()
    df=dict()
    df,x=genera(x,d,df)
    f=open(fout,"w")
    dump(df,f)
    f.close()
    
def genera(x,d,df):
    if x in d:
        df[x]=d[x]
        for i in d[x]:
            df,x=genera(i,d,df)
    return df,x

#            SECONDA FUNZIONE
def cancella_sottoalbero(fnome,x,fout):
    f=open(fnome,"r")
    d=load(f)
    f.close()
    a=x
    df=dict()
    df,x=genera(x,d,df)
    d1=dict(d)
    for i in d1: 
        if a in d[i]:
            d[i].remove(a)
        if i in df:
            del d[i]
    f=open(fout,"w")
    dump(d,f)
    f.close()
    
#            TERZA FUNZIONE
def dizionario_livelli(fnome,fout):
    f=open(fnome,"r")
    d=load(f)
    f.close()
    cont=0
    df=dict()
    root=trova_root(d)
    df=calcola(root,d,df,cont)
    for i in df:
        df[i].sort()
    f=open(fout,"w")
    dump(df,f)
    f.close()
    
def calcola(x,d,df,cont):
    if cont in df:
        df[cont]+=[x]
    else:
        df[cont]=[x]
    cont+=1
    for i in d[x]:
        df=calcola(i,d,df,cont)
    return df
       
def trova_root(d):
    s=set()
    for i in d:
        for x in d[i]:
            s.add(x)
    for i in d:
        if i not in s:
            return i
 
#            QUARTA FUNZIONE
def dizionario_gradi_antenati(fnome,y,fout):
    f=open(fnome,"r")
    d=load(f)
    f.close()
    df=dict()
    root=trova_root(d)
    cont=0
    df=trova(root,d,df,cont,y)
    
    f=open(fout,"w")
    dump(df,f)
    f.close()

def trova(nodo,d,df,cont,y):
    df[nodo]=cont
    if len(d[nodo])==y:
        cont+=1
    for i in d[nodo]:
        trova(i,d,df,cont,y)
    return df
