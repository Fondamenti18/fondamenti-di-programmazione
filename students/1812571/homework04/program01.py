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

def loadJSON(fname):
    with open(fname) as jFile:
        tree = json.load(jFile)
        return tree


def dumpJSON(fname, tree):
    with open(fname,"w") as jFile:
        json.dump(tree, jFile)


def getSubTree(tree, currentNode):
    nodesList = tree[currentNode]
    treeBranch = {currentNode : nodesList}
    for node in nodesList:
        treeBranch.update(getSubTree(tree, node))
    return treeBranch


def deleteSubTree(tree,currentNode):
    for subNodeID in tree[currentNode]:
        deleteSubTree(tree, subNodeID)
    del tree[currentNode]


def genera_sottoalbero(fnome,x,fout):
    tree = loadJSON(fnome)
    newTree = getSubTree(tree, x)
    dumpJSON(fout, newTree)


def findParentNode(tree):
    parentsList = []
    for key in tree:
        parentsList += [key]
    for key in tree:
        for item in tree[key]:
            parentsList.remove(item)
    return parentsList[0]


def createLevelsDict(tree, currentNode, levelsDict, deepness = 0):
    if (deepness in levelsDict):
        levelsDict[deepness].append(currentNode)
    else:
        levelsDict[deepness] = [currentNode]
    for node in tree[currentNode]:
        createLevelsDict(tree, node, levelsDict, deepness+1)
    
def createDictOfBlahBlahBlah(tree, currentNode, dictOfBBB, targetRank, currentCount = 0):
    dictOfBBB[currentNode] = currentCount
    if (len(tree[currentNode]) == targetRank):
        currentCount += 1
    for node in tree[currentNode]:
        createDictOfBlahBlahBlah(tree, node, dictOfBBB, targetRank, currentCount)


def cancella_sottoalbero(fnome,x,fout):
    tree = loadJSON(fnome)
    deleteSubTree(tree, x)
    for key, lst in tree.items():
        for cnt in range(0,len(lst)):
            if (lst[cnt] == x):
                del lst[cnt]
                dumpJSON(fout, tree)
                return


def dizionario_livelli(fnome,fout):
    tree = loadJSON(fnome)
    parentNode = findParentNode(tree)
    levelsDict = dict()
    createLevelsDict(tree, parentNode, levelsDict)
    for lst in levelsDict.values():
        lst.sort() 
    dumpJSON(fout, levelsDict)


def dizionario_gradi_antenati(fnome,y,fout):
    tree = loadJSON(fnome)
    parentNode = findParentNode(tree)
    dictOfBBB = dict()
    createDictOfBlahBlahBlah(tree, parentNode, dictOfBBB, y)  
    dumpJSON(fout,dictOfBBB)