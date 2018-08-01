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

def gen(a,s,d):
    if a==[]:return s
    else: 
        s[a[0]]=d[a[0]]
        for k in d[a[0]]:
            s[k]=d[k]
            gen(s[k],s,d)
    gen(a[1:],s,d)
        
def genera_sottoalbero(fnome,x,fout):
    with open(fnome) as f: d=json.load(f)
    s={}
    s[x]=d[x]
    gen(d[x],s,d)
    with open(fout,'w') as o:o.write(json.dumps(s))
    o.close()
    
    


def can(a,r,d):
    if a==[]:return d
    else: 
        for k in d[a[0]]:
            r.append(k)
            for m in d[k]:
                r.append(m)
                can(d[k],r,d)
    can(a[1:],r,d)
    
def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as f: d=json.load(f)
    r=[]
    r.append(x)
    for w in d[x]:
        r.append(w)
    can(d[x],r,d)
    for j in set(r):
        del d[j]
        for y in d:
            if j in d[y]:
                d[y].remove(j)
    with open(fout,'w') as o:o.write(json.dumps(d))
    o.close()
    

def liv(x,c,d,s):
        try:
            for k in d:
                if x in d[k]:
                    c+=1
                    liv(k,c,d,s)
            try:
                s[str(c)].append(list(d.keys())[-1])
                d.pop(list(d.keys())[-1],None)
            except KeyError:
                s[str(c)]=[list(d.keys())[-1]]
                d.pop(list(d.keys())[-1],None)
        except RuntimeError:
            pass
        
def dizionario_livelli(fnome,fout):
    with open(fnome) as f:d=json.load(f)
    s={}
    c=0
    while d!={}:
        liv(list(d.keys())[-1],c,d,s)
    for n in s:
        s[n].sort()
    with open(fout,'w') as o:o.write(json.dumps(s))
    o.close()
                
 

def ant(x,c,d,s):
        try:
            for k in d:
                if x in d[k]:
                    if len(d[k])==2:
                        c+=1
                    ant(k,c,d,s)
            s[list(d.keys())[-1]]=c
            d.pop(list(d.keys())[-1],None)
        except RuntimeError:
            pass
        
def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as f:d=json.load(f)
    s={}
    c=0
    while d!={}:
        ant(list(d.keys())[-1],c,d,s)
    with open(fout,'w') as o:o.write(json.dumps(s))
    o.close()