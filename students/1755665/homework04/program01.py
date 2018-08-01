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
import sys
sys.setrecursionlimit(999999999)

def genera_sottoalbero(fnome,x,fout):
    '''crea un sotto-albero partendo
        dal nodo x'''
    f=open(fnome)
    r=f.read()
    diz=json.loads(r)
    dizout=tree_generated(diz, {}, x)
    ret=open(fout,'w')
    ret.write(json.dumps(dizout))
    ret.close()

def cancella_sottoalbero(fnome,x,fout):
    '''cancella dallìalbero il sottoalbero
        radicato in x'''
    f=open(fnome)
    r=f.read()
    diz=json.loads(r)
    dizout=tree_generated(diz, {}, x)
    for k in dizout.keys():
        del diz[k]
    for l in diz.values():
        if x in l:
            l.remove(x)
    ret=open(fout,'w')
    ret.write(json.dumps(diz))
    ret.close()
      

def dizionario_livelli(fnome,fout):
    '''torna diz con livelli nel file'''
    f=open(fnome)
    r=f.read()
    diz=json.loads(r)
    r=search_tree_radix(diz)
    dizout=livelli(diz, 0, {0:[r]})
    ret=open(fout,'w')
    ret.write(json.dumps(dizout))
    ret.close()
 

def dizionario_padre(d):
    dizout={}
    for k in d.keys():
        if len(d[k])>0:
            for item in d[k]:
                dizout[item]=k
    return dizout

def trova_antenati(d, dp, v, grado, count):
    if v in dp.keys():
        p=dp[v]
        if len(d[p])==grado:
            return trova_antenati(d, dp, p, grado, count+1)
        else:
            return trova_antenati(d, dp, p, grado, count)
    else:
        return count

def dizionario_gradi_antenati(fnome,y,fout):
    '''torna il dizionario con gli antenati di grado y'''
    f=open(fnome)
    r=f.read()
    diz=json.loads(r)
    dizout=dict()
    dp=dizionario_padre(diz)
    for k in diz.keys():
        dizout[k]=trova_antenati(diz, dp, k, y, 0)
    ret=open(fout,'w')
    ret.write(json.dumps(dizout))
    ret.close()
    


def livelli(diz, c, out):
    l = []
    for node in out[c]:
        l += diz[node]
    if len(l) > 0:
        l.sort()
        out[c + 1] = l
        return livelli(diz, c+1, out)
    return out

def tree_generated(diz, out, n):
    '''funzione ricorsiva che genera il subdizionario partendo da un dizionario out vuoto e il nodo'''
    if n in diz:
        out[n] = diz[n]
        for node in diz[n]:
            tree_generated(diz, out, node)
    return out
    
def search_tree_radix(diz):
    '''torna la radice'''
    lis=[]
    for e in diz.values():
        lis += e
    for x in diz.keys():
        if x not in lis:
            return x



