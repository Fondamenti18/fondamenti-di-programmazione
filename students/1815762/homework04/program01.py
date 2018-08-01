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


def sottoalbero(x,d,diz):
    diz[x]=d[x]
    for y in d[x]:
        diz=sottoalbero(y,d,diz)
    return diz

def canc_sottoalbero(x,z):
    for y in z[x]:
        z=canc_sottoalbero(y,z)
    z.pop(x)
    return z

def livello_func(z,dizio,c,x):
        if c not in dizio.keys() and z[x]!=[]:
            dizio[c]=[]
        for k in z[x]:
            dizio[c].append(k)
            livello_func(z,dizio,c+1,k)
        return dizio

def antenati(y,lst,z,diz,c,cont,a):
    for x in z.keys():
        if a in z[x]:
            if len(z[x])==y:
                cont+=1
                diz[lst[c]]=cont
            elif len(z[x])!=y:
                diz[lst[c]]=cont
            k=x
            antenati(y,lst,z,diz,c,cont,k)
        elif a ==lst[0]:
            cont=0
            c-=1
            if c==-len(lst):
                break
            else:
                a=lst[c]
                antenati(y,lst,z,diz,c,cont,a)
    return diz




def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome,'r')
    d=json.load(f)
    diz={}
    diz=sottoalbero(x,d,diz)
    g=open(fout,'w')
    g.write(json.dumps(diz))
    f.close()
    g.close()
    
    
    

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome,'r')
    z=json.load(f)
    for k in z.values():
        if x in k:
            k.remove(x)
    z=canc_sottoalbero(x,z)
    g=open(fout,'w')
    g.write(json.dumps(z))
    f.close()
    g.close()



    

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome,'r')
    z=json.load(f)
    lst=[]
    for r in z.keys():
        lst.append(r)
    dizio={}
    
    dizio[0]=[lst[0]]
    
    x=lst[0]
    
    c=1
    dizio=livello_func(z,dizio,c,x)
    for y in dizio.keys():
        dizio[y].sort()
    g=open(fout,'w')
    g.write(json.dumps(dizio))
    f.close()
    g.close()
 

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    f=open('Alb10.json','r')
    z=json.load(f)
    diz={}
    diz2={}
    lst=[]
    c=-1
    cont=0
    for k in z.keys():
        lst.append(k)
    a=lst[c]
    diz[lst[0]]=0
    antenati(y,lst,z,diz,c,cont,a)
    for k in range(len(lst)):
        diz2[lst[k]]=diz[lst[k]]
    g=open(fout,'w')
    g.write(json.dumps(diz2))
    f.close()
    g.close()
