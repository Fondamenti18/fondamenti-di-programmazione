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


def gen_subtree(diz_inizio, id_ricerca, diz_fine):
    if id_ricerca in diz_inizio:
        diz_fine[id_ricerca] = diz_inizio[id_ricerca]
        lista = diz_fine[id_ricerca]
        for conta in range(len(lista)):
            gen_subtree(diz_inizio, lista[conta], diz_fine)
    else:
        diz_fine[id_ricerca] = []
    return

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as json_data:
        d = json.load(json_data)
        diz_risultato = dict()
        gen_subtree(d, x, diz_risultato)
        with open(fout, 'w') as outfile:
            json.dump(diz_risultato, outfile)

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as json_data:
        d = json.load(json_data)
        diz_risultato = dict()
        gen_subtree(d, x, diz_risultato)
        for y in diz_risultato.keys():
            del d[y]
        for y in d.keys():
            if x in d[y]:
                c = 0
                while c < len(d[y]):
                    if d[y][c] == x:
                        del d[y][c]
                    c+=1
        with open(fout, 'w') as outfile:
            json.dump(d, outfile)

def inizio_albero(dizionario):
    key = list(dizionario.keys())
    values = []
    for y in dizionario:
        for x in dizionario[y]:
            values.append(x)
    values = set(values)
    for x in key:
        if x not in values: 
            return x
            
def conta(diz_inizio, id_ricerca, diz_fine, contatore = 0):
    lista = diz_inizio[id_ricerca]
    if str(contatore) not in list(diz_fine.keys()):
        diz_fine[str(contatore)] = []
    for x in range(len(lista)):
            conta(diz_inizio, lista[x], diz_fine, contatore + 1)
    diz_fine[str(contatore)].append(id_ricerca)
    return

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as json_data:
        d = json.load(json_data)
        diz_risultato = dict()
        inizio = inizio_albero(d)
        conta(d, inizio, diz_risultato)
        for x in diz_risultato:
            diz_risultato[x].sort()
        with open(fout, 'w') as outfile:
            json.dump(diz_risultato, outfile)

def funzione(diz_inizio, x, grado, diz_fine, lista = []):
    diz_fine[x] = len(lista)
    if len(diz_inizio[x]) == grado: lista +=[x]
    for z in diz_inizio[x]:
        funzione(diz_inizio, z, grado, diz_fine, lista)
    if x in lista: del lista[lista.index(x)]

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as json_data:
        d = json.load(json_data)
        inizio = inizio_albero(d)
        diz_risultato = dict()
        funzione(d, inizio, y, diz_risultato)
        with open(fout, 'w') as outfile:
            json.dump(diz_risultato, outfile)