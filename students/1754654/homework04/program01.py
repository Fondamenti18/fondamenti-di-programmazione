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

search_child_dictionary = dict()
def genera_sottoalbero(fnome,x,fout):
    with open(fnome) as f: dict_tree = json.load(f)

    global search_child_dictionary
    search_child_dictionary = dict()

    for _ in dict_tree.items():
        if _[0] == x:
            dict_fout = search_child(dict_tree,_[0])

    with open(fout,'w') as wr:
       json.dump(dict_fout,wr)

    return search_child_dictionary

def search_child(d_tree, father):
    if d_tree[father] != []:
        for _ in d_tree[father]:
            search_child_dictionary[father] = d_tree[father]
            search_child(d_tree,_)
    else:
        search_child_dictionary[father] = []
        return
    return search_child_dictionary



delete_subtree_dictionary = dict()
def cancella_sottoalbero(fnome,x,fout):

    with open(fnome) as f_ile: d_tree = json.load(f_ile)

    for _ in d_tree.items():
        if _[0] == x:

            root = find_root(d_tree)

            r_dictionary = new_tree(d_tree,root,x)

            global delete_subtree_dictionary
            delete_subtree_dictionary = dict()

    with open(fout,'w') as f_ileout: json.dump(r_dictionary,f_ileout)

    return None

def find_root(tree):

    keylist = set()
    items = set()
    for key,value in tree.items():
        keylist.add(key)
        if value != []:
            for _ in value:
                items.add(_)

    r_value = list(keylist - items)
    return r_value[0]

def new_tree(tree_, root_,b_leaf):
    global delete_subtree_dictionary

    delete_subtree_dictionary[root_] = tree_[root_]

    if b_leaf in delete_subtree_dictionary[root_]:
        delete_subtree_dictionary[root_].remove(b_leaf)

    for elem in tree_[root_]:
        if elem != b_leaf:
            new_tree(tree_,elem,b_leaf)
    return delete_subtree_dictionary



dictionary_levels = dict()
def dizionario_livelli(fnome,fout):

    with open(fnome) as file_: tree_d = json.load(file_)

    root = find_root(tree_d)
    returned_dict = dict_levels(tree_d,root,0)

    for key, value in returned_dict.items():
        returned_dict[key] = sorted(value)

    with open(fout,'w')as w_r: json.dump(returned_dict,w_r)

    global dictionary_levels
    dictionary_levels = dict()

    return returned_dict

def dict_levels(tree_,root,level):

    global dictionary_levels
    if level not in dictionary_levels:
        dictionary_levels[level] = [root]
    else:
        if root not in dictionary_levels[level]:
            dictionary_levels[level].append(root)
    for elem_ in tree_[root]:
        dict_levels(tree_,elem_,level+1)
    return dictionary_levels



dictionary_el_son = dict() #dizionario con il numero di figli per ogni nodo
quar_dictionary = dict()
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    global dictionary_el_son
    global quar_dictionary
    dictionary_el_son = dict()
    quar_dictionary = dict()

    with open(fnome) as f_t: f_tree = json.load(f_t)
    root = find_root(f_tree)

    #dizionario con il numero di figli per ogni nodo
    h_son(f_tree,root)
    to_save_dict = quart_funct(f_tree,'',root,y)

    with open(fout,'w') as f_out: json.dump(to_save_dict,f_out)
    dictionary_el_son = dict()
    quart_dictionary = dict()
    return

def h_son(a_tree, root):
    global dictionary_el_son
    if a_tree[root] != []:
        dictionary_el_son[root] = len(a_tree[root])
    else:
        dictionary_el_son[root] = 0
    for element in a_tree[root]:
        h_son(a_tree,element)
    return dictionary_el_son

def quart_funct(an_tree,father,root,grade):
    global quar_dictionary
    global dictionary_el_son
    if father == '':
        quar_dictionary[root] = 0
    else:
        quar_dictionary[root] = quar_dictionary[father]
        if dictionary_el_son[father] == grade:
            quar_dictionary[root] = quar_dictionary[root] + 1
    for node in an_tree[root]:
        father_ = root
        quart_funct(an_tree,father_,node,grade)
    return quar_dictionary
