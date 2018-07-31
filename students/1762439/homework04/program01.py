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


class Nodo:
    def __init__(self, nome):
        self.nome = nome
        self.lista_figli = {} 
        self.lista_antenati = []


def gen1(x,da):
        if x in da:
            nodo = Nodo(x)
            nodo.lista_figli.update({x : da[x]})
            for k in da[x]:
                nodo.lista_figli.update(gen1(k,da))
        else:
            nodo = Nodo(x)
            nodo.lista_figli = {}
        return nodo.lista_figli
def genera_sottoalbero(fname, x, fout):
    #nuovo_diz = []
    f = open(fname)
    da = json.loads(f.read())
   
    
    with open(fout, 'w') as p:
            json.dump(gen1(x,da),p)








def canc1(x,da):
        if x in da:  
            nodo = Nodo(x)
            nodo.lista_figli.update({x : da[x]})
            for k in da[x]:
                nodo.lista_figli.update(canc1(k,da))
        else:
            nodo = Nodo(x)
            nodo.lista_figli = da
        return nodo.lista_figli

def cancella_sottoalbero(fname, x, fout):
    f = open(fname)
    da = json.loads(f.read())
   
    
    nuovo = da
    with open(fout, 'w') as l:
            for c in canc1(x,da).keys():
                del nuovo[c]
            for i in nuovo:
                if x in nuovo[i]:
                    (nuovo[i]).remove(x)
            json.dump(nuovo,l)





def rad1(fname):
    f = open(fname)
    d = json.loads(f.read())
    o = []
    p = set(d.keys())
    for j in d.values():
        o += [i for i in j]
            
    return  ''.join(p - set(o))
    
def dizi(nuv, prova, x, livello = 0):
        
        if livello in nuv.keys():
            nuv[livello] += [x]
        else:
            nuv.update({livello : [x] })
        
        for figlio in prova[x]:
            
            dizi( nuv, prova, figlio, livello + 1)
        return nuv
    
def ulti(x, nuv, prova):
        di = dizi(nuv, prova, x)
        for v in di.values():
            v.sort(key = str.lower)
        return di
def dizionario_livelli(fname, fout):
    
    xa = rad1(fname)
    f = open(fname)
    da = json.loads(f.read())
    
   
    nuv = {}    
    prova = da
    
    
    
    def ulti(x, nuv, prova):
        di = dizi(nuv, prova, x)
        for v in di.values():
            v.sort(key = str.lower)
        return di
    with open(fout, 'w') as l:
            json.dump(ulti(xa, nuv, prova),l) 



def gen41(xa,da, lu=0):
        
        try:
            m = xa.index('>>')
            l = xa[:m]
            lu = len(l)
        except ValueError:
            lu = len(xa)
        
        if xa[0:lu] in da:  
            
            nodo = Nodo(xa)
            dato = [p for p in xa[lu:]]
            
            nodo.lista_antenati += [str(len(da[xa[0:lu]])) ]
            for p in dato:
                nodo.lista_antenati += p
            val = [ x + '>>' + ''.join(nodo.lista_antenati) for x in da[xa[0:lu]]  ]
            
            nodo.lista_figli.update({xa : val})
            
            for k in val:
                #lu = a 
                nodo.lista_figli.update(gen41(k,da, lu))
        else:
            nodo = Nodo1(xa)
            nodo.lista_figli = {}
        return nodo.lista_figli

def dizionario_gradi_antenati(fname, y, fout):
    #nuovo_diz = []
    xa = rad1(fname)
    f = open(fname)
    da = json.loads(f.read())
    nu = {}
    for k in (gen41(xa,da)).keys():
        try:
            m = k.index('>>')
            l = k[:m]
            j = k[m:]
        except ValueError:
            l = k
            j = 'a'
        nu.update({l : j.count(str(y))})
        

    
    with open(fout, 'w') as l:
            json.dump(nu,l)
