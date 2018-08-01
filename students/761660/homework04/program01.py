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
import copy
def sottoalbero(dout,din,x):
    dout[x]=[] 
    for v in din[x]: 
        dout[x]+=[v]
     
    for k in dout[x]:
         if din[k]!=[]:
             dout=sottoalbero(dout,din,k)
         else:
             dout[k]=[]
    return dout

'''def calcolalivello(din,dout,livello,k,esaminati):
        esaminati[k]=1
        dout[livello]=[k]
        if din[k]==[]:
            return esaminati,dout
        else:
            livello+=1
            for v in din[k]:
                esaminati,dout=calcolalivello(din,dout,livello,v,esaminati)'''

'''def calcolalivello(din,lista,k):
    h=len(lista)
    if len(lista)==0:
        return 0
    else:
            if  k in din[lista[h-1]]:
                lista.remove(lista[h-1])
                return calcolalivello(din,lista,k)+1'''
'''def calcolalivello(k,esaminati,h,din):
    
    if h==0:
        return 0
    p=esaminati[h-1]
    if(k in din[p]):
        return 1+calcolalivello(p,esaminati,h-1,din)
    else:
        return calcolalivello(k,esaminati,h-1,din) '''

def antenati(din,dp,k,y):
    b=dp[k]
    if(dp[k]==''):
        return 0
    else:
        a=len(din[b])
        h=dp[k]
        if (a-y)!=0:
            return antenati(din,dp,h,y)
        else:
            return antenati(din,dp,h,y)+1

def calcolalivello(h,din,dout,dp):
    if dp[h]=='':
        return 0
    k=dp[h]
    return calcolalivello(k,din,dout,dp)+1
          
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    dout={}
    with open(fnome,'r') as f:
        din=json.load(f)
    if x not in din.keys():
        dout={}
    else:
        dout=sottoalbero(dout,din,x)
    
    with open(fout,'w') as f:
        json.dump(dout,f)
    
def cancella_sottoalbero(fnome,x,fout):
  dout={}
  dout1={}
  with open(fnome,'r') as f:
      din=json.load(f)
 
  if x in din.keys():
      dout=sottoalbero(dout,din,x)
  for k in din.keys():
      if k not in dout.keys():
           dout1[k]=din[k] 
  for k in dout1.keys():
      for q in dout1[k]: 
          if q in dout.keys():
              dout1[k].remove(q)
  with open(fout,'w') as f:
      json.dump(dout1,f)
     
'''def dizionario_livelli(fnome,fout):'''
'''inserire qui il vostro codice'''
''' dout={}
    esaminati={}
    with open(fnome,'r') as f:
        din=json.load(f)
    livello=0
    dout[livello]=[]
    for k in din.keys():
        esaminati[k]=0
    for k in din.keys(): 
        if esaminati[k]==0:
           esaminati,dout=calcolalivello(din,dout,livello,k,esaminati)
    with open(fout,'w') as f:
        json.dump(dout,f)'''
'''def dizionario_livelli(fnome,fout):'''
'''inserire qui il vostro codice'''
'''dout={}
    lista=[]
    with open(fnome,'r') as f:
        din=json.load(f)
    
    livello=0
    for k in din.keys():
        dout[livello]=[]
        livello=calcolalivello(din,lista,k)
        dout[livello]+=[k]
        lista+=[k]
        print(livello)
    with open(fout,'w') as f:
        json.dump(dout,f)''' 
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    dout={}
    dp={}
    with open(fnome,'r') as f:
        din=json.load(f)
    livello=0
    for k in din.keys():
        dp[k]=''
        for h in din.keys():
            if k not in din[h]:
                continue
            else:
                dp[k]=h     
    dout[livello]=[]            
    for k in din.keys():
        livello=calcolalivello(k,din,dout,dp)
        dout[livello]+=[k]
        if din[k]!=[]:
            livello+=1
            dout[livello]=[]
    with open(fout,'w') as f:
        json.dump(dout,f)

        

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    dout={}
    dp={}
    with open(fnome,'r') as f:
        din=json.load(f)
    for k in din.keys():
        dp[k]=''
        for h in din.keys():
            if k not in din[h]:
                continue
            else:
                dp[k]=h   
    for k in din.keys():
        dout[k]=0
    for k in din.keys():
        
            dout[k]=antenati(din,dp,k,y)
    with open(fout,'w') as f:
        json.dump(dout,f)       