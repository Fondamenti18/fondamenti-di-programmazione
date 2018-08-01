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
    with open(fnome) as file:
        dizio_alb=json.load(file)
        sottoalbero=ric_genera_albero(dizio_alb, x, sottoalbero={})
    with open(fout, 'w') as outfile:
        json.dump(sottoalbero, outfile)
def ric_genera_albero(dizio_alb, x, sottoalbero):   #sottofunzione di genera_albero
    for k in dizio_alb.keys():
        if x in k:
            sottoalbero[x]=sorted(dizio_alb[x])
            for el in dizio_alb[x]:
                ric_genera_albero(dizio_alb, el, sottoalbero)
    return sottoalbero


def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as file:
        dizio_alb=json.load(file)
        dizio_alb=ric_cancella_sottoalbero(dizio_alb, x)
        for v in dizio_alb.values():
            for i in v:
                if i==x:
                    v.remove(x)
    with open(fout, 'w') as outfile:
        json.dump(dizio_alb, outfile)
def ric_cancella_sottoalbero(dizio_alb, x): #sottofunzione di cancella_sottoalbero
    for k in dizio_alb.copy().keys():
        if x in k:
            figli=dizio_alb[x]
            del dizio_alb[x]
            for el in figli:
                ric_cancella_sottoalbero(dizio_alb, el)
    return dizio_alb


def dizionario_livelli(fnome,fout):
    with open(fnome) as file:
        dizio_alb=json.load(file)
        lista=[]
        for k in dizio_alb.keys():
            while len(lista)<2:
                lista+=[k]
        x=[lista[0]]
        alb_livelli=ric_dizionario_livelli(x, dizio_alb, alb_livelli={}, livello=0)
    with open(fout, 'w') as outfile:
        json.dump(alb_livelli, outfile)
def ric_dizionario_livelli(x, dizio_alb, alb_livelli, livello): #sottofunzione di dizionario_livelli
    if x==[]:
        return alb_livelli
    lista=[]
    alb_livelli[livello]=sorted(x)
    livello+=1
    for el in x:
        lista+=dizio_alb[el]
    ric_dizionario_livelli(lista, dizio_alb, alb_livelli, livello)
    return alb_livelli
     
    
def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as file:
        dizio_alb=json.load(file)
        lis_ant=[]
        alb_gradi={}
        for k in dizio_alb.keys():
            if len(dizio_alb[k])==y:
                lis_ant+=[k]
                alb_gradi[k]=0
                break
            else:
                alb_gradi[k]=0
        alb_gradi=ric_dizionario_gradi_antenati( alb_gradi, lis_ant, dizio_alb, y, tot=0)
    with open(fout, 'w') as outfile:
        json.dump(alb_gradi, outfile)
def ric_dizionario_gradi_antenati(alb_gradi, lis_ant, dizio_alb, y, tot):   #sottofunzione di dizionario_gradi_antenati
    if lis_ant!=[]:
        for el in lis_ant:
            if len(dizio_alb[el])==y:
                tot+=1
                for v in dizio_alb[el]:
                    alb_gradi[v]=tot
            else:
                for v in dizio_alb[el]:
                    alb_gradi[v]=tot
        ric_dizionario_gradi_antenati(alb_gradi, dizio_alb[el], dizio_alb, y, tot)
    return alb_gradi
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
