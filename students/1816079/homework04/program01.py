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



from collections import defaultdict
import json

def genera_sottoalbero(fnome,x,fout):
    d = load_dict(fnome)
    
    rad = gen_tree(d, x)
    d1 = tree_dict(rad)
    
    save_dict(d1, fout)
    

def cancella_sottoalbero(fnome,x,fout):
    d = load_dict(fnome)
    
    rad = sub_tree(d, x, next(iter(d)))
    d1 = tree_dict(rad)
    
    save_dict(d1, fout)
    

def dizionario_livelli(fnome,fout):
    d = load_dict(fnome)
    
    rad = gen_tree(d, next(iter(d)))
    d1 = tree_dict_bylevel(rad)
    
    save_dict(d1, fout)
 

def dizionario_gradi_antenati(fnome,y,fout):
    d = load_dict(fnome)
    
    agrad = grad_tree(d, next(iter(d)), y)
    
    save_dict(agrad, fout)
    
    
    
class Nodo():
    def __init__(self,x):
        self.nome = x
        self.figli = [] #lista dei nodi figli
    
def gen_tree(d, rad):
    nodo = Nodo(rad)
    for child in d[rad]:
        nodo.figli.append(gen_tree(d, child))
    return nodo

def sub_tree(d, sub, rad):
    nodo = Nodo(rad)
    for child in d[rad]:
        if child == sub:
            continue
        nodo.figli.append(sub_tree(d, sub, child))
    return nodo

def grad_tree(d, rad, grad, dgrad = [0], a = {}):
    a[rad] = dgrad.count(grad)
    dgrad.append(len(d[rad]))
    for child in d[rad]:
        grad_tree(d, child, grad, dgrad, a)
    return a
'''
def tree_dict(rad, di = {}):
    print(di)
    di[rad.nome] = []
    for figlio in rad.figli:
        di[rad.nome].append(figlio.nome)
        print(di)
        tree_dict(figlio, di)
    return di
'''
def tree_dict(rad):
    di = {}
    di[rad.nome] = []
    for figlio in rad.figli:
        di[rad.nome].append(figlio.nome)
        di.update(tree_dict(figlio))
    return di
'''
def tree_dict_bylevel(rad, d = {}, lvl = 0):
    print(d)
    if d.get(lvl):
        d[lvl].append(rad.nome)
        d[lvl].sort()
    else:
        d[lvl] = [rad.nome]
    for figlio in rad.figli:
        tree_dict_bylevel(figlio, d, lvl+1)
    return d
'''  
def tree_dict_bylevel(rad, lvl = 0):
    di = defaultdict(list)
    di[lvl].append(rad.nome)
    for figlio in rad.figli:
        di2 = tree_dict_bylevel(figlio, lvl+1)
        if di2.get(lvl+1):
            di[lvl].extend(di2.get(lvl+1))
        di.update(di2)
    return di

def load_dict(fname):
    with open(fname, 'r') as f:
        d = json.load(f)
    return d

def save_dict(d, fname):
    with open(fname, 'w') as f:
        f.write(json.dumps(d))
    return True



