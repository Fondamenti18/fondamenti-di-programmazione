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

def my_genera_sottoalbero(fnome,node,fout,tree):
    diz = {node: [figlio for figlio in tree[node]]}  #inizializzo il dizionario con i figli del nodo corrente
    for figlio in diz.copy()[node]:  # per ogni figlio del nodo corrente, aggiorno il dizionario ricorsivamente
        diz.update(my_genera_sottoalbero(fnome, figlio, fout, tree))
    return diz

def genera_sottoalbero(fnome,x,fout):
    with open(fnome) as file:
        tree = json.load(file)
    diz = my_genera_sottoalbero(fnome, x, fout, tree)
    with open(fout, 'w') as file:
        json.dump(diz, file)


def my_cancella_sottoalbero(fnome, x, fout, tree):
    if tree.get(x, None) == None:    # caso base: sono una foglia, allora mi tolgo dall'albero
        tree.pop(x)
    else:
        # ricorsione: per ogni figlio, prima elimino ricorsivamente i loro sottoalberi, poi elimino i figli stessi
        for figlio in tree[x][:]:
            tree = my_cancella_sottoalbero(fnome, figlio, fout, tree)
            if figlio in tree[x]:
                tree[x].remove(figlio)
        tree.pop(x)    # infine elimino il nodo corrente
    for n, figli in tree.items():     # rimuovo il puntatore al nodo della prima chiamata dal padre di nodo
        if x in figli:
            figli.remove(x)
    return tree

def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as file:
        tree = json.load(file)
    tree = my_cancella_sottoalbero(fnome, x, fout, tree)
    with open(fout, 'w') as file:
        json.dump(tree, file)


def my_dizionario_livelli(fnome, fout, diz, tree, index):
    lista_livello = []
    for nodo in diz[index-1]:
        for figlio in tree[nodo]:
            lista_livello.append(figlio)
    if lista_livello != []:
        diz[index] = sorted(lista_livello)
        my_dizionario_livelli(fnome, fout, diz, tree, index + 1)

def dizionario_livelli(fnome,fout):
    with open(fnome) as file:
        tree = json.load(file)

    tutti_figli = set()
    for figli in tree.values():
        for figlio in figli:
            tutti_figli.add(figlio)
    tot_nodi = tree.keys()
    tot_nodi = set(tot_nodi)
    root = tot_nodi.difference(tutti_figli).pop()

    dizionario = {};
    dizionario[0] = [root]

    my_dizionario_livelli(fnome, fout, dizionario, tree, 1)
    with open(fout, 'w') as file:
        json.dump(dizionario, file)


def my_dizionario_gradi_antenati(fnome, y, fout, tree, diz, node, c):
    diz[node] = c  # assegno il numero di antenati di grado y al nodo corrente
    if len(tree[node]) == y:
        c += 1
        # se il nodo corrente è di grado y, tutti i suoi discendenti avranno un numero count+1 di antenati con grado y
    for figlio in tree[node]:
        my_dizionario_gradi_antenati(fnome, y, fout, tree, diz, figlio, c)

def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as file:
        tree = json.load(file)
    diz = {}
    tutti_figli = set()
    for figli in tree.values():
        for figlio in figli:
            tutti_figli.add(figlio)
    tot_nodi = tree.keys()
    tot_nodi = set(tot_nodi)
    my_dizionario_gradi_antenati(fnome, y, fout, tree, diz, tot_nodi.difference(tutti_figli).pop(), 0)
    with open(fout, 'w') as f:
        json.dump(diz, f)


genera_sottoalbero('Alb10.json', 'd', 'tAlb10_1.json')