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
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as y:
        dizionario = json.load(y)

    radice = generaAlbero(x,dizionario,y=None)
    d = {}
    if x in dizionario:
        d = genDizionario(radice,d)
        
    with open(fout,'w') as outfile:
        json.dump(d,outfile)
    
    return radice


def generaAlbero(x,dizionario,y):
    radice = TNode(x,y)
    listaFigli = []
    for k,v in dizionario.items():
        if ( k == str(x) ):
            listaFigli = v
    for i in listaFigli:
        radice.figli+=[(generaAlbero(i,dizionario,x))]    #lista dei figli aumenta 
        
    return radice

def genDizionario(radice,d):
    lis=[]
    for i in radice.figli:
        lis+=[i.nome]
    d[radice.nome]=lis     
    for x in radice.figli:
        genDizionario(x,d)

    return d

def stampa_albero(radice,livello=0):
    print('    '*livello+radice.nome)
    for figlio in radice.figli:
        stampa_albero(figlio,livello+1)
        
def teo(albero, d,livello=0):
    nodo = albero.nome
    l = []
    if livello not in d:  #livello è la chiave
        l += [nodo]
        d[livello] = l
    else:
        d.get(livello).append(nodo)
        l = sorted(d.get(livello))
        d[livello] = l
    for figlio in albero.figli:
        teo(figlio,d,livello+1)
    return d

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as y:
        dizionario = json.load(y)
        
    radice=generaAlbero(x,dizionario,y=None)
    nodi=nodiTotali(radice)
    d={}
    for k,v in dizionario.items():
        if radice.searchNode(k) not in nodi:
            for j in v:
                if radice.searchNode(j) in nodi:
                    v.remove(j)
            d[k] = v
    
    with open(fout,'w') as outfile:
        json.dump(d,outfile) 
        
def nodiTotali(radice):
    lis=[]
    lis+=[radice]
    for x in radice.figli:
        lis+= nodiTotali(x)
    return lis

'''def nodeToString(radice):
    lis = nodiTotali(radice)
    l=[]
    for x in lis:
        l+=[x.nome]
    return l'''

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as y:
        dizionario = json.load(y)
        
    listaDiz=list(dizionario.keys())
    t= listaDiz[0]
    albero= generaAlbero(t, dizionario,None)
    d = {}
    d=teo(albero,d)
    
    '''r=list(d.values())
   
    k=0
    for k, v in d.items():
        p=r[k]
        p=sorted(p)
        d[k] = p
        k+=1'''
        
    with open(fout,'w') as outfile:
        json.dump(d,outfile)

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as x:
        dizionario = json.load(x)
        
    listaDiz=list(dizionario.keys())
    t= listaDiz[0]
    radice= generaAlbero(t, dizionario,None)
    d={}
    nodi=nodiTotali(radice)
    for n in nodi:
        count = parenti(radice,n,y)
        d[n.nome] = count
        
    with open(fout,'w') as outfile:
        json.dump(d,outfile)
    
def parenti(radice ,x,y,count=0):
    if x.padre==None:
        return count
    padre = radice.searchNode(x.padre)
    if len(padre.figli)==y:
        count += 1
    return parenti(radice,padre,y,count)


class TNode(object):
    def __init__(self,w,f):
        self.nome=w
        self.figli=[]
        self.padre=f
    def __str__(self):
        return 'Nodo('+self.nome+')'
    def searchNode(self,x):
        if self.nome==x:
            return self
        for figlio in self.figli:
            nodo=figlio.searchNode(x)
            if nodo is not None:
                return nodo
    
    
      
#print(genera_sottoalbero('Alb10.json','a','tAlb10_1.json').altezza())
#print(dizionario_gradi_antenati('Alb10.json',2,'tAlb10_1.json'))
#print(dizionario_livelli('Alb10.json','tAlb10_3.json'))