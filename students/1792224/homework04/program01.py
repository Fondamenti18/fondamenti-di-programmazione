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

def genera_sottoalbero(fnome,x,fout):
    global diz1, diz2
    diz2 = {}
    with open(fnome) as f:
        diz1 = json.load(f)
    ramo(x)
    with open(fout, 'w') as f:
        json.dump(diz2, f)
    return


def ramo(c):
    diz2[c] = diz1[c]
    ls = diz2[c]
    nls = len(ls)
    if nls == 0:
        return
    else:
        for i1 in range(nls):
            ramo(diz2[c][i1])
    return


def cancella_sottoalbero(fnome,x,fout):
    global diz1, diz2
    with open(fnome) as f:
        diz1 = json.load(f)
    diz2 = diz1.copy()
    ramodel(x)
    ls = list(diz2.keys())
    ni1 = len(ls)
    for i1 in range(ni1):
        ni2 = len(diz2[ls[i1]])
        for i2 in range(ni2):
            if not diz2[ls[i1]][i2] in ls:
                diz2[ls[i1]].remove(diz2[ls[i1]][i2])
                break
    with open(fout, 'w') as f:
        json.dump(diz2, f)
    return

def ramodel(c):
    diz2.pop(c)
    ls = diz1[c]
    nls = len(ls)
    if nls == 0:
        return
    else:
        for i1 in range(nls):
            ramodel(diz1[c][i1])
    return


def dizionario_livelli(fnome,fout):
    with open(fnome) as f:
        diz1 = json.load(f)
    l1 = list(diz1.keys())
    nl1 = len(l1)
    diz1[l1[0]] = diz1[l1[0]], 0
    for i1 in range(nl1):
        l2 = diz1[l1[i1]][0]
        nl2 = len(l2)
        if nl2 > 0:
            for i2 in range(nl2):
                diz1[l2[i2]] = diz1[l2[i2]], diz1[l1[i1]][1] + 1
    diz2 = {}
    for i1 in range(nl1):
        if diz1[l1[i1]][1] in diz2:
            diz2[diz1[l1[i1]][1]].append(l1[i1])
        else:
            diz2[diz1[l1[i1]][1]] = [l1[i1]]
    for i1 in diz2.keys():
        diz2[i1] = sorted(diz2[i1])
    with open(fout, 'w') as f:
        json.dump(diz2, f)
    return


def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as f:
        diz1 = json.load(f)
    global l1, dizg
    l1 = list(diz1.keys())
    nl1 = len(l1)
    dizg = {}
    for i1 in range(nl1):
        dizg[l1[i1]] = "", 0
    for i1 in range(nl1):
        nfigli = len(diz1[l1[i1]])
        for i2 in range(nfigli):
            dizg[diz1[l1[i1]][i2]] = l1[i1], nfigli
    dizr = {}
    for i1 in range(nl1):
        nris = 0
        nris = ricerca_ant(l1[i1], y, 0)
        dizr[l1[i1]] = nris
    with open(fout, 'w') as f:
        json.dump(dizr, f)
    return

def ricerca_ant(c, nfy, nris):
    if dizg[c][1] == nfy:
        nris += 1
    if  dizg[c][1] == 0:
        return nris
    else:
        nris = ricerca_ant(dizg[c][0], nfy, nris)
    return nris

