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

def genera_sottoalbero(fnome,x,fout):
    with open(fnome) as f:
        diz=json.load(f)
        if x not in diz.keys():
            risultato=dict()
            with open(fout,mode='w',encoding='utf-8') as d:
               json.dump(risultato,d)
           
        else:
            l1=[]
            l2=[]
            valori=diz[x]
            liste=sottalbero(diz,x,valori,l1,l2)
            risultato= dict(zip(liste[0],liste[1]))
            with open(fout,mode='w',encoding='utf-8') as d:
               json.dump(risultato,d)
            
        
        
def sottalbero(d,x,valori,l1,l2):
    if valori==[]:
        l1.append(x)
        l2.append(d[x])
        return [list(reversed(l1)),list(reversed(l2))]
    else:
        l1.append(x)
        l2.append(d[x])
        x=valori[-1]
        valori2=valori[:-1]+d[x]
        return sottalbero(d,x,valori2,l1,l2)
        
        
        
        
        
         
         
        
    
          
    

def cancella_sottoalbero(fnome,x,fout):
     with open(fnome) as f:
        diz=json.load(f)
        if x not in diz.keys():
            with open(fout,mode='w',encoding='utf-8') as d:
               json.dump(diz,d)
        else:
            valori=diz[x]
            risultato=cancella(diz,x,valori)
            for v in risultato.values():
                if x in v:
                    v.remove(x)
                    break
            with open(fout,mode='w',encoding='utf-8') as d:
               json.dump(risultato,d)

def cancella(d,x,valori):
    if valori==[]:
        d.pop(x)
        return d
    else:
        d.pop(x)
        x=valori[-1]
        valori2=valori[:-1]+d[x]
        return cancella(d,x,valori2)

def dizionario_livelli(fnome,fout):
    with open(fnome) as f:
        diz=json.load(f)
        radice=trova_radice(diz)
        ris=dict()
        liv=0
        v=[]
        risultato=crea_diz(diz,radice,liv,ris,v)
        with open(fout,mode='w',encoding='utf-8') as d:
           json.dump(risultato,d)
           
def crea_diz(d,r,l,ris,v):
    if r==[]:
        return ris
    else:
        if len(r)==1:
            if l in ris.keys():
                l+=1
                r=sorted(v)
                v=[]
                return crea_diz(d,r,l,ris,v)
            else:
                ris.update({l:r})
                l+=1
                v=v+d[r[0]]
                r=sorted(v)
                v=[]
                return crea_diz(d,r,l,ris,v)
        else:
           if l in ris.keys():
            ris[l]=sorted(ris[l]+r)
           else:
            ris.update({l:r})
           for x in r:
            v+=d[x]
           return crea_diz(d,[r[0]],l,ris,v)
    
def trova_radice (diz):
    lis1=set()
    lis2=set()
    for k in diz.keys():
        lis1.add(k)
    for v in diz.values():
        for i in v:
            lis2.add(i)
    return list(lis1.difference(lis2))
        
             
   
        


def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as f:
        diz=json.load(f)
        radice=trova_radice(diz)
        ris={radice[0]:0}
        while radice != []:
            if len(diz[radice[0]])==y:
               ris=diz_gradi(diz[radice[0]],ris,ris[radice[0]]+1)
               
            else:
               ris=diz_gradi(diz[radice[0]],ris,ris[radice[0]]) 
            radice=radice[1:]+diz[radice[0]]
        with open(fout,mode='w',encoding='utf-8') as d:
            json.dump(ris,d)
        
def diz_gradi(lista,ris,g):
    if lista==[]:
        return ris
    else:
        ris.update({lista[0]:g})
        return diz_gradi(lista[1:],ris,g)
            
        
           
            
        
            
                
        
        
        
        
        

   
    
            
            
            
    
    
    
        
        
        
        
