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
    diz = json.load(open(fnome))
    lst = [x]
    out = {}
    ritorna_el(diz,x,lst)
    for i in lst:
            if i in diz:
                out[i] = diz[i]
    with open(fout,'w') as diz:
        json.dump(out,diz)
        
        
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    diz = json.load(open(fnome))
    lst = [x]
    lst2 = []
    out = {}
    ritorna_el(diz,x,lst)
    for i in diz:
        if i not in lst:
            lst2.append(i)
    for n in lst2:
        if x in diz[n]:
            diz[n].remove(x)
        out[n] = diz[n]
    with open(fout,'w') as diz:
        json.dump(out,diz)


def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    diz = json.load(open(fnome))
    out = {}
    for x in diz:
        padre = diz1(diz,x)
        if padre == "":
            out[0] = [x]
        else:
            livello = ritorna_livello(out,padre) + 1
            if livello in out:
                lstg = out[livello]
                lstg.append(x)
                out[livello] = lstg
            else:
                out[livello] = [x]
    for x in out:
        lstg = out[x]
        lstg.sort()
        out[x] = lstg
    with open(fout,'w') as diz:
        json.dump(out,diz) 
        

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    diz = json.load(open(fnome))
    chiavi = []
    for x in diz:
        chiavi.append(x)
    out = {}
    lstgy = []
    for x in chiavi:
        if len(diz[x]) == y:
            lstgy.append(x)
    for x in chiavi:
        if len(diz[x]) == 0:
            diz.pop(x)         
    for x in chiavi:
        lstan = []
        figli = []
        padri = []
        num = 0
        cerca_antenati(diz,x,lstan,figli,padri)
        for z in lstan:
            if z in lstgy:
                num += 1
        out[x] = num
    with open(fout,'w') as diz:
        json.dump(out,diz)


def ritorna_el(diz,x,lst):
    if x in diz:
        lst += diz[x]
        for i in diz[x]:
            ritorna_el(diz,i,lst)
            
            
def ritorna_livello(out,padre):
    lstp = []
    for y in out:
        lstp = out[y]
        if padre in lstp:
            return y
    return 0

def cerca_antenati(diz,x,lstan,figli,padri):
    try:
        papa = figli.index(x)
    except ValueError: 
        papa = diz1(diz,x)
        figli.append(x)
        padri.append(papa)
    if papa != "":
        lstan.append(papa)
        cerca_antenati(diz,papa,lstan,figli,padri)

def diz1(diz,x):
    padre = ""
    for i in diz:
        if x in diz[i]:
            padre = i
            break
    return padre                        
