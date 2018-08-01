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

def cercafigli(albero,x,ris):
    for y in range(0,len(x)):
        if x[y] != '':
            figli = albero[x[y]]
            ris = cercafigli(albero,figli,ris)
        ris[x[y]] = albero[x[y]]
    return ris

def genera_sottoalbero(fnome,x,fout):
    ris = {}
    with open(fnome) as f:
        dati = json.load(f)
    if x != '':
        figli = dati[x]
        ris = cercafigli(dati,figli,ris)
        ris[x] = figli
    with open(fout,'w') as f:
        json.dump(ris,f)
        
def cancellalbero(dati,x):
    y = 0
    while y <= len(x)-1:
        if x[y] != '':
            figli = dati[x[y]]
            dati = cancellalbero(dati,figli)
        dati.pop(x[y],'')
        y += 1
    return dati

def cancellaradice(dati,x):
    for i in dati:
        if x in dati[i]:
            dati[i].remove(x)
            return dati

def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as f:
        dati = json.load(f)
    if x != '':
        figli = dati[x]
        dati = cancellalbero(dati,figli)
    dati.pop(x,'')
    cancellaradice(dati,x)
    with open(fout,'w') as f:
        json.dump(dati,f)

def trovarad(dati):
    valori = []
    for a in dati.values():
        valori += a
    valori = set(valori)
    chiavi = dati.keys()
    if len(chiavi) >20000:
        chiavi = set(chiavi)
    for x in chiavi:
        if x not in valori:
           return x
            
def trovaliv(ris,dati,x,liv):
    if str(liv) not in ris:
        ris[str(liv)] = sorted(x)
    else:
        ris[str(liv)] += x
        ris[str(liv)] = sorted(ris[str(liv)])
    liv +=1
    for padre in x:
        figli = dati[padre]
        if figli != []:
            ris = trovaliv(ris,dati,figli,liv)
    return ris         

def dizionario_livelli(fnome,fout):
    with open(fnome) as f:
        dati = json.load(f)
    ris = {}
    x = trovarad(dati)
    ris = trovaliv(ris,dati,[x],0)
    with open(fout,'w') as f:
        json.dump(ris,f)

def grado_antenati(dati,padre,ris,y,nodi):
    nodi[padre] = antenati_grado_n(y,ris[padre])
    figli = dati[padre]
    for x in figli:
        if padre in ris:
            ris[x] = ris[padre]+[len(figli)]
        else:
            ris[x] = [len(figli)]
        ris = grado_antenati(dati,x,ris,y,nodi)[0]
    return ris,nodi
        
def antenati_grado_n(y,nodo):
    i = 0
    for n in nodo:
        if n == y:
            i +=1
    return i

def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as f:
        dati = json.load(f)
    ris = {}
    nodi = {}
    risultato = {}
    x = trovarad(dati)
    ris[x] = [0]
    ris,nodi = grado_antenati(dati,x,ris,y,nodi)
    keys = sorted(nodi.keys())
    for x in keys:
        risultato[x] = nodi[x]
    with open(fout,'w') as f:
        json.dump(risultato,f)

