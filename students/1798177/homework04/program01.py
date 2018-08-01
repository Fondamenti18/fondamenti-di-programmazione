# Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come
# dizionario-albero) se ciascuna chiave di d è un identificativo di un nodo
# dell'albero e l'attributo della chiave è la lista (eventualmente vuota) degli
# identificativi dei figli del nodo. Gli identificativi dei nodi all'interno
# delle liste sono in ordine lessicografico crescente.
#
# Ecco un esempio di dizionario d che rappresenta un dizionario-albero:
#
# d = {
#  'a' : ['b'],
#  'b' : ['c','d'],
#  'c' : ['i'],
#  'd' : ['e','l'],
#  'e' : ['f','g','h'],
#  'f' : [],
#  'g' : [],
#  'h' : [],
#  'i' : [],
#  'l' : []
# }
#
# L'albero rappresentato da d é:
#
#                             'a'
#                              |
#                _____________'b'____________
#               |                            |
#              'c'                  ________'d'_______
#               |                  |                  |
#              'i'         _______'e'_______         'l'
#                         |        |        |
#                        'f'      'g'      'h'
#
# Implementare le seguenti funzioni:
#
# 1) la funzione genera_sottoalbero(fnome, x, fout) che, presi:
#  - il nome di un file json contenente un dizionario-albero d (fonome),
#  - un identificativo x,
#  - il nome di un file json (fout);
#  produce il dizionario-albero che rappresenta il sottoalbero radicato
#  nell'identificativo x che si ottiene dal dizionario-albero d. Il
#  dizionario-albero ottenuto va registrato nel file fout. Se l'identificativo x
#  non è tra i nodi di d allora il dizionario-albero prodotto deve essere
#  vuoto.
#
# Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione
# di genera_sottoalbero(fname, 'd', fout) il file fout conterrà il dizionario:
# {'f': [], 'g': [], 'h': [], 'e': ['f', 'g', 'h'], 'l': [], 'd': ['e', 'l']}.
#
# 2) la funzione cancella_sottoalbero(fnome, x, fout) che, presi:
#  - il nome di un file json contenente un dizionario-albero d (fonome),
#  - un identificativo x,
#  - il nome di un file json (fout);
# ricava da d il sottoalbero radicato in x e lo salva nel file fout. Se x non è
# presente tra le chiavi di d allora il dizionario-albero d non viene
# modificato.
#
# Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione
# di cancella_sottoalbero(fname, 'd', fout) il file fout conterrà il dizionario:
# {'a': ['b'], 'b': ['c'], 'c': ['i'], 'i':[]}.
#
# 3) la funzione dizionario_livelli(fnome, fout) che, presi:
#  - il nome di un file json contenente un dizionario-albero d (fonome),
#  - il nome di un file json (fout);
# costruisce il dizionario che ha come chiavi i livelli del dizionario-albero d.
# L'attributo di una chiave di valore x è la lista degli identificativi dei
# nodi che si trovano a livello x nell'albero rappresentato da d. La lista è
# ordinata lessicograficamente ed in modo crescente. Il dizionario così
# costruito va registrato nel file fout.
#
# Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione
# di dizionario_livelli(fname, fout) il file fout conterrà il dizionario:
# {0: ['a'], 1: ['b'], 2: ['c', 'd'], 3: ['e','i','l'], 4: ['f', 'g', 'h']}
#
# 4) la funzione dizionario_gradi_antenati(fnome, y, fout) che, presi:
#  - il nome di un file json contenente un dizionario-albero d (fonome),
#  - un intero y,
#  - il nome di un file json (fout);
# costuisce il dizionario che ha come chiavi gli identificativi dei nodi
# dell'albero rappresentato dal dizionario-albero d. L'attributo di una chiave
# di valore x è il numero di antenati di grado y che ha il nodo con
# identificativo x nell'albero. Registra il dizionario costruito nel file fout.
#
# Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione
# di dizionario_gradi_antenati(fnome, 2, fout) il file fout conterrà il
# dizionario:
# {'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1,
#  'l': 2}
#
# AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
# importare moduli che non sono nella libreria standard.
#
# Esercizio svolto da Emanuele Petriglia.

