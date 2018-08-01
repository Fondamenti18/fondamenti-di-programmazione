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

ad=(next (iter (d)))
    erasel(x,d,next (iter (d[ad])))
'''




import json
from copy import deepcopy
class nodo:
    def ___init___(self,x):
        self.valore=x
        self.attributo=None
        
def albero(diz,x,d):
    d[x]=diz[x]
    for y in diz[x]:
        albero(diz,y,d)
    return d
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome)
    ff=open(fout,'w')
    diz=json.load(f)
    d={}
    d=albero(diz,x,d)
    json.dump(d,ff)
    f.close()

def erase(diz,x,d):

    #print(x)
    del d[x]
    #print(d)
    for y in diz[x]:
        #print(y)
        erase(diz,y,d)
    #print(d)
    return d
def erasel(d,n,x,ls): #da vedere il limite di ricorsioni per i 20.000 nodi
    if ls[-1] == ls[n]:
        return d
    if x in d[ls[n]]:
        d[ls[n]].remove(x)
    erasel(d,n+1,x,ls)
    return d
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome)
    ff=open(fout,'w')
    diz=json.load(f)
    #print(diz)
    d={}    
    d=deepcopy(diz)
    d=erase(diz,x,d)
    for y in d:
        if x in d[y]:
            d[y].remove(x)
    #print(d)
    #ls=list(d.keys())
    #print(len(ls))
    #d=erasel(d,0,x,ls)
    json.dump(d,ff)
    f.close()
    
def choose(d,n,ls):
    if n in d:
        d[n]+=ls
    else:
        d[n]=ls    
def livello(diz,ls,d,n):
    
    if ls == []:
        return d    
    choose(d,n,ls)
    d[n]=sorted(d[n])
    if len(ls) > 1:
        for x in ls:
            livello(diz,diz[x],d,n+1)
    else:
        livello(diz,diz[str(ls).strip("[']")],d,n+1)


    return d
def cercaRad(diz):
    cacca=str(list(diz.values())).replace('[','').replace(']','')
    #radiz=''
    for xx in reversed(list(diz.keys())):
        if xx not in cacca:
            return xx
            
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome)
    ff=open(fout,'w')
    d={}
    radiz=''
    diz=json.load(f)
    radiz=cercaRad(diz)
    d[0]=[radiz]
    #print(diz[ls[0]])
    d=livello(diz,diz[radiz],d,1)
    json.dump(d,ff)
    f.close()
    
def patrimonio(diz,n,ls,y,d):
    d[ls]=n
    if len(diz[ls]) == y:
        n=n+1
        #print(ls)
    
    for x in diz[ls]:
        patrimonio(diz,n,x,y,d)
    return d
def dizionario_gradi_antenati(fnome,y,fout):#controlla i figli se ne ha 2 spara un count 1 ai suoi figli, eredita
    '''inserire qui il vostro codice'''
    f=open(fnome)
    ff=open(fout,'w')
    diz=json.load(f)
    d={}
    radiz=''
    radiz=cercaRad(diz)

    d=patrimonio(diz,0,radiz,y,d)
    json.dump(d,ff)
    f.close()
#{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}
#genera_sottoalbero('Alb10.json','d','tAlb10_1.json')

#cancella_sottoalbero('Alb20000.json','felici','tAlb20000_2.json')

dizionario_livelli('Alb10.json','tAlb10_3.json')

#dizionario_gradi_antenati('Alb10.json',2,'tAlb10_4.json')