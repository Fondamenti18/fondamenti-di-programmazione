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
def st(x,d2,d):# x indice da cercare, d2 dizionario vuoto , d dizionario da usare nella ricerca
    if x in d:
        figli=d[x]
        d2[x]=figli
        if figli!='[]':
            for figlio in figli:
                d2=st(figlio,d2,d)
            return d2
        else:
            return d2
    else:
        return d2
def dt(x,d):# x indice da cercare, d dizionario da usare nella ricerca
    if x in d:
        
        figli=d.pop(x,'[]')
        if figli!='[]':
            for figlio in figli:
                d=dt(figlio,d)
            return d
        else:
            return d
    else:
        return d
    
    
    
def tf2(d):
    figlio=next(iter (d.keys()))
    return figlio

def tp(d,figlio): #restituisce il padre maggiore
    ris=figlio
    for p,f in d.items():
        if figlio in f:
            ris=tp(d,p)
    
    return ris
def tp2(d,figlio):
    ris='[]'
    for p,f in d.items():
        if figlio in f:
            ris=p
            return ris
    
    return ris


def ta(d):
    figlio=tf2(d)
    antenato=tp(d,figlio)
    return antenato

def cl(d,d2,lvl,par):
    ls=[]
    ls.append(par)
    if lvl in d2:
        ls+=d2[lvl]
        ls.sort()
        d2[lvl]=ls
    else:
        d2[lvl]=ls
    
    figli=d[par]
    if figli!='[]':
        for figlio in figli:
            d2=cl(d,d2,lvl+1,figlio)
       
    return d2

def diza(d,d2,gr,y,pr):
    d2[pr]=gr
    figli=d[pr]
    if len(figli)==y:
        gr+=1
    for figlio in figli:
        d2=diza(d,d2,gr,y,figlio)
    return d2
    
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, 'r') as f:
        d = json.load(f)
        d2={}
        d2=st(x,d2,d)
        with open(fout, 'w') as f1:
            json.dump(d2, f1)   
    

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, 'r') as f:
        d = json.load(f)
        fl='f'
        for padre,figli in d.items():
            if x in figli:
                figli.remove(x)
                d[padre]=figli
                fl='t'
            if fl=='t':
                break
            
        d=dt(x,d)
        with open(fout, 'w') as f1:
            json.dump(d, f1)
    

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    
    with open(fnome, 'r') as f:
        d = json.load(f)
        
    radice=ta(d)   
    d2={}
    d2=cl(d,d2,0,radice)
        
        
    with open(fout, 'w') as f1:
            json.dump(d2, f1)    
 

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    
    
    with open(fnome, 'r') as f:
        d = json.load(f)
        
    radice=ta(d)   
    d2={}
    d2=diza(d,d2,0,y,radice)
        
        
    with open(fout, 'w') as f1:
            json.dump(d2, f1)   
