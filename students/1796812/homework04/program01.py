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

def gen_lista(diz, x):
    lista = [(x, diz[x])]
    for i in diz[x]:
        lista += gen_lista(diz, i)
    return lista


def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        diz = json.load(f)
    new_diz = {}
    if x in diz.keys():
        lista = gen_lista(diz, x)
        for items in lista:
            new_diz[items[0]] = items[1]
    with open(fout, 'w') as ff:
        json.dump(new_diz, ff)
    

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        diz = json.load(f)
    if x in diz.keys():
        lista = gen_lista(diz, x)
        for items in lista:
            del diz[items[0]]
        for coppia in diz.items():
            if x in coppia[1]: diz[coppia[0]].remove(x)
    with open(fout, 'w') as ff:
        json.dump(diz, ff)
    

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        diz = json.load(f)
    lista = livello(diz, 0)
    new_diz = {}
    for liv in lista:
        new_diz[liv[0]] = sorted(liv[1:])
    with open(fout, 'w') as ff:
        json.dump(new_diz, ff)
 

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        diz = json.load(f)
    new_diz = {}
    for c in diz.keys():
        num = contatore(diz, c, y)
        new_diz[c] = num
    with open(fout, 'w') as ff:
        json.dump(new_diz, ff)


def contatore(d, c, y):
    counter = 0
    for c2 in d.keys():
        if c in d[c2]:
            if len(d[c2]) == y: counter += 1
            counter += contatore(d, c2, y)
    return counter


def livello(d, liv):
    if len(d) == 0: return []
    chiavi, valori = d.keys(), d.values()
    lista = [[liv]]
    x = 0
    for c in chiavi:
        for v in valori:
            if c in v: x += 1
        if x == 0: lista[0] += [c]
        else: x = 0
    for el in lista[0][1:]:
        del d[el]
    lista += livello(d, liv+1)
    return lista
