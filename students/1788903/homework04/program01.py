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

costruisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero 
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

class Nodo:
    
    def __init__(self, valore):
        self.valore = valore
        self.figli = []
#-----------------------------------------------------------------------------------------------
def ricorsione(t,x,d):
    if x not in t: return None
    else:
        sottoAlbero = Nodo(x)
        sottoAlbero.figli += t[x]
        d[sottoAlbero.valore] = sottoAlbero.figli
        for x in d[x]:
            ricorsione(t,x,d)
    return d
#-----------------------------------------------------------------------------------------------
def ricorsioneD(t,x,d):
    if x not in t: return t
    else:
        sottoAlbero = Nodo(x)
        sottoAlbero.figli += t[x]
        d[sottoAlbero.valore] = sottoAlbero.figli
        for x in d[x]:
            ricorsione(t,x,d)
    return d
#-----------------------------------------------------------------------------------------------
def ricorsioneL(dizionario,d,livello):
    if d == {}: return 
    for x in dizionario:
        nodo = Nodo(x)
        d[livello] = nodo.valore
        print(d)
        nodo.figli += [dizionario[x]]
        livello += 1
        return ricorri(dizionario,d,livello)
#-----------------------------------------------------------------------------------------------
# def livelli(lista,dizionario,livello,indice):
#     if indice > len(lista)-1: return dizionario
#     else:
#         dizionario[livello] = lista[indice]
#         return livelli(lista,dizionario,livello+1,indice+1)
def livelli(livello, diz, dizOriginale, lista):
    try:
        diz[livello] += lista
        livello += 1
    except KeyError:
        diz[livello] = lista
        livello += 1
    for x in lista:
        livelli(livello, diz, dizOriginale, dizOriginale[x])
#-----------------------------------------------------------------------------------------------
#def trova_gradi(dizionario,nuovoDizionario,radice,contatore = 0):
#    if dizionario[radice] == [] : return nuovoDizionario
#    for x in dizionario[radice]:
#        contatore += 1
#    nuovoDizionario[radice] = contatore
#    print(nuovoDizionario)
#    for x in radice:
#        return trova_gradi(dizionario,nuovoDizionario,x,contatore = 0)
# def trova_gradi(dizionario,nuovoDizionario,radice,contatore = 0):
#     nodo = Nodo(radice)
#     nodo.figli += dizionario[radice]
#     #if nodo.figli == [] : return nuovoDizionario
#     for x in nodo.figli:
#         contatore += 1
#     nuovoDizionario[nodo.valore] = contatore
#     for x in nodo.figli:
#         trova_gradi(dizionario,nuovoDizionario,x,contatore = 0)
# def gradi(dizionario,radice,d,numero,contatore):
#     d[radice] = contatore
#     for x in dizionario[radice]:
#         if len(dizionario[radice]) == numero:
#             contatore += 1
#             gradi(dizionario,x,d,numero,contatore)
#             contatore -= 1
#         else:
#             gradi(dizionario,x,d,numero,contatore)
#-----------------------------------------------------------------------------------------------
        
#-----------------------------------------------------------------------------------------------
import json
#-----------------------------------------------------------------------------------------------
def genera_sottoalbero(fnome,x,fout):

    with open(fnome, 'r') as f:
        t = json.load(f)

    d = {}
    
    ricorsione(t,x,d)
    
    with open(fout, 'w') as out:
        json.dump(d, out)
#-----------------------------------------------------------------------------------------------  
def cancella_sottoalbero(fnome,x,fout):
    
    with open(fnome,'r') as f:
        dizionario = json.load(f)

    d = {}
    ricorsioneD(dizionario,x,d)

    diz = {k:v for k,v in dizionario.items() if k not in d}

    for i in diz:
        for j in diz[i]:
            if x == j: 
                diz[i].remove(j)

    with open(fout, 'w') as out:
        json.dump(diz, out)
#-----------------------------------------------------------------------------------------------
def dizionario_livelli(fnome,fout):
    with open(fnome,'r') as f:
        dizionario = json.load(f)

    chiavi = [x for x in dizionario]
    valori = []
    for x in dizionario:
        for y in dizionario[x]:
            valori += [y]
    radice = [x for x in chiavi if x not in valori]

    d = {}
    livello = 0
    
    livelli(livello,d,dizionario,radice)
    dizFinale = {k:sorted(v) for k,v in d.items() if v != []}
    
    with open(fout,'w') as f:
        json.dump(dizFinale,f)
#-----------------------------------------------------------------------------------------------
def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome,'r') as f:
        dizionario = json.load(f)

    radice = 0
    for chiave in dizionario:
        for chiavep in dizionario:
            if chiave in dizionario[chiavep]:
                break
            radice = chiave
        if radice != 0:
            break
    d = {}
    contatore = 0

    gradi(dizionario,radice,d,y,contatore)
    
    with open(fout,'w') as f:
        json.dump(d,f)

def gradi(dizionario,radice,d,numero,contatore):
    d[radice] = contatore
    for x in dizionario[radice]:
        if len(dizionario[radice]) == numero:
            contatore += 1
            gradi(dizionario,x,d,numero,contatore)
            contatore -= 1
        else:
            gradi(dizionario,x,d,numero,contatore)
