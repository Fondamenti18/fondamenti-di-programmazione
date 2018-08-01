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

def root(diz):
    valori = []
    for x in diz.values():
        valori += x
    valori = set(valori)
    for x in diz.keys():
        if x not in valori:
            return x

def Bob(diz, x, subtree):
    if x not in diz:
        return {}
    else:
        subtree[x] = diz[x]
        for y in subtree[x]:
            Bob(diz,y,subtree)
    return subtree

def genera_sottoalbero(fnome,x,fout):
    sottoalbero = {}
    file = open(fnome).read()
    torta = json.loads(file)
    ris = Bob(torta,x,sottoalbero)
    with open(fout,'w') as outfile:    
        json.dump(ris, outfile)
    

def cancella_sottoalbero(fnome,x,fout):
    sottoalbero = {}
    file = open(fnome).read()
    torta = json.loads(file)
    tucano = Bob(torta,x,sottoalbero)
    
    for k in tucano:
        torta.pop(k)

    for k in torta:
        for n in torta[k]:
            if n == x:
                torta[k].remove(n)
    with open(fout,'w') as outfile:    
        json.dump(torta, outfile)

def livello(diz,x,level,tree):
    if str(level) not in tree:
        tree[str(level)] = [x]
    else:
        tree[str(level)] = sorted(tree[str(level)] + [x])
    figli = diz[x]
    for x in figli:
        tree = livello(diz,x,level+1,tree)
    return tree

def dizionario_livelli(fnome,fout):
    albero_livelli = {}
    file = open(fnome).read()
    torta = json.loads(file)
    radice = root(torta)
    albero_livelli = livello(torta,radice,0,albero_livelli)
    
    with open(fout,'w') as outfile:
        json.dump(albero_livelli,outfile)
    
 
def antenati_k_grado(diz,diz_ant,x,padre,k):   
    if len(diz[padre]) == k:
        diz_ant[x] = diz_ant[padre]+1
    else:
        diz_ant[x] = diz_ant[padre]
    for y in diz[x]:
        diz_ant = antenati_k_grado(diz,diz_ant,y,x,k)
    return diz_ant

def dizionario_gradi_antenati(fnome,y,fout):
    file = open(fnome).read()
    torta = json.loads(file)
    radice = root(torta)
    diz_gradi_antenati = {}
    diz_gradi_antenati[radice] = 0
    figli = torta[radice]
    for x in figli:
        diz_gradi_antenati = antenati_k_grado(torta,diz_gradi_antenati,x,radice,y)
        
    with open(fout,'w') as outfile:
        json.dump(diz_gradi_antenati,outfile)