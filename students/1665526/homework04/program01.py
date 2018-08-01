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
'''

        
        
        
'''
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
dic={}
def lista(l,fnome):
    with open(fnome,'r') as j:
        a=json.load(j)
        if l==[]:
            return 
        dic.update({l[0]:a[l[0]]})
        lista(l[1:],fnome)
        return dic
    
def genera_sottoalbero2(fnome,x,fout):
    '''inserire la dunzioe qui'''
    with open(fnome,'r') as j:
        a=json.load(j)
        l=[]
        l+=a[x]
        for i in l:
            l+=a[i]
        return(l)

def genera_sottoalbero(fnome,x,fout):
    '''inserire la dunzioe qui'''
    d={}
    l=genera_sottoalbero2(fnome,x,'1')
    p=lista(l,fnome)
    global dic
    with open(fnome,'r') as j:
        a=json.load(j)
        d.update({x:a[x]})
        d.update(p)
        dic={}
        #return (d)
    with open(fout,'w')as qls:
        json.dump(d,qls)

def cancella_sottoalbero1(fnome,x,fout):
    '''inserire la dunzioe qui'''
    with open(fnome,'r') as j:
        a=json.load(j)
        l=[]
        l+=a[x]
        for i in l:
            l+=a[i]
        c=list(a)
        for i in l:
            if i in c:
                c.remove(i)
        c.remove(x)
        return(c)
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    d={}
    l=cancella_sottoalbero1(fnome,x,'1')
    p=lista(l,fnome)
    global dic
    d.update(p)
    for g in d:
        for i in d[g]:
            if x in d[g]:
                d[g].remove(x)
                break
        dic={}
        #return (d)
    with open(fout,'w')as qls:
        json.dump(d,qls)
def cdv(fname):
    with open(fnome,'r') as j:
        a=json.load(j)
        b=list(a)
        return len(b)
z=0
def listaa(fnome,i):
    global z
    with open(fnome,'r') as j:
        a=json.load(j)
        for b,c in a.items():
            if i in c:
                z+=1
                listaa(fnome,b)
    return z
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    global dic,z
    l=[]
    m={}
    with open(fnome,'r') as j:
        a=json.load(j)
        for i in a:
            doppa=listaa(fnome,i)
            l.append([doppa,i])
            z=0
        for x,y in l:
            m.setdefault(x,[]).append(y)
        for i in m:
            m[i].sort()
    with open(fout,'w') as w:
        json.dump(m,w)
cc=0
def listaa1(fnome,i,y):
    global cc
    with open(fnome,'r') as j:
        a=json.load(j)
        for b,c in a.items():
            if i in c:
                if len(c)==y:
                    cc+=1
                listaa1(fnome,b,y)
    return cc
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    global cc
    aa={}
    with open(fnome,'r') as j:
        a=json.load(j)
        b=list(a)
        for i in a:
            aa.update({i:listaa1(fnome,i,y)})
            cc=0
    with open(fout,'w') as wo:
        json.dump(aa,wo)