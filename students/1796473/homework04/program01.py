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

def radice_albero(albero):
    for key in albero.keys():
        for value in albero.values():
            if key in value:
                break
        return key


def componi(albero, nodo=None): #da {"a":["b","c"],"b":["d"],"c":[],"d":[]} a {"a":{"b":{"d":{}},"c":{}}}
    if nodo == None:
        nodo = radice_albero(albero)
        return {nodo: componi(albero, nodo)}
    
    figli = {}
    for figlio in albero[nodo]:
        figli[figlio] = componi(albero, figlio)
    return figli


def scomponi(albero, nodo=None): #da {"a":{"b":{"d":{}},"c":{}}} a {"a":["b","c"],"b":["d"],"c":[],"d":[]}
    if nodo == None:
        nodo = list(albero.keys())[0] # il primo strato ha solo una chiave
    nodi = {}
    figli = list(albero[nodo].keys())
    nodi[nodo] = figli
    for figlio in figli:
        nodi.update(scomponi(albero[nodo], figlio))
    return nodi


def genera_sottoalbero_impl(albero,x):
    if x in albero:
        return {x: albero[x]}
    for nodo in albero:
        ris = genera_sottoalbero_impl(albero[nodo], x)
        if ris != None:
            return ris


def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, 'r') as din:
        albero = scomponi(genera_sottoalbero_impl(componi(json.load(din)), x))
    with open(fout, 'w') as dout:
        json.dump(albero, dout)
    

def cancella_sottoalbero_impl(albero,x):
    if x in albero:
        del albero[x]
        return albero
    for nodo in albero:
        cancella_sottoalbero_impl(albero[nodo], x)
    return albero


def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, 'r') as din:
        albero = scomponi(cancella_sottoalbero_impl(componi(json.load(din)), x))
    with open(fout, 'w') as dout:
        json.dump(albero, dout)


def fondi(d1, d2):
    for key in d1:
        if key in d2:
            d1[key] += d2[key]
            d1[key].sort()
    d2.update(d1)
    return d2


def dizionario_livelli_impl(albero, livello=0):
    livelli = {livello: list(albero.keys())}
    for key in albero:
        if albero[key] != {}:
            livelli = fondi(livelli, dizionario_livelli_impl(albero[key], livello+1))
    return livelli


def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, 'r') as din:
        livelli = dizionario_livelli_impl(componi(json.load(din)))
    with open(fout, 'w') as dout:
        json.dump(livelli, dout)


def dizionario_gradi_antenati_impl(albero,y,diz,nodo=None,count=0):
    if nodo == None:
        nodo = radice_albero(albero)
    diz.update({nodo: count})

    for figlio in albero[nodo]:
        dizionario_gradi_antenati_impl(albero, y, diz, figlio, count+1 if len(albero[nodo]) == y else count)
        
    return diz


def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    with open(fnome, 'r') as din:
        gradi = dizionario_gradi_antenati_impl(json.load(din),y,{})
    with open(fout, 'w') as dout:
        json.dump(gradi, dout)

