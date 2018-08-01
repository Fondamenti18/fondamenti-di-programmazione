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


import itertools

from collections import defaultdict
import json
class Fnode(object):
    def __init__(self,obj,dizionario):
        self.obj=obj
        self.dizionario=dizionario
        self.contenuto=self.dizionario[self.obj]
    def __str__(self):
        return 'Fnode("' + self.obj +self.dizionario+'")'
    
def trova_radice(diz):
    flat_list = [item for sublist in diz.values() for item in sublist]
    for k in diz:
        if k not in flat_list:
            return k
    
    
    
    
        
        
        
        
        
        
        
    
    
    



        
                
        



def albero(chiave,dizionario,nuovo):
    nodo=Fnode(chiave,dizionario)
    if chiave not in dizionario.keys():
        return {}
    if nodo.contenuto==[] : 
        nuovo[chiave]=nodo.contenuto
        
    if nodo.contenuto!=[] :
        nuovo[chiave]=nodo.contenuto
        for el in nodo.contenuto:
            albero(el,dizionario,nuovo)
    return nuovo


def livelli(chiave,dizionario,new,livello=0):
    
    nodo=Fnode(chiave,dizionario)
   
    new[livello].append(chiave)
    new[livello]=sorted(new[livello])    
    if nodo.contenuto!=[]:
        for el in nodo.contenuto:                               
            livelli(el,dizionario,new, livello+1)         
    return new

def antenati(ch,d,l):
    try:
        nodo=Fnode(ch,d)
        if nodo.contenuto!=[]:
            l.append(nodo.contenuto)
            antenati(nodo.contenuto,d,l)
        return l
    except:
        KeyError                

def liv(chiave,dizionario,y,lista,new,sup,livello=0):
           
    
    nodo=Fnode(chiave,dizionario)
    h=antenati(chiave,new,[]) 
    contatore=0
    try:
        for el in h:
            if el in lista:
                contatore+=1
       # print(h,chiave,contatore)
        
    except:
        TypeError
    sup[chiave]=contatore    
    if len(nodo.contenuto)==y:
        lista.append(chiave)        
    for el in nodo.contenuto:
        new[el]=chiave
        liv(el,dizionario,y,lista,new,sup,livello+1)
    return sup




def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open (fnome) as f:
        diz=json.load(f)
        sottoal=albero(x,diz,{})
    with open (fout,"w") as o:   
        json.dump(sottoal,o)
        
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open (fnome) as f:
        diz=json.load(f)
        sottoal=albero(x,diz,{})
        result={}
        for k in diz:
            if k not in sottoal:
                result[k]=diz[k]
        for _ in result.values():
            for el in _:
                if el ==x:
                    _.remove(el)
             
    with open (fout,"w") as o:   
        json.dump(result,o)
        
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open (fnome)as f:
        diz=json.load(f)
        #giacomo=list(diz.keys())
        giacomo=trova_radice(diz)
        h=defaultdict(list)
        result=livelli(giacomo,diz,h,0)
    with open(fout,"w")as o:
        json.dump(result,o)



def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    with open (fnome) as f:
        diz=json.load(f)
       # giacomo=list(diz.keys())
        giacomo=trova_radice(diz) 
        j=liv(giacomo,diz,y,[],{},{})
    with open (fout,"w") as o:
        json.dump(j,o)


                
            
         
    
    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    
    
    
    
    
    
    
    