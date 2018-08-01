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


def genera_sottoalbero(fnome, x, fout):
    '''inserire qui il vostro codice'''

    output_tree = {}

    with open(fnome, 'r') as input_file:
        tree = json.load(input_file)
        input_file.close()

    list_of_nodes = [x]

    '''using the fact that empty list is equal to false in Python'''
    while list_of_nodes:
        node = list_of_nodes.pop()  # removes and returns the last item in the list
        output_tree[node] = tree[node]
        list_of_nodes += tree[node]

    with open(fout, 'w') as output_file:
        json.dump(output_tree, output_file)
        output_file.close()


def cancella_sottoalbero(fnome, x, fout):
    '''inserire qui il vostro codice'''

    with open(fnome, 'r') as input_file:
        tree = json.load(input_file)
        input_file.close()

    list_of_nodes = []

    if x in list(tree.keys()):

        '''removing node x'''
        for k in tree.keys():
            if x in tree[k]:
                tree[k].remove(x)
                break

        '''removing x's children'''
        list_of_nodes += [x]
        while list_of_nodes:
            node = list_of_nodes.pop()  # removes and returns the last item in the list
            list_of_nodes += tree[node]
            del tree[node]

    with open(fout, 'w') as output_file:
        json.dump(tree, output_file)
        output_file.close()


def dizionario_livelli(fnome, fout):
    '''inserire qui il vostro codice'''

    out_dict = {}

    with open(fnome, 'r') as input_file:
        tree = json.load(input_file)
        input_file.close()

    root = list(tree.keys())[0]
    level = 0

    nodes_list = [root]

    while nodes_list:
        nodes_list.sort()
        out_dict[level] = nodes_list

        children_list = []
        for obj in nodes_list:
            children_list += tree[obj]

        nodes_list = children_list
        level += 1

    with open(fout, 'w') as output_file:
        json.dump(out_dict, output_file)
        output_file.close()


def dizionario_gradi_antenati(fnome, y, fout):
    '''inserire qui il vostro codice'''
    with open(fnome, 'r') as input_file:
        tree = json.load(input_file)
        input_file.close()

    result_dict = {}

    for node in list(tree.keys()):
        if len(tree[node]) == y:
            children_list = tree[node]
            while children_list:
                child = children_list.pop()
                result_dict[child] = result_dict.get(child, 0) + 1
                children_list += tree[child]

    for node in list(tree.keys()):
        result_dict[node] = result_dict.get(node, 0)

    with open(fout, 'w') as output_file:
        json.dump(result_dict, output_file)
        output_file.close()