from json import dump, load

def gen_dict_from(element, src_dict, dst_dict):
    '''Genera il dizionario 'dst_dict' con l'elemento 'element' come radice,
    usando 'src_dict' come dizionario dove prendere i dati.
    '''
    dst_dict[element] = src_dict[element]

    for children in dst_dict[element]:
        gen_dict_from(children, src_dict, dst_dict)

def genera_sottoalbero(fnome, x, fout):
    sub_tree = {}

    data = load(open(fnome))

    if x in data: # Non è garantito che l'elemento esista.
        gen_dict_from(x, data, sub_tree)

    dump(sub_tree, open(fout, "w"))

# ------------------------------------------------------------------------------

def remove_element(element, data):
    '''Rimuove l'elemento 'element' dal dizionario 'data' rimuovendo anche
    eventuali figli.
    '''
    if not element in data:
        return

    # Prima si "uccidono" i figli ...
    set(map(lambda children: remove_element(children, data), data[element]))

    del data[element] # ... poi il padre.

def remove_father(father, data, this):
    '''Rimuove l'elemento 'this' dalla lista dei figli di 'father' se 'this' è
    presente.
    '''
    if this in data[father]:
        data[father].remove(this)

def cancella_sottoalbero(filename, x, fout):
    data = load(open(filename))

    remove_element(x, data)

    # Bisogna eliminare 'x' anche dalla lista dei figli di suo padre.
    set(map(lambda element: remove_father(element, data, x), data))

    dump(data, open(fout, "w"))

# ------------------------------------------------------------------------------

def remove_duplicates(element, data, elements_counter):
    '''Rimuove da 'elements_counter' gli elementi presenti nella lista di
    'element' nel dizionario 'data'.
    '''
    for sub_element in data[element]:
        elements_counter.discard(sub_element)

def get_root(data):
    '''Restituisce la radice dell'albero del dizionario 'data'.'''
    # Crea il nuovo insieme aggiungendo tutte le chiavi.
    counter = set(map(lambda element: element, data))

    # Toglie dall'insieme le chiavi ripetute nelle liste, facendo rimanere solo
    # la radice (che non è in nessuna lista).
    set(map(lambda element: remove_duplicates(element, data, counter), data))

    return counter.pop()

def get_levels_from(element, src_data, dst_data, level = 0):
    '''Crea un dizionario non ordinato con chiave il livello e attributo tutti i
    nodi a quel livello. I dati vengono presi da 'src_data' e scritti su
    'dst_data'.
    '''

    dst_data.setdefault(level, [])

    dst_data[level].append(element)

    level += 1
    set(map(lambda children: get_levels_from(children, src_data, dst_data,
                                             level),
            src_data[element]))

def dizionario_livelli(fnome, fout):
    data = load(open(fnome))

    root = get_root(data)

    levels = {}

    get_levels_from(root, data, levels)

    for element in levels: # Ogni lista viene ordinata.
        levels[element].sort()

    dump(levels, open(fout, "w"))

# ------------------------------------------------------------------------------

def get_forefather_grade(key, src_data, dst_data, grade, forefather_grade = 0):
    '''Ad ogni elemento di 'src_data' viene associato il valore numerico del
    grado dei suoi antenati (vedere l'enunciato dell'esercizio).
    '''
    dst_data[key] = forefather_grade

    elements = src_data[key]

    # Il valore booleano è considerato come numerico (False -> 0, True -> 1).
    forefather_grade += len(elements) == grade

    for element in elements:
        get_forefather_grade(element, src_data, dst_data, grade,
                             forefather_grade)

def dizionario_gradi_antenati(fnome, y, fout):
    data = load(open(fnome))

    root = get_root(data)

    new_dict = {}

    get_forefather_grade(root, data, new_dict, y)

    dump(new_dict, open(fout, "w"))
