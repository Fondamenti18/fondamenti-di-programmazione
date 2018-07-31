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
- il nome di un file json contenente un dizionario-albero  d (fnome)
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

def chiusura(diz,fout):
    file=open(fout,'w')
    json.dump(diz,file)
    
def apertura(fnome):
    file=open(fnome)
    stringa=file.read()
    diz=json.loads(stringa)
    return diz
    
def apice(diz):
    for el in diz:
        if el not in diz.values():
            return el


def f(lista,diz,diz2):
    for el in lista:
        diz2[el]=diz[el]
        f(diz[el],diz,diz2)
        
    return diz2
        
def genera_sottoalbero(fnome,x,fout):
    diz2={}
    diz=apertura(fnome)    
    print(apice(diz))
    diz2=f(diz[x],diz,diz2)
    diz2[x]=diz[x]
    chiusura(diz2,fout)
   
    
def liv(lista,diz,diz2,cont):
    cont+=1
    if lista!=[]:
        l(lista,diz,diz2,cont)
        for el in lista:
            liv(diz[el],diz,diz2,cont)
    return diz2
    
def l(lista,diz,diz2,cont):
    if cont in diz2.keys():
            l=diz2[cont]
            l+=lista
            diz2[cont]=sorted(l)
    else:diz2[cont]=lista
    
    
    
    
def cancella_sottoalbero(fnome,x,fout):
    diz=apertura(fnome)
    diz3={}
    diz2={}
    diz2=f(diz[x],diz,diz2)
    diz2[x]=diz[x]
    diz3=cancella(diz,diz2,x)
    chiusura(diz3,fout)

def dizionario_livelli(fnome,fout):
    diz=apertura(fnome)
    a=apice(diz)
    cont=0
    diz2={}
    diz2=liv(diz[a],diz,diz2,cont)
    diz2[0]=[a]
    chiusura(diz2,fout)
        



def dizionario_gradi_antenati(fnome,y,fout):
    diz=apertura(fnome)
    diz2={}
    a=apice(diz)
    diz2[a]=0
    diz2=antenati(a,diz,diz2,y)
    chiusura(diz2,fout)
    

def cancella(diz,diz2,x):
    diz3={}
    for il in diz:
        if il not in diz2:
            l=[]
            for el in diz[il]:
                if x!=el:
                    l.append(el)   
            diz3[il]=l        
    return diz3
        
def antenati(k,diz,diz2,grad):
    for el in diz[k]:
        if len(diz[k])!=grad: diz2[el]=diz2[k]
        else: diz2[el]=diz2[k]+1
        antenati(el,diz,diz2,grad)
    return diz2
        