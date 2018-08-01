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
    tree = json.load(open(fnome))
    lista = {}
    func1(tree[x], tree, lista)
    lista[x] = tree[x]
    with open(fout, 'w') as f:
        json.dump(lista, f)
    
def func1(nodo, tree, lista):
    for key in nodo:
        if len(tree[key]) > 0:
            func1(tree[key], tree, lista)
        lista[key] = tree[key]
        
def cancella_sottoalbero(fnome,x,fout):
    tree = json.load(open(fnome))
    for key in tree:
        if x in tree[key]:
            tree[key].remove(x)
            break
        
    func2(tree.pop(x), tree)
    with open(fout, 'w') as f:
        json.dump(tree, f)

def func2(nodo, tree):
    for key in nodo:
        elem = tree.pop(key)
        if len(elem) > 0:
            func2(elem, tree)

def dizionario_livelli(fnome,fout):
    tree = json.load(open(fnome))
    lista = {} 
    key = findRoot(tree)
    
    #key = next(iter(tree))
    #print(key)
    lista[0] = [key]
    func3(key, tree, lista, 1)
    with open(fout, 'w') as f:
        json.dump(lista, f)
 
def func3(key, tree, lista, level):
    nodo = tree[key]
    if(len(nodo) == 0):
        return
    if level in lista.keys():
        
        lista[level] += nodo
        lista[level].sort()
    else:
        lista[level] = nodo
        lista[level].sort()
        
    for n in nodo:
        func3(n, tree, lista, level +1)
    
    
def dizionario_gradi_antenati(fnome,y,fout):
    tree = json.load(open(fnome))
    lista = {}
    global listaAnt
    listaAnt = {}
    global setAnt
    setAnt = set()
    print('starting find root....')
    global root 
    root = findRoot(tree)
    print('find root ended:' + root)
    lista[root] = 0
    
    func4(tree[root], y, tree, lista)
    
    with open(fout, 'w') as f:
        json.dump(lista, f)

def func4(nodo, y, tree, lista):
    #print('entro')
    for key in nodo:
        lista[key] = 0
        func4(tree[key], y, tree, lista)
        listaAntenati = findAntenati(key, tree, [])
        #print(listaAntenati)
        for ant in listaAntenati:
            grado = len(tree[ant])
            if grado == y:
                lista[key] += 1
        
    
def findAntenati(key, tree, listaAntenati):
    if key == root:
        return listaAntenati
    if key in setAnt:
        listaAntenati.append(listaAnt[key])
        findAntenati(listaAnt[key], tree, listaAntenati)
    else:
        for el in tree.keys():
            if key in tree[el]:
                listaAnt[key] = el
                setAnt.add(key)
                listaAntenati.append(el)
                findAntenati(el, tree, listaAntenati)
                break
    #print('returning:' + str(listaAntenati))
    return listaAntenati
            
def findRootKey(key, tree):
    flag = True
    for el in tree.keys():
        if key in tree[el]:
            flag = False
            root = findRootKey(el, tree)
            if root != '':
                return root
    if flag:
        return key
    else:
        return ''

def findRoot(tree):
# =============================================================================
#     chiavi = list(tree.keys())
#     
#     for el in tree.values():
#         newChiavi = []
#         for key in chiavi:
#             #print(key)
#             if key in el:
#                 newChiavi.append(key)
#         for x in newChiavi:
#             chiavi.remove(x)
#         if(len(chiavi) == 1):
#             return chiavi[0]
    chiavi = next(iter(tree))
     
    return findRootKey(chiavi, tree)