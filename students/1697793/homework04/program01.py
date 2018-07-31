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

def getRootKey (tree):

    rootKey = None

    obj = {}

    #lista apoggio di chavi che hanno i figli
    for key in tree:
        for i in range(len(tree[key])):
            obj[tree[key][i]] = True

    for key in tree:
        if obj.get(key, None) == None:
            rootKey = key
            break

    return rootKey

def openJson(name):

    with open(name) as json_data:
        return json.load(json_data)

def saveJson(name, data):
    
    outFile = open(name,'w')
    json.dump(data, outFile)

def getSubTree (key, tree, finalSubTree):

    finalSubTree[key] = tree[key]

    if len(tree[key]) > 0:

        for i in range(len(tree[key])):
            getSubTree(tree[key][i], tree, finalSubTree)

def deleteSubTree (key, tree):

    if len(tree[key]) > 0:

        for i in range(len(tree[key])):
            deleteSubTree(tree[key][i], tree)

    del tree[key]

def getTreeLevels (key, tree, finalTree, level):

    if not finalTree.get(level, False):
        finalTree[level] = []

    finalTree[level].append(key)

    if len(tree[key]) > 0:

        for i in range(len(tree[key])):
            getTreeLevels(tree[key][i], tree, finalTree, level+1)

    finalTree[level].sort()
'''
def getAncestorsGrades(tree, mainKey, grade, finalTree, currentMainKey): #TODO IMPROVE CODE FOR TIME

    for key in tree:
        if currentMainKey in tree[key]:
            if len(tree[key]) == grade:
                finalTree[mainKey]+=1
            getAncestorsGrades(tree, mainKey, grade, finalTree, key)
            break
'''
#{"a": ["b"], "b": ["c", "d"], "c": ["i"], "d": ["e", "l"], "e": ["f", "g", "h"], "f": [], "g": [], "h": [], "i": [], "l": []}

def getAncestorsGrades(tree, fatherKey, mainGrade, finalTree, fatherGrade): #TODO IMPROVE CODE FOR TIME

    #get sons
    sons = tree[fatherKey] 

    #get grade of father
    totals = len(sons)

    #itherate sons and if father grade equals to mainGrade, increment current son
    for iSon in range(totals):   

        #initialize son
        finalTree[sons[iSon]] = fatherGrade

        #check if can increment
        if totals == mainGrade:
            finalTree[sons[iSon]] +=1

        getAncestorsGrades(tree, sons[iSon], mainGrade, finalTree, finalTree[sons[iSon]])


# *********************

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''

    tree = openJson(fnome)

    finalSubTree = {}

    getSubTree(x, tree, finalSubTree)

    saveJson(fout, finalSubTree)
    

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''

    tree = openJson(fnome)

    deleteSubTree(x, tree)

    for key, value in tree.items():

      if x in value:
        value.remove(x)

    saveJson(fout, tree)
    

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''

    tree = openJson(fnome)

    x = getRootKey(tree)

    finalTree = {}

    getTreeLevels(x, tree, finalTree, 0)

    saveJson(fout, finalTree)
 
'''
def dizionario_gradi_antenati(fnome,y,fout):

    tree = openJson(fnome)

    finalTree = {}

    for mainKey in tree:

        finalTree[mainKey] = 0

        getAncestorsGrades(tree, mainKey, y, finalTree, mainKey)

    saveJson(fout, finalTree)
 '''

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''

    tree = openJson(fnome)

    rootKey = getRootKey(tree)

    #initialize root
    finalTree = {
        rootKey: 0
    }

    getAncestorsGrades(tree, rootKey, y, finalTree, 0)

    saveJson(fout, finalTree)
