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
def genera_ricorsione(diz, chiave):
    copy_diz = {}
    if chiave in diz:
        copy_diz[chiave] = diz[chiave]
        for el in diz[chiave]:
            copy_diz.update(genera_ricorsione(diz, el))
    return copy_diz
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    d = json.loads(open(fnome).read())
    
    diz_copy = genera_ricorsione(d, x)
    
    f = open(fout, 'w')
    json.dump(diz_copy, f)

def cancella_ricorsione(diz, chiave):
    if chiave in diz:
        for el in diz[chiave]:
            cancella_ricorsione(diz, el)
        diz.pop(chiave, None)
    return diz
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    d = json.loads(open(fnome).read())
    cancella_ricorsione(d, x)
    
    for i in d.values():
        if x in i:
            i.remove(x)
    
    f = open(fout, 'w')
    json.dump(d, f)

def livelli_ricorsione(diz, chiave, diz_liv, liv = 0):
    if liv not in diz_liv:
        diz_liv[liv] = [chiave]
    else:
        diz_liv[liv] += [chiave]
    for el in diz[chiave]:
        livelli_ricorsione(diz, el, diz_liv, liv+1)
    return diz_liv
def create_insi(d):
    insi = set()
    for key in d:
        for x in d[key]:
            insi.add(x)
    return insi
def find_radice(d):
    insi = create_insi(d)
    for key in d:
        if key not in insi:
            radice = key
    return radice
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    d = json.loads(open(fnome).read())
    
    diz_liv = {}
    diz_liv.clear()
    
    radice = find_radice(d)
    
    diz_liv = livelli_ricorsione(d, radice, diz_liv)
    
    for el in diz_liv:
        diz_liv[el] = sorted(diz_liv[el])
    
    f = open(fout, 'w')
    json.dump(diz_liv, f)

def antenati_ricorsione(chiave, d, diz_antenati):
    for el in d[chiave]:
        diz_antenati[el] += 1
        antenati_ricorsione(el, d, diz_antenati)
    return diz_antenati
def inizialize_antenati(d):
    return {x : 0 for x in d}
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    d = json.loads(open(fnome).read())
    
    diz_antenati = inizialize_antenati(d)
    for el in d:
        if len(d[el]) == y:
            diz_antenati = antenati_ricorsione(el, d, diz_antenati)
    
    f = open(fout, 'w')
    json.dump(diz_antenati, f)