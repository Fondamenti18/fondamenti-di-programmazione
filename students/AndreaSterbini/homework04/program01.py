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

#########################################################################

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, encoding='utf8') as f:
        albero = json.load(f)
        sottoalbero = estrai_sottoalbero(albero, x)
        with open(fout, mode='w', encoding='utf8') as fo:
            json.dump(sottoalbero, fo)

def estrai_sottoalbero(albero, x):
    sottoalbero = {}
    if x in albero:
        figli = albero[x]
        sottoalbero[x] = figli
        for y in figli:
            sottoalbero.update(estrai_sottoalbero(albero,y))
    return sottoalbero

#########################################################################

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, encoding='utf8') as f:
        albero = json.load(f)
        eliminati = elimina_sottoalbero(albero, x)
        elimina_sottoalbero_2(albero, eliminati)
        with open(fout, mode='w', encoding='utf8') as fo:
            json.dump(albero, fo)
   
def elimina_sottoalbero(albero, x):
    eliminati = {x}
    if x in albero:
        figli = albero[x]
        if figli:
            for y in figli:
                eliminati.update(elimina_sottoalbero(albero, y))
        del albero[x]
    return eliminati

def elimina_sottoalbero_2(albero, eliminati):
    for nodo, valori in albero.items():
        for x in eliminati:
            if x in valori:
                valori.remove(x)

#########################################################################

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, encoding='utf8') as f:
        albero = json.load(f)
        radice,_ = trova_radice(albero)
        livelli = {}
        estrai_livelli(albero, livelli, radice, 0)
        ordina_livelli(livelli)
        with open(fout, mode='w', encoding='utf8') as fo:
            json.dump(livelli, fo)

def trova_radice(albero):
    padri = {}
    for padre, figli in albero.items():
        for figlio in figli:
            padri[figlio] = padre
    for nodo in albero:
        if nodo not in padri:
            return nodo, padri

def estrai_livelli(albero, livelli, radice, livello=0):
    if not livello in livelli: 
        livelli[livello] = []
    livelli[livello].append(radice)
    figli = albero[radice]
    for figlio in figli:
        estrai_livelli(albero, livelli, figlio, livello+1)

def ordina_livelli(livelli):
    for l, nodi in livelli.items():
        nodi.sort()

#########################################################################

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, encoding='utf8') as f:
        albero = json.load(f)
        radice,padri = trova_radice(albero)
        dizio = {}
        gradi_antenati(padri, albero, radice, y, dizio)
        with open(fout, mode='w', encoding='utf8') as fo:
            json.dump(dizio, fo)

def gradi_antenati(padri, albero, radice, y, dizio):
    if radice not in padri:
        dizio[radice] = 0
    else:
        padre = padri[radice]
        fratelli = albero[padre]
        grado = len(fratelli)
        add1 = 1 if grado == y else 0
        dizio[radice] = dizio[padri[radice]] + add1
    for f in albero[radice]:
        gradi_antenati(padri, albero, f, y, dizio)

