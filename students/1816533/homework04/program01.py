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

def load_dict(fnome):

    with open(fnome, "r") as IN:

        return json.load(IN)

def getRoot(fname):

    root = ""
    
    with open(fname, "r") as IN:
        for line in IN:
            for i in range(len(line)):
                if(line[i] == '\"'):
                    counter = i + 1
                    while(line[counter] != '\"'):
                        root += line[counter]
                        counter += 1
                    return root
                    
def print_toFile(dictionary, fout):

    with open(fout, "w") as OUT:
        
        json.dump(dictionary, OUT, sort_keys=True)

def addNodes(node, d, result):
    
    result[node] = []
    if d[node] == []:
        return
    for nodo in d[node]:
        result[node].append(nodo)
        addNodes(nodo, d, result)

def genera_sottoalbero(fnome,x,fout):

    d = load_dict(fnome)

    result = {}

    if x not in d:
        print_toFile(result, fout)

    addNodes(x, d, result)
    print_toFile(result, fout)
    return

def get_RemoveList(node, d, to_remove):

    if d[node] == []:
        return
    for nodo in d[node]:
        to_remove.append(nodo)
        get_RemoveList(nodo, d, to_remove)

def cancella_sottoalbero(fnome,x,fout):
    
    d = load_dict(fnome)

    if x not in d:
        print_toFile(d, fout)

    to_remove = [x]

    get_RemoveList(x, d, to_remove)
    for victim in to_remove:
        d.pop(victim)
    for key in d:
        if x in d[key]:
            d[key].remove(x)
    print_toFile(d, fout)
    return

def getLevel(node, d, level, result):

    if d[node] == []:
        return
    for elem in d[node]:
        result[elem] = level
        getLevel(elem, d, level+1, result)

def sortLevel(dictionary, result):
    for tupla in dictionary:
        if tupla[1] not in result:
            result[tupla[1]] = []
            result[tupla[1]].append(tupla[0])
        else:
            result[tupla[1]].append(tupla[0])
    return result
    
def dizionario_livelli(fnome,fout):

    d = load_dict(fnome)

    aux = {}
    result = {}

    level = 0

    root = getRoot(fnome)
    aux[root] = level
    getLevel(root, d, level + 1, aux)
    aux = sorted(aux.items(), key=lambda x: x[1])
    sortLevel(aux, result)

    for key in result:
        result[key] = sorted(result[key])
    
    print_toFile(result, fout)
    return

def getAntenato(node, dictionary):

    for key in dictionary:
        if node in dictionary[key]:
            return key

def getGrade(node, dictionary, root, ancestors):
    
    if node == root:
        return 0
    if len(dictionary[ancestors[node]]) == 2:
        return 1 + getGrade(ancestors[node], dictionary, root, ancestors)
    else:
        return getGrade(ancestors[node], dictionary, root, ancestors) 

def dizionario_gradi_antenati(fnome,y,fout):
    
    d = load_dict(fnome)

    root = getRoot(fnome)

    aux = {}

    result = {}

    for key in d:
        if key == root:
            aux[key] = None
        else:
            aux[key] = getAntenato(key, d)

    for key in sorted(d.keys(), reverse=True):
        result[key] = getGrade(key, d, root, aux)

    print_toFile(result, fout)
    return