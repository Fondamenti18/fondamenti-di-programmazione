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

class nodo:
    def __init__(self,x,l=0):
        self.valore=x
        self.lista_figli=[]
        self.livello=l
        self.grado=0

def trova_radice(d):
    ins=set()
    r=None
    for v in d.values():
        for v1 in v:
            ins.add(v1)
    for k in d.keys():
        if not k in ins:
            r=nodo(k)
            break
    return r


def crea_albero(d,radice,stop=None):
    if d[radice.valore]==[]: return radice
    for v in d[radice.valore]:
        if v!=stop:
            r=nodo(v,radice.livello+1)
            r=crea_albero(d,r,stop)
            radice.lista_figli+=[r]
    radice.grado=len(radice.lista_figli)
    return radice


def crea_diz(diz,d,radice,stop=None):
    if diz=={}:
        diz[radice.valore]=[]
        for v in d[radice.valore]:
            if v!=stop:
                diz[radice.valore]+=[v]
    if radice.lista_figli==[]:diz[radice.valore]=[]
    else:
        for r in radice.lista_figli:
            diz[r.valore]=[]
            for v in d[r.valore]:
                if v!=stop:
                    diz[r.valore]+=[v]
            crea_diz(diz,d,r,stop)

def crea_diz2(diz,radice):
    if diz=={}:diz['0']=[radice.valore]
    if radice.lista_figli!=[]:
        for r in radice.lista_figli:
            if not str(r.livello) in diz.keys():
                diz[str(r.livello)]=[]
            diz[str(r.livello)]+=[r.valore]
            crea_diz2(diz,r)
    diz[str(radice.livello)].sort()
            
def crea_diz3(diz,radice,grado,tot=0):
    if diz=={}:diz[radice.valore]=tot
    if radice.grado==grado: tot+=1
    for r in radice.lista_figli:
        diz[r.valore]=tot
        crea_diz3(diz,r,grado,tot)

        
import json

  
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome)
    d=json.load(f)
    f.close()
    diz={}
    if x in d.keys():
        radice=nodo(x)
        radice=crea_albero(d,radice)
        crea_diz(diz,d,radice)
    f=open(fout,'w')
    json.dump(diz,f)
    f.close()
    

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome)
    d=json.load(f)
    f.close()
    diz={}
    radice=trova_radice(d)
    if radice.valore!=x:
        radice=crea_albero(d,radice,x)
        crea_diz(diz,d,radice,x)
    f=open(fout,'w')
    json.dump(diz,f)
    f.close()

    
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome)
    d=json.load(f)
    f.close()
    diz={}
    radice=trova_radice(d)
    radice=crea_albero(d,radice)
    crea_diz2(diz,radice)
    f=open(fout,'w')
    json.dump(diz,f)
    f.close()
    
    
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome)
    d=json.load(f)
    f.close()
    diz={}
    radice=trova_radice(d)
    radice=crea_albero(d,radice)
    crea_diz3(diz,radice,y)
    f=open(fout,'w')
    json.dump(diz,f)
    f.close()