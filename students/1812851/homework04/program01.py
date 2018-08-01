'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero  e l'attributo della chiave e' la lista 
(eventualmente vuota) degli identificativi dei  figli del nodo. Gli identificativi dei nodi 
all'interno delle liste sono in ordine lessicografico crescente.



Ecco un esempio di dizionario d che rappresenta un dizionario-albero

d={
'a':['b'] ,
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

- il nome di un file json contenente un dizionario-albero  d (fnome)
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
json.load(open('Alb10.json'))
'''



import json


def genera_sottoalbero(fnome,x,fout):
    ris={}
    diz=json.load(open(fnome))
    if x in diz:
        ris=pr(x,diz,ris)
    else:
        ris={}
    #print(ris)
    with open(fout, 'w') as f:
       json.dump(ris, f, ensure_ascii=False)
    return

def pr(x,diz,ris):
    ris[x]=diz[x]
    #print(x,ris[x])
    for i in diz[x]:
        pr(i,diz,ris)
    return ris
#chiavi=list(diz.keys())   



def cancella_sottoalbero(fnome,x,fout):
    diz=json.load(open(fnome))
    ris={}
    val=None
    pos=None
    if x in diz:
        chiavi=list(diz.keys())
        inizio=chiavi[0]
        #print(inizio,x,diz)
        ris=prel(inizio,x,diz,ris)
        #print(ris)
        val,pos=canc_residui(x,ris)
        if val!=None:
            del diz[val][pos]
    with open(fout, 'w') as f:
       json.dump(ris, f, ensure_ascii=False)
    return

def prel(inizio,canc,diz,ris):
    #x='Sì'
    if canc==inizio:
        #x='No'
        return
    for i in diz[inizio]:
        prel(i,canc,diz,ris)
    #print(inizio,diz[inizio],x)
    ris[inizio]=diz[inizio]
    return ris



def canc_residui(canc,rispdata):
    val=None
    pos=None
    for i in rispdata.keys():
        if canc in rispdata[i]:
            val=i
            pos=rispdata[i].index(canc)
    return val,pos
        
        
    

def dizionario_livelli(fnome,fout):
    diz=json.load(open(fnome))
    ris={}
    chiavi=list(diz.keys())
    x=chiavi[0]
    ris=prlvl(x,diz,-1,ris)
    ris=ordina(ris)
    with open(fout, 'w') as f:
       json.dump(ris, f, ensure_ascii=False)
    return
 
def prlvl(x,diz,c,ris):
    c+=1
    #print(x,diz[x],c)
    if c in ris:
        ris[c].append(x)
    
    else:
        ris[c]=[x]
    for i in diz[x]:
        prlvl(i,diz,c,ris)
    return ris

def ordina(ris):
    for i in ris:
        ris[i].sort()
    return ris



def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
