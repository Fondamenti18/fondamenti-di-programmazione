import json
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
'''

def naviga_albero(orig, k, ris):
    ris[k] = orig[k][:]
    for c in ris[k]:
        naviga_albero(orig, c, ris)



def genera_sottoalbero(fnome, x, fout):
    with open(fnome, mode='r', encoding='utf-8') as fin:
        albero_in = json.load(fin)
    ris = {}
    if x in albero_in.keys():
        naviga_albero(albero_in, x, ris)
    with open(fout, mode='w', encoding='utf-8') as fo:
        json.dump(ris, fo)


'''
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

'''

def elimina(orig, k):
    for c in orig[k]:
        elimina(orig, c)
    del orig[k]


def cancella_sottoalbero(fnome, x, fout):
    with open(fnome, mode='r', encoding='utf-8') as fin:
        albero_in = json.load(fin)
    if x in albero_in.keys():
        elimina(albero_in, x)
        for k in albero_in.keys():
            if x in albero_in[k]:
                albero_in[k].remove(x)
    with open(fout, mode='w', encoding='utf-8') as fo:
        json.dump(albero_in, fo)

'''

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

'''

def trova_radice(orig):
    radice = None
    d = {}
    for k in orig.values():
        for n in k:
            d[n] = 0

    for k in orig.keys():
        try:
            a = d[k]
        except KeyError:
            radice = k
            break
    return radice


def livelli(albero_in, ris, radice, livello):
    try:
        m = ris[livello]
    except KeyError:
        ris[livello] = []

    ris[livello].append(radice)

    for f in albero_in[radice]:
        livelli(albero_in, ris, f, livello + 1)



def dizionario_livelli(fnome,fout):
    with open(fnome, mode='r', encoding='utf-8') as fin:
        albero_in = json.load(fin)
    radice = trova_radice(albero_in)
    ris = {}
    livello = 0
    if radice != None:
        livelli(albero_in, ris, radice, livello)
    for k in ris.keys():
        ris[k].sort()
    with open(fout, mode='w', encoding='utf-8') as fo:
        json.dump(ris, fo)


'''
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

def scandaglio(albero_in, ris, padre, ant, y):
    ris[padre] = ant
    if len(albero_in[padre]) == y:
        ant += 1
    for f in albero_in[padre]:
        scandaglio(albero_in, ris, f, ant, y)



def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome, mode='r', encoding='utf-8') as fin:
        albero_in = json.load(fin)
    radice = trova_radice(albero_in)
    ris = {}
    scandaglio(albero_in, ris, radice, 0, y)
    with open(fout, mode='w', encoding='utf-8') as fo:
        json.dump(ris, fo)
