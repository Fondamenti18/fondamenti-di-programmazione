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
'''
class ANodo:
    def __init__(self,x,l=[]):
        self.valore=x
        self.lf=l # lista dei nodi figli

def gen_tree(radice,d):
    nodo=ANodo(radice,d[radice])
    if d[radice]==[]:
        return nodo
    for el in d[radice]:
        nodo.lf=
'''
        
def trova_radice(d):
    for el in d:
        if d[el]!=[]:
           radice=cerca(d,el)
           return radice   

def cerca (d,x):
    for el in d:
        if x in d[el]:
            return cerca(d,el)
    return x    
        
               
            
    

def genera_sottoalbero(fnome,x,fout):
    with open (fnome, 'r', encoding='utf8') as f:
        d=json.load(f)
    diz={}
    if not x in d:
        with open(fout,'w', encoding='utf8') as f:
            json.dump(diz,f) 
    else:        
        diz=gendiz_1(d,x,diz)
        with open(fout,'w', encoding='utf8') as f:
            json.dump(diz,f)  
            
def gendiz_1(d,x,diz):
    if d[x]==[]:
        diz[x]=d[x]
        return diz
    for el in d[x]:
       gendiz_1(d,el,diz)
    diz[x]=d[x] 
    return diz
    

def cancella_sottoalbero(fnome,x,fout):
    with open (fnome, 'r', encoding='utf8') as f:
        d=json.load(f)
    diz={}
    if not x in d:
        with open(fout,'w', encoding='utf8') as f:
            json.dump(d,f) 
    else:
        diz=d.copy()
        diz=gendiz_2(d,x,diz)
        for el in diz:
            if x in diz[el]:
                diz[el]=diz[el][:diz[el].index(x)]+diz[el][diz[el].index(x)+1:]    
        with open(fout,'w', encoding='utf8') as f:
            json.dump(diz,f)  
            
def gendiz_2(d,x,diz):
    if d[x]==[]:
        del diz[x]
        return diz
    for el in d[x]:
        gendiz_2(d,el,diz)
    del diz[x]            
    return diz
    

def dizionario_livelli(fnome,fout):
    with open (fnome, 'r', encoding='utf8') as f:
        d=json.load(f) 
    if d=={}:
        with open(fout,'w', encoding='utf8') as f:
            json.dump(d,f) 
    else:
        radice=(trova_radice(d))
        diz={}
        diz[0]=[radice]
        c=1
        for el in d[radice]:
            diz=gendiz_3(d,el,diz,c)
        with open(fout,'w', encoding='utf8') as f:
            json.dump(diz,f) 
            
 
def gendiz_3(d,x,diz,c):
    if not c in diz:
        diz[c]=[x]
    else:
        diz[c]=sorted(diz[c]+[x])
    if d[x]==[]:
        return diz
    c=c+1
    for el in d[x]:
       gendiz_3(d,el,diz,c)
     
    return diz
    
    

def dizionario_gradi_antenati(fnome,y,fout):
    with open (fnome, 'r', encoding='utf8') as f:
        d=json.load(f)
    diz={}
    if d=={}:
        with open(fout,'w', encoding='utf8') as f:
            json.dump(d,f) 
    else:
        radice=(trova_radice(d))  
        diz={}
        diz[radice]=0
        c=0
        if len(d[radice])==y:
            c=c+1
        for el in d[radice]:
            diz=gendiz_4(d,el,diz,c,y)   
        with open(fout,'w', encoding='utf8') as f:
            json.dump(diz,f) 
            
def gendiz_4(d,x,diz,c,y):
    diz[x]=c
    if len(d[x])==y:
        c=c+1
    if diz[x]==[]:
        return diz
    for el in d[x]:
        gendiz_4(d,el,diz,c,y)
        
    return diz    
        

'''dizionario_gradi_antenati('Alb10.json',2,'tAlb10_4.json')'''