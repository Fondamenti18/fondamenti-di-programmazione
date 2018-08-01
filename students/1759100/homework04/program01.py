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



import sys
sys.setrecursionlimit(5000)
import json

def genera_sottoalbero(fnome,x,fout):
    '''produce   il  dizionario-albero che rappresenta   il sottoalbero  radicato 
nell'identificativo x che si ottiene dal dizionario-albero d. '''
    with open(fnome) as f: #apre e carica il file json1
        dizionario=json.load(f)
        risultato={}
        ris=ricerca(x,dizionario,risultato) 
    with open(fout,'w') as d:
        json.dump(ris,d)
    
def ricerca(x,dizionario,ris):
    '''ricerca le chiavi da utilizzare per formare il sottoalbero. è connessa a genera_sottoalbero.'''
    for j,k in dizionario.items():
        if j==x :
            ris[j]=k
            for y in k:
                ricerca(y,dizionario,ris)
        else: pass
    return ris


def cancella_sottoalbero(fnome,x,fout):
    '''ricava  da d il sottoalbero radicato in x e lo salva nel file fout.
Se x non e' presente tra le chiavi di  d allora  il dizionario-albero d non viene modificato'''
    with open(fnome) as f:
        dizionario=json.load(f)
        risu={}
        ris=ricerca(x,dizionario,risu) #cerca il sottoalbero da eliminare
        risultato=cancella(x,dizionario,ris)
    with open(fout,'w') as d:
        json.dump(risultato,d)

def cancella(x,dizionario,ris):
    '''cancella tutti i sottoalberi presenti in dizionario che sono presenti anche in ris, fatto ciò cancella x come valore .'''
    for y in ris.keys():
        del dizionario[y]
    for y in dizionario.keys():
        if x in dizionario[y]:
            del dizionario[y][dizionario[y].index(x)]
    return dizionario




def dizionario_livelli(fnome,fout):
    '''costruisce il  dizionario che ha come  chiavi i livelli del dizionario-albero d. L'attributo di una 
chiave di valore x e' la lista degli identificativi  dei nodi che si trovano a livello x '''
    with open(fnome) as f:
        dizionario=json.load(f)
        risultato={}
        l=[]
        li=[]
        for j,k in dizionario.items():
            l.append(j)
            l.append(k)
        livello=0
        risultato[str(livello)]=[l[0]]
        risultato[str(livello+1)]=l[1] 
        li+=l[1]
        h=[]
        x=0
        while x<len(l):
            if l[x]==[]:
                del l[x]
                del l[x-1]
                x-=1
            else:x+=1
        ris=cerca_livello(l[2:],risultato,livello+1,li)
    with open(fout,'w') as d:
        json.dump(ris,d)
def cerca_livello(lista,risultato,livello,l): 
    if len(lista)<1:
        return risultato
    if len(l)==1:
        x=0
        while x<len(lista):
            if lista[x]==l[0]:
                risultato[livello+1]=lista[x+1]
                l=[]
                l+=lista[x+1]
                del lista[x]
                del lista[x]
                break    
            else:
                x+=1
    else:
        k=[]
        for el in l:
            x=0
            while x<len(lista):
                if lista[x]==el:
                    risultato[livello+1]=[]
                    k+=lista[x+1]
                    del lista[x]
                    del lista[x]
                    break    
                else:
                    x+=1
        if len(k)>=1:
        	risultato[livello+1]+=sorted(k)
        l=[]
        l+=k
    return cerca_livello(lista,risultato,livello+1,l)
    return risultato


def dizionario_gradi_antenati(fnome,y,fout):
    '''costuisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero 
    rappresentato dal dizionario-albero d, Attributo di una chiave di valore x e' il numero 
    di antenati di grado y che ha il nodo con identificativo x nell'albero.'''
   # f=dizionario_livelli(fnome,fout)
    dic={}
    with open(fnome) as file:
        f=json.load(file)
        #print(f)
        lista=list(f.keys())
        cerca_chiavi(lista,dic)
        #print(dic)
        lista=[]
        for j,k in f.items():
            lista.append(j)
            lista.append(k)
        lista=(lista[::-1])
        cerca_antenati(lista,dic,y)
       # print(dic)
def cerca_antenati(lista,dic,y):
    if lista[0]==[]:
        cerca_antenati(lista[1:],dic,y)
    else:
        if dic[lista[0]]!='':
            cerca_antenati(lista[1:],dic,y)
        cer(lista,dic,y)
        if len(lista)>1:
            print(lista)
            x=0
            x+=1
            cerca_antenati(lista[1:],dic,y)
        print(dic,x)
        
    return dic
def cer(lista,dic,y):
    if len(lista)==1:
        return dic
    print(lista)
    if len(list(lista[0]))==1:
        c=lista[0]
       # print(c,lista)
        x=0
        while x<len(lista):
            if type(lista[x])==list:
                if c in lista[x] and len(lista[x])>=y:

                 #   print(lista[x],len(lista[x]),y)
                    dic[c]+='1'
                    #del lista[0]
                    #print(lista)
                    cer(lista[x+1:],dic,y)
                    x+=1
                else:x+=1
            else:x+=1
    return dic

    
def cerca_chiavi(lst,dic):
    for x in lst:
        dic[x]=''
    return dic