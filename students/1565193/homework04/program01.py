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

def genera(albero,gentree,x):
       
    if x in albero:
        gentree.setdefault(x,albero[x])

        for i in albero[x]:                
            x=i
            genera(albero,gentree,x)
                
    return gentree
    
  
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''  

    gentree={}
    a=open(fnome)
    albero=json.load(a)
    gentree=genera(albero,gentree,x)                        
    a=open(fout,'w')
    json.dump(gentree,a)


def cancella(albero,alberosw,x):

    if x in albero:
        del albero[x]
        
        for i in alberosw[x]:                
            x=i
            cancella(albero,alberosw,x)
            
    return albero

    
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    
    alberosw={}
    a=open(fnome)
    albero=json.load(a)
    alberosw=albero.copy()
    albero=cancella(albero,alberosw,x)
    
    for i in albero.values(): 
            if x in i: 
                i.remove(x)
                break
            
    a=open(fout,'w')
    json.dump(albero,a)


def livelling(livelli,liv,albero,inizio):
        
    for i in albero[inizio]:
        livelli.setdefault(liv,[])
        if inizio not in livelli[liv]: livelli[liv].append(inizio)
        livelling(livelli,liv+1,albero,i)
        
    if albero[inizio]==[]:
        livelli.setdefault(liv,[])
        livelli[liv].append(inizio)
        
    return livelli
    
    
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    
    livelli={}
    inizio=''
    liv=0
    a=open(fnome)
    albero=json.load(a)
    alberosw=albero.copy()
    
    for i in albero.values():
        if len(alberosw)==1: break
        for j in i:
            if j in alberosw: del alberosw[j]
            
            #inizio=i
        
    
    inizio=tuple(alberosw.keys())[-1]
    livelli=livelling(livelli,liv,albero,inizio)
    
    [livelli[i].sort() for i in livelli]
    
    a=open(fout,'w')
    json.dump(livelli,a)
    

def grad_ant(num_ant,y,albero,num,inizio):
    
    for i in albero[inizio]:
        num_ant.setdefault(inizio,num)

        if len(albero[inizio])==y: 
            grad_ant(num_ant,y,albero,num+1,i)
        else: 
            grad_ant(num_ant,y,albero,num,i)
        
    if albero[inizio]==[]: num_ant.setdefault(inizio,num)
        
    return num_ant
        

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    
    num_ant={}
    inizio=''
    num=0
    a=open(fnome)
    albero=json.load(a)
    alberosw=albero.copy()
    
    for i in albero.values():
        if len(alberosw)==1: break
        for j in i:
            if j in alberosw: del alberosw[j]
            
            #inizio=i
        
    
    inizio=tuple(alberosw.keys())[-1]
    num_ant=grad_ant(num_ant,y,albero,num,inizio)
    a=open(fout,'w')
    json.dump(num_ant,a)