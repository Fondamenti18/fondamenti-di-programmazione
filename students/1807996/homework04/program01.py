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

def fclose(alb,fout):
    json.dump(alb,open(fout,'w'))

def compf(alb_appoggio,alb,alb_out):
    for key in alb_appoggio:
        alb_out[key]=alb[key]
        compf(alb[key],alb,alb_out)
    return alb_out
        
def genera_sottoalbero(fnome,x,fout):
    alb_out={}
    alb=json.loads(open(fnome).read())    
    alb_out=compf(alb[x],alb,alb_out)
    alb_out[x]=alb[x]
    fclose(alb_out,fout)
       
def agg_alb_out(alb_appoggio,h,alb_out):
    if alb_appoggio!=[] and (h in alb_out.keys()):
        newlist=alb_out[h]
        newlist+=alb_appoggio
        alb_out[h]=sorted(newlist)
    elif alb_appoggio!=[]: 
        alb_out[h]=alb_appoggio
    return alb_out
    
def height(alb_appoggio,alb,alb_out,h):
    h+=1
    alb_out=agg_alb_out(alb_appoggio,h,alb_out)
    for key in alb_appoggio:
        height(alb[key],alb,alb_out,h)
    return alb_out

def crea_list_nodi(alb,key,x):
    list_nodi=[]
    for nodo in alb[key]:
        if x!=nodo:
            list_nodi.append(nodo) 
    return list_nodi
        
def top(alb):
    for key in alb: 
        if key not in alb.values():
            return key

def canc_alb(alb,alb_out,new_alb_out,x):
    for key in alb:
        if key not in alb_out:
            new_alb_out[key]=crea_list_nodi(alb,key,x)
    return new_alb_out

def cancella_sottoalbero(fnome,x,fout):
    alb=json.loads(open(fnome).read())
    new_alb_out={}
    alb_out={}
    alb_out=compf(alb[x],alb,alb_out)
    alb_out[x]=alb[x]
    fclose(canc_alb(alb,alb_out,new_alb_out,x),fout)

def dizionario_livelli(fnome,fout):
    alb=json.loads(open(fnome).read())
    alb_out={}
    alb_out=height(alb[top(alb)],alb,alb_out,h=0)
    alb_out[0]=[top(alb)]
    fclose(alb_out,fout)

def dizionario_gradi_antenati(fnome,y,fout):
    alb=json.loads(open(fnome).read())
    alb_out={}
    alb_out[top(alb)]=0
    alb_out=genitori(top(alb),alb,alb_out,y)
    fclose(alb_out,fout)
    
def new_alb_out(alb, start, y, alb_out,key):
    if len(alb[start])!=y: 
        alb_out[key]=alb_out[start]
    else: 
        alb_out[key]=alb_out[start]+1
    return alb_out

def genitori(start,alb,alb_out,y):
    for key in alb[start]:
        alb_out=new_alb_out(alb, start, y, alb_out,key)
        genitori(key,alb,alb_out,y)
    return alb_out
