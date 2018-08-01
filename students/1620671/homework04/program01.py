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
    dout = dict()
    d = ricava_d(fnome)
    if x not in d:
        with open(fout, 'w') as of:
            json.dump({}, of, ensure_ascii = False)
    else:
        dout[x] = d[x]
        with open(fout, 'w') as of:
            json.dump(sottoalbero(d, x, dout), of, ensure_ascii = False)

def cancella_sottoalbero(fnome,x,fout):
    d = ricava_d(fnome)
    dout = dict()
    if x not in d:
        with open(fout, 'w') as of:
            json.dump(d, of, ensure_ascii = False)
    else:
        dout[x] = d[x]
        dout = sottoalbero(d,x,dout)
        dout2 = dict()
        for v in d:
            if v not in dout:
                dout2[v] = d[v]
                for i in dout2[v]:
                    if i in dout:
                        dout2[v].remove(i)
        with open(fout, 'w') as of:
            json.dump(dout2, of, ensure_ascii = False)

def dizionario_livelli(fnome,fout):
    d = ricava_d(fnome)
    d2 = modifica_d(d)
    dout = dict()
    for v in d:
        m = len(sopralbero(d2, v, {}))
        if d2[v][1] == 0:
            dout[0] = [v]
        elif m in dout:
            dout[m] += [v]
            dout[m] = sorted(dout[m])
        else:
            dout[m] = [v]
    with open(fout, 'w') as of:
        json.dump(dout, of, ensure_ascii = False)

def dizionario_gradi_antenati(fnome,y,fout):
    d = ricava_d(fnome)
    d2 = modifica_d(d)
    dout = dict()
    for v in d:
        count = 0
        for i in sopralbero(d2,v,{}):
            if d2[v][1] == 0:
                count = 0
            elif len(d[i]) == y:
                count += 1
        dout[v] = count
    with open(fout, 'w') as of:
        json.dump(dout, of, ensure_ascii = False)


def ricava_d(fnome):
    with open(fnome, encoding = 'utf-8') as f:
        t = f.read()
        d = json.loads(t)
    return d

def sottoalbero(d, x , dout):
    for v in d[x]:
        dout[v] = d[v]
        sottoalbero(d, v, dout)
    return dout

def modifica_d(d):
    dout = dict()
    for i in d:
        if len(sottoalbero(d,i,{})) == len(d)-1:
            dout[i] = d[i], 0
        for j in d[i]:
            dout[j] = d[j], i
    return dout

def sopralbero(dm, x, dout):
    if dm[x][1] != 0:
        dout[dm[x][1]] = dm[dm[x][1]][0]
        sopralbero(dm,dm[x][1],dout)
    else:
        dout[x] = dm[x][0]
    return dout

def ricava_d(fnome):
    with open(fnome, encoding = 'utf-8') as f:
        t = f.read()
        d = json.loads(t)
    return d