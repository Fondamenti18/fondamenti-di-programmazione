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
    with open(fnome) as f: 
        dizio=json.load(f)
    l=[x]
    di_fi={}
    ok2(dizio,x,l)
    for i in l:
        if i in dizio:
            di_fi[i]=dizio[i]
    with open(fout,"w") as fp: 
        json.dump(di_fi,fp)
def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as f: 
        dizio=json.load(f)
    l=[x]
    di={}
    ok2(dizio,x,l)
    for i in dizio:
        if i not in l:
            di[i]=dizio[i]
    for w in di:
        if x in di[w]:
            d=di[w].index(x)
            del di[w][d]
    with open(fout,"w") as fp: 
        json.dump(di,fp)
def ok2(dizio,d,l):
    m=[]
    if d in dizio:
        l+=dizio[d]
        m+=dizio[d]
    for x in m:
        ok2(dizio,x,l)    
def dizionario_livelli(fnome,fout):
    with open(fnome) as f: 
        dizio=json.load(f)
    diziof={}
    x={a for b in dizio.values() for a in b}
    for i in dizio:
        if i not in x:
            radice=[i]
    l=[]
    listaliv(l,radice,dizio)
    n=0
    diziofi(n,l,diziof)
    with open(fout,"w") as fp: 
        json.dump(diziof,fp)

def listaliv(l,radice,dizio):
    lista=[]
    if radice!=[]:
        l+=[radice]
        for i in radice:
            for a in dizio.get(i,()):
                lista+=[a]
        radice=lista
        listaliv(l,radice,dizio)
def diziofi(n,l,diziof):
    if n<len(l):
        diziof[n]=sorted(l[n])
        n+=1
        diziofi(n,l,diziof)
def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as f: 
        dizio=json.load(f)
    di={}
    df={}
    x={a for b in dizio.values() for a in b}
    for q in dizio:
        if q not in x:
            r=q
    df[r]=0
    for x,y1 in dizio.items():
        for p in y1:
            di[p]=x
    for w in di:
        c=0
        l=[]
        trova_ant(di,w,l)
        for o in l:
            if len(dizio[o])==y:
                c+=1                
            df[w]=c
    with open(fout,"w") as fp: 
        json.dump(df,fp)        
def trova_ant(d,w,l):
    if w in d:
        l+=[d[w]]
        trova_ant(d,d[w],l)
    else:
        return l