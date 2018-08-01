'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero  e l'attributo della chiave 
e' la lista 
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

costruisce il  dizionario che ha come  chiavi i livelli del dizionario-albero d. L'attributo 
di una 
chiave di valore x e' la lista degli identificativi  dei nodi che si trovano a livello x  
nell'albero rappresentato da d. 
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


class Nodo:
    def __init__(self,io,listaFigli,padre=''):
        self.io=io
        self.listaFigli=listaFigli
        self.padre=padre
        
    def tornaIo(self):
        return self.io
        
    def tornaFigli(self):
        return self.listaFigli
    
    def tornaPadre(self):
        return self.padre
    
    def set_Padre(self, padre2):
        self.padre=padre2



'''Ricorda di controllare se esiste x'''
def genera_sottoalbero(fnome,x,fout):
    '''Apertura file'''
    with open(fnome) as json_file:  
        diz = json.load(json_file)
    dizOut={}
    dizOut[x]=diz[x]
    gen (dizOut, diz[x], diz)
    with open(fout, 'w') as fout:
        json.dump(dizOut, fout)
    
def gen (dizOut, diz, dizOrigin):
    for x in diz:
        dizOut[x]=dizOrigin[x]
        gen(dizOut, dizOrigin[x], dizOrigin)
    

def cancella_sottoalbero(fnome,x,fout):
    '''Apertura file'''
    with open(fnome) as json_file:  
        diz = json.load(json_file)
    dizOut={}
    t=''
    dizOut[x]=diz[x]
    dizOrigin=canc (dizOut, diz[x], diz)
    del(dizOrigin[x])
    for y in dizOrigin:
        if x in dizOrigin[y]:
            t=dizOrigin[y]
            t.remove(x)
            dizOrigin[y]=t
    with open(fout, 'w') as fout:
        json.dump(dizOrigin, fout)
    
def canc (dizOut, diz, dizOrigin):
    for x in diz:
        dizOut[x]=dizOrigin[x]
        canc(dizOut, dizOrigin[x], dizOrigin)
        del(dizOrigin[x])
    return dizOrigin
    
    

def albero (dizOrigin):
    listaDiz={}
    for x in dizOrigin:
        z=''
        for y in dizOrigin:
            if x in dizOrigin[y]:
                z=y
                break       
        listaDiz[x]=Nodo(x,dizOrigin[x],z)
    return listaDiz
    
def apriFile(fnome):
    with open(fnome) as json_file:  
        diz = json.load(json_file)
    return albero (diz)
    
def contaLivelli(x,listaDiz,conta=0):
    if listaDiz[x].tornaPadre() =='':
        return 0 
    return 1+ contaLivelli(listaDiz[x].tornaPadre(),listaDiz, conta)

def dizionario_livelli(fnome,fout):
    '''Apertura file'''
    listaDiz=apriFile(fnome) 
    listaFin={}
    for x in listaDiz:
        y=contaLivelli(listaDiz[x].tornaIo(),listaDiz)
        if y not in listaFin:
            listaFin[y]=[x]
        else:           
            listaFin[y]+=[x]
    for x in listaFin:
        y=listaFin[x]
        y.sort()
        listaFin[x]=y
    with open(fout, 'w') as fout:
        json.dump(listaFin, fout)
 

def contaAntenati(x,listaDiz,y,conta=0):
    if listaDiz[x].tornaPadre() =='':
        z=listaDiz[x].tornaFigli() 
        if len(z)==y:
            return 1
        else:
            return 0
    z=listaDiz[x].tornaFigli()
    if len(z)==y: 
        return 1+ contaAntenati(listaDiz[x].tornaPadre(),listaDiz,y, conta)
    else:
        return contaAntenati(listaDiz[x].tornaPadre(),listaDiz,y, conta)

def dizionario_gradi_antenati(fnome,y,fout):
    listaDiz=apriFile(fnome)
    listaFin={}
    for x in listaDiz:
        z=listaDiz[x].tornaFigli()
        if len(z)==y:
            listaFin[x]=contaAntenati(listaDiz[x].tornaIo(),listaDiz,y)-1
        else:
            listaFin[x]=contaAntenati(listaDiz[x].tornaIo(),listaDiz,y)
    with open(fout, 'w') as fout:
        json.dump(listaFin, fout)
