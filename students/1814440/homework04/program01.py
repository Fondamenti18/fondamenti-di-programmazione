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

def genera(ris,mio,x):
    try:
        ris[x]=mio[x]
    except: return {}
    for el in ris[x]:
        ris=genera(ris,mio,el)
    return ris
    
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    mio=json.load(open(fnome))
    ris={}
    ris=genera(ris,mio,x)
    f=open(fout,'w')
    json.dump(ris,f)
    f.close()

def cancella(mio,x):
    for el in mio[x]:
        mio=cancella(mio,el)
    del(mio[x])
    return mio

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    mio=json.load(open(fnome))
    try:
        a=mio[x]
    except:
        with open(fout,'w') as f:
            json.dump(mio,f)
        return
    mio=cancella(mio,x)
    for el in mio.keys():
        if x in mio[el]:
            a=mio[el]
            mio[el]=[k for k in a if k!=x]
            with open(fout,'w') as f:
                json.dump(mio,f)
                return
    
def livelli(ret,chiave,mio,livello):
    try:
        ret[livello].append(chiave)
        ret[livello].sort()
    except:
        ret[livello]=[chiave]
    for figlio in mio[chiave]:
        ret=livelli(ret,figlio,mio,livello+1)
    return ret

def radice(diz):
    l=[]
    chiavi=set(list(diz.keys()))
    v=diz.values()
    for el in v: l+=el
    l=set(l)
    return chiavi-l

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    mio=json.load(open(fnome))
    ret={}
    rad=radice(mio)
    ret=livelli(ret,list(rad)[0],mio,0)
    with open(fout,'w') as f:
        json.dump(ret,f)
        

def antenati(ris,radice,mio,y):
    try:
        a=ris[radice]
    except:
        ris[radice]=0 # inizializzo i valori vuoti
    for el in mio[radice]:
        if len(mio[radice])==y:
            ris[el]=ris[radice]+1
            ris=antenati(ris,el,mio,y)
        else:
            ris[el]=ris[radice]
            ris=antenati(ris,el,mio,y)
    return ris
       
 
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    mio=json.load(open(fnome))
    listachiavi=mio.keys()
    ris={}
    rad=list(radice(mio))[0]
    ris=antenati(ris,rad,mio,y)
    with open(fout,'w') as f:
        json.dump(ris,f)
        