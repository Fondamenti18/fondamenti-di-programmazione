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

from json import load, dump

def genera_sottoalbero(fnome, x, fout):
    dOut = {}
    with open(fnome) as infile:
        dIn = load(infile)
        with open(fout, 'w') as outfile:
            if x not in dIn:
                dump({}, outfile)
            else:
                dump(gen_subtree(dIn, x, dOut), outfile)

def gen_subtree(dIn, x, dOut):
    dOut[x] = dIn[x]
    for element in dIn[x]:
        gen_subtree(dIn, element, dOut)
    return dOut    

#--------------------------------------------------------

def cancella_sottoalbero(fnome, x, fout):
    dOut = {}
    with open(fnome) as infile:
        dIn = load(infile)
        with open(fout, 'w') as outfile:
            if x not in dIn:
                dump(dIn, outfile)
            else:
                dOut = dIn
                dOut = del_subtree(dIn, x, dOut)
                dOut = del_remaining(x, dOut)
                dump(dOut, outfile)
                
def del_subtree(dIn, x, dOut):
    for element in dIn[x]:
        del_subtree(dIn, element, dOut)
    del dOut[x]
    return dOut

def del_remaining(x, dOut):
    liste = [l for l in dOut.values()]
    for i in range(len(liste)):
        if x in liste[i]:
            liste[i].remove(x)
    return dOut

#--------------------------------------------------------

def dizionario_livelli(fnome, fout):
    dOut = {}
    with open(fnome) as infile:
        dIn = load(infile)
        with open(fout, 'w') as outfile:
            level_key(find_root(dIn), dIn, 0, dOut)
            for key in dOut:
                dOut[key] = sorted(dOut[key])
            dump(dOut, outfile)
            
def find_root(dIn):
    liste = [l for l in dIn.values()]
    for root in dIn:
        for i in range(len(liste)):
            if root not in liste[i]:
                return root

def level_key(root, dIn, level, dOut):
    if not dOut.get(level):
        dOut[level] = []
    dOut[level] += [root]
    for key in dIn[root]:
        level_key(key, dIn, level+1, dOut)
        
#--------------------------------------------------------

def dizionario_gradi_antenati(fnome, y, fout):
    dOut = {}
    with open(fnome) as infile:
        dIn = load(infile)
        with open(fout, 'w') as outfile:
            gradi(find_root(dIn), dIn, y, 0, dOut)
            dump(dOut, outfile)
            
def gradi(root, dIn, y, num_ant, dOut):
    dOut[root] = num_ant
    if len(dIn[root]) == y:
        num_ant += 1
    for key in dIn[root]:
        gradi(key, dIn, y, num_ant, dOut)
        








    
