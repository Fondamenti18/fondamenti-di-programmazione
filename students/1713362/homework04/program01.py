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
    with open(fnome) as file:
        d = json.loads(file.read())
    d_out = {}                              # inizializzo un dizionario vuoto
    if not x in d.keys():                   # se x non è tra le chiavi di d
        return d_out                        # allora torna il dizionario vuoto
    l = d.get(x)                            # chiamo l la lista dei figli dell'elemento x
    d_out = subTree(d,x,l,{})               # chiamo la subtree che mi ritorna un dizionario
    with open(fout, 'w') as outfile:
        json.dump(d_out, outfile)           # salva
    return d_out                            # non sarebbe necessario ma richiamiamo questa funzione altrove e ci serve

def subTree(d,x,l,diz):
    dict = diz
    dict[x] = l                             # dict = aggiungi x come chiave e i suoi elementi come valore
    if d[x] == []:                          # prendo l'elemento x di d e controllo se la sua lista figli è vuota
        return dict                         # termino la chiamata
    for e in l:                             # per ogni elemento nella lista figli
        dict = subTree(d,e,d[e],dict)       # comincio la ricorsione che prende come argomenti il dizionario di partenza
                                            # l'elemento e, la lista figli dell'elemento, e il dizionario che mi creo
    return dict                             # ritorno dict

def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as file:
        d = json.loads(file.read())
    if not x in d.keys():                           # se x non è tra le chiavi del dizionario
        with open(fout, 'w') as outfile:            # allora deve scrivere il file senza modificarlo
            json.dump(d, outfile)
    dict_find = genera_sottoalbero(fnome,x,fout)    # altrimenti chiama genera_sottoalbero per avere il sottoalbero a partire da x
    for key in dict_find:                           # per ogni chiave nel sottoalbero
        if key in d.keys():                         # se la chiave è tra le chiavi di d
            del d[key]                              # allora elimina la chiave da d
            for k in d.keys():                      # per ogni k nelle chiavi di d
                if key in d[k]:                     # se la chiave è contenuta all'interno dei figli di k
                    d[k].remove(key)                # allora eliminala dalla lista
    with open(fout, 'w') as outfile:
        json.dump(d, outfile)                       # salva


def dizionario_livelli(fnome,fout):
    with open(fnome) as file:
        d = json.loads(file.read())
    txt = open(fnome).read()                    # leggi il file come testo, non come dizionario
    l = txt.split("\"")                         # splitta al carattere " ---> split ritorna una lista
    chiave = l[1]                                 # la radice è l'elemento all'indice 1 della lista
    root = findRoot(d,chiave)
    d_out = levelTree(d,root,d[root],{},0)      # richiama la leveltree a partire dalla radice root e dal livello 0
    for key in d_out.keys():
        list = d_out[key]                       # list è uguale alla lista attribuita alla chiave key [figli]
        d_out[key] = sorted(list)               # e poi li mette in ordine alfabetico
    with open(fout, 'w') as outfile:
        json.dump(d_out, outfile)               # salva

def findRoot(d,r):
    root = r
    oldkey = root
    while True:
        for key in d.keys():
            if root in d[key]:
                root = key
        if oldkey == root:
            return root
        else:
            oldkey = root

def levelTree(d,x,l,diz,n):
    dict = diz
    list = []
    list.append(x)                              # aggiungi alla lista vuota x e i suoi elementi
    if not n in dict.keys():                    # se n non è tra le chiavi di dict
        dict[n] = list                          # all'elemento n del dizionario assegna come valore list
    else:
        lista = dict[n]                         # metto l'attuale valore di dict[n] dentro una lista
        lista.append(x)                         # alla lista aggiungo x
        dict[n] = lista                         # e assegno a n nel dizionario la lista modificata
    m = n+1                                     # incremento il livello dell'albero
    if d[x] == []:
        return dict
    for e in l:
        dict = levelTree(d,e,d[e],dict,m)
    return dict


def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as file:
        d = json.loads(file.read())
    txt = open(fnome).read()
    l = txt.split("\"")
    root = l[1]
    root = findRoot(d,root)
    d_degree = degreeTree(d,root,d[root],y,{},{})           # ottengo un dizionario di vero falso per ogni chiave
    d_out = {}
    for key in d.keys():
        d_out[key] = 0                                      # inizializzo d_out con valore 0
    diz = finalDegreeTree(d,d_degree,d_out,root,0)          # chiamo la funzione che mi calcola il grado
    with open(fout, 'w') as outfile:
        json.dump(diz, outfile)                             # salvo

def finalDegreeTree(d,d_degree,d_out,root,n):
    diz = d_out
    l = d[root]
    diz[root] = n                                           # associa a dizionario in root n (intero)
    if d_degree[root]:                                      # se è True (l'elemento root è un nodo di grado y e ha y-figli)
        for e in l:                                         # per ogni elemento e in l
            diz = finalDegreeTree(d,d_degree,diz,e,n+1)     # in diz metto il risultato della chiamata finaldegreetree
    else:
        for e in l:
            diz = finalDegreeTree(d,d_degree,diz,e,n)
    return diz

def findPadre(d,f):
    for key in d.keys():    # per ogni chiave nel dizionario
        if f in d[key]:     # se f sta nella lista di figli della chiave
            return key      # allora la chiave è il padre



def degreeTree(d,x,l,y,diz,d_number):
    dict = diz
    dict[x] = l
    if d[x] == []:                                      # se la lista di figli è vuota
        d_number[x] = False                             # il nodo non è di grado y
        return dict                                     # termina la chiamata
    if len(l) == y:                                     # se il nodo ha y figli
        d_number[x] = True                              # allora torna true
    else:
        d_number[x] = False                             # altrimenti false
    for e in l:
        dict = degreeTree(d,e,d[e],y,dict,d_number)     # altrimenti richiama se stessa per tutti i figli di x
    return d_number