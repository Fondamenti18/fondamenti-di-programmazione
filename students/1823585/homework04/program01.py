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

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, encoding='utf8') as f: d=json.load(f)
    e = genera_sottoalbero_ricorsivo(d,x)
    with open(fout, 'w', encoding='utf8') as f: json.dump(e, f)

def genera_sottoalbero_ricorsivo(s,n,t=None):
    if t is None:
        t = {}
    if n not in s:
        return t
    t[n] = s[n]
    for child in t[n]:
        genera_sottoalbero_ricorsivo(s,child,t)
    return t


def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, encoding='utf8') as f: d=json.load(f)
    e = genera_sottoalbero_ricorsivo(d,x)
    for node in e:
        d.pop(node,None)
    for node in d:
        for g in e:
            if g in d[node]:
                d[node].remove(g)
    with open(fout, 'w', encoding='utf8') as f: json.dump(d, f) 
    

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, encoding='utf8') as f: d=json.load(f)
    nodes = trova_radice(d)
    e = dizionario_livelli_ricorsivo(d,nodes)
    with open(fout, 'w', encoding='utf8') as f: json.dump(e, f)


def trova_radice(d):
    nodes = list(d.keys())
    for k in d:
        for c in d[k]:
            if c in nodes:
                nodes.remove(c)
    return nodes


def dizionario_livelli_ricorsivo(s,ns,t=None,a=0):
    if t is None:
        t = {}
    if not ns:
        return t
    f = []
    for n in ns:
        f.extend(s.get(n,[]))
        if a not in t:
            t[a] = []
        t[a].append(n)
    f.sort()
    u = dizionario_livelli_ricorsivo(s,f,t,a+1)
    t.update(u)
    return t


def dizionario_gradi_antenati(fnome,y,fout):
    '''
    - il nome di un file json contenente un dizionario-albero  d (fonome)
    - un intero y
    - il nome di un file json (fout)

    costuisce il dizionario che ha come chiavi gli identificativi dei nodi 
    dell'albero rappresentato dal dizionario-albero d, Attributo di una chiave 
    di valore x e' il numero di antenati di grado y che ha il nodo con 
    identificativo x nell'albero. Registra il dizionario costruito nel file fout.

    Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione 
    di dizionario_gradi_antenati(fnome,2,fout) il file fout conterra' il dizionario
    {'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}
    '''
    with open(fnome, encoding='utf8') as f: d=json.load(f)
    nodes = trova_radice(d)
    e = dizionario_gradi_antenati_ricorsivo(d,y,nodes[0])
    with open(fout, 'w', encoding='utf8') as f: json.dump(e, f)

def dizionario_gradi_antenati_ricorsivo(d, y, nodo, antenati=None):
    if antenati is None:
        antenati = {}
    antenati_di_grado_y = len( [x for x in antenati if antenati[x] == y] )
    #print(f"nodo: {nodo}, antenati: {antenati}")
    d_gradi_antenati_finale = { nodo: antenati_di_grado_y }
    #print(f"nodo: {nodo}, antenati: {antenati}")
    figli = d.get(nodo)
    #print(f"nodo: {nodo}, antenati: {antenati}, d_gradi_antenati_finale: {d_gradi_antenati_finale}")
    if not figli:   # caso base
        #print(f"nodo: {nodo}, antenati: {antenati}, d_gradi_antenati_finale: {d_gradi_antenati_finale}")
        return d_gradi_antenati_finale
    antenati[nodo] = len(figli)
    for figlo in figli:
        d_gradi_antenati = dizionario_gradi_antenati_ricorsivo(d, y, figlo, antenati)
        d_gradi_antenati_finale.update(d_gradi_antenati)
    return d_gradi_antenati_finale
	
if __name__ == '__main__':
    #print(genera_sottoalbero('Alb10.json','d','tAlb10_1.json'))
    #print(cancella_sottoalbero('Alb10.json','d','tAlb10_2.json'))
    #print(dizionario_livelli('Alb100.json', 'tAlb100_3.json'))
    pass