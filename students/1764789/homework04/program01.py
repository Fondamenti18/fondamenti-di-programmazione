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

- il nome di un file json contenente un dizionario-albero  d (fnome)
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
    din = {}
    dout = {}
    with open(fnome, 'r') as f:
        din = json.load(f)
        aggiungi_sottoalbero(din,x,dout)
    with open(fout, 'w') as f:
        json.dump(dout, f)

def cancella_sottoalbero(fnome,x,fout):
    din = {}
    dout = {}
    ddel = {}
    with open(fnome, 'r') as f:
        din = json.load(f)
        aggiungi_sottoalbero(din,x,ddel)
    with open(fnome, 'r') as f:
        din = json.load(f)
        escludi_sottoalbero(din,ddel,x,dout)
    with open(fout, 'w') as f:
        json.dump(dout, f)
    
def dizionario_livelli(fnome,fout):
    din = {}
    dout = {}
    with open(fnome, 'r') as f:
        din = json.load(f)
        aggiungi_livello(din,dout)
    for l in dout:
        dout[l].sort()
    with open(fout, 'w') as f:
        json.dump(dout, f)

def dizionario_gradi_antenati(fnome,y,fout):
    din = {}
    dout = {}
    with open(fnome, 'r') as f:
        din = json.load(f)
        costruisci_albero_gradi(din,y,dout)
    with open(fout, 'w') as f:
        json.dump(dout, f)
    
# ########################################################################
# UTILITY
# ########################################################################
def aggiungi_sottoalbero(din,x,dout):
    dout[x] = din[x]
    for y in dout[x]:
        aggiungi_sottoalbero(din,y,dout)
        
def escludi_sottoalbero(din,ddel,x,dout):
    for y in din:
        if (y not in ddel):
            dout[y] = din[y]
            if (x in dout[y]):
                dout[y].remove(x)
                
def aggiungi_livello(din,dout,x='',l=0):
    if l == 0:
        x = cerca_radice(din)
    if (l not in dout):
        dout[l] = []
    dout[l] += [x]
    for y in din[x]:
        aggiungi_livello(din,dout,y,l+1)
        
def cerca_radice(din,inizia_da=''):
    if inizia_da == '':
        inizia_da = list(din.keys())[0]
    trovato = ''
    for v in din:
        if inizia_da in din[v]:
            trovato = v
            break
    if trovato == '':
        return inizia_da
    else:
        return cerca_radice(din, trovato)
    
def costruisci_albero_gradi(din,y,dga,inizia_da='',numero_antenati=0):
    if inizia_da == '':
        inizia_da = cerca_radice(din)
    dga[inizia_da] = numero_antenati
    if len(din[inizia_da]) == y:
        numero_antenati += 1
    for v in din[inizia_da]:
        costruisci_albero_gradi(din,y,dga,v,numero_antenati)
