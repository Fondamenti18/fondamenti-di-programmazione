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

costruisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero 
rappresentato dal dizionario-albero d, attributo di una chiave di valore x e' il numero 
di antenati di grado y che ha il nodo con identificativo x nell'albero.
Registra il dizionario costruito nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_gradi_antenati(fnome,2,fout)
il file fout conterra' il dizionario 

                             'a'
                              |
                _____________'b'____________             
               |                            |            
              'c'                  ________'d'_______   
               |                  |                  |  
              'i'         _______'e'_______         'l'
                         |        |        |               
                        'f'      'g'      'h'

{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.
'''

import json

def first(filename):
    with open(filename, mode="r") as file:
        data = json.load(file)   
    return data

def find_root(diz):
    for el in diz.keys():
        if el not in diz.values():
            return el

def find_all_occurrences_recursive(data, x, diz):
    to_find = data.get(x)
    my_set = set(to_find)
    diz[x] = to_find
    for el in my_set:
        find_all_occurrences_recursive(data, el, diz)
    return diz

def genera_sottoalbero(fnome,x,fout):
    data = first(fnome)
    diz = {}
    data_to_write = find_all_occurrences_recursive(data, x, diz)
    with open(fout, 'w') as out:
        json.dump(data_to_write, out)
     

def remove_x(file, x):
    # elimino la chiave che sto cercando dalle liste valori del dizionario.
    data = first(file)
    for keys in data.keys():
        if x in data.get(keys):
            data.get(keys).remove(x)
    return data

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    # uso la funzione iniziale, find_all_occurrences
    general_data = remove_x(fnome, x) # carico il dizionario iniziale
    diz = {}
    to_delete = find_all_occurrences_recursive(general_data, x, diz) # le chiavi da eliminare sono qui!!
    for keys in to_delete.keys():
        general_data.pop(keys, None) # eliminiamo le chiavi inutili.
    with open(fout, 'w') as out: # et voila'
        json.dump(general_data, out)
    
def get_son(diz, element):
    return diz.get(element)

def calculate_level(data, diz, count, element = None):
    my_list = []
    if element is None:
        count = count + 1
        root = list(data.keys())[0]
        diz[count] = [root] # aggiungiamo la radice che sarà 0.
        my_list = get_son(data, root) # voglio iterare sulla lista, così aggiungo la lista di elementi collegati alla radice.
    else:
        count = count + 1
        if diz.get(count):
            diz[count] += [element]
        else:
            diz[count] = [element]
        my_list = get_son(data, element)
    diz[count] = sorted(diz.get(count))
    for el in my_list:
        calculate_level(data, diz, count, el)
    return diz

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    diz = {}
    count = -1
    data = first(fnome)
    data = calculate_level(data, diz, count)
    with open(fout, 'w') as out:
        json.dump(data, out)
    
'''

4)
la funzione dizionario_gradi_antenati(fnome,y,fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- un intero y
- il nome di un file json (fout)

costruisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero 
rappresentato dal dizionario-albero d, attributo di una chiave di valore x e' il numero 
di antenati di grado y che ha il nodo con identificativo x nell'albero.
Registra il dizionario costruito nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_gradi_antenati(fnome,2,fout)
il file fout conterra' il dizionario 

                             'a'
                              |
                _____________'b'____________             
               |                            |            
              'c'                  ________'d'_______   
               |                  |                  |  
              'i'         _______'e'_______         'l'
                         |        |        |               
                        'f'      'g'      'h'

{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}

'''

def fourth(data, levels):
    diz = {}
    root = ''.join(levels[0])
    for l, k in enumerate(data.keys()):
        print(l, k)
        if k == root:
            diz[k] = 0
        else:
            diz[k] = 1
    return diz

def find_dependences(data, element, my_list):
    if element == list(data.keys())[0]:
        return my_list
    for el in data.keys():
        if element in data.get(el):
            my_list.append(el)
            find_dependences(data, el, my_list)
            continue
            
def test(data, diz, y):
    for k in data.keys():
        my_list = []
        count = 0
        find_dependences(data, k, my_list)
        for el in my_list:
            if len(data.get(el)) == y:
                count += 1
        diz[k] = count
    return diz

      
def dizionario_gradi_antenati(fnome,y,fout):
    f = first(fnome)
    d = test(f, {}, y)
    with open(fout, 'w') as out:
        json.dump(d, out)
    
