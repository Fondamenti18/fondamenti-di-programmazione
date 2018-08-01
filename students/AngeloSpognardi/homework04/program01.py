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

def gen_subtree(tree, nlist):
    if not nlist:
        return {}
    head=nlist[0]
    headlist=tree[head][:]
    return {head:headlist, **gen_subtree(tree,nlist[1:]+headlist)}

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as f:
        tree=json.load(f)
    nodes=tree.setdefault(x)
    if nodes:
        subtree={x:nodes[:], **gen_subtree(tree, nodes[:])}
    else:
        subtree={x:[]}
    with open(fout, 'w') as f:
        json.dump(subtree, f)

def del_subtree(tree, nlist):
    if not nlist:
        return
    head=nlist[0]
    headlist=tree[head][:]
    del_subtree(tree, headlist+nlist[1:])
    del tree[head]

        
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as f:
        tree=json.load(f)
    del_subtree(tree, [x])
    for n,c in tree.items():
        if x in c:
            c.remove(x)
    with open(fout, 'w') as f:
        json.dump(tree, f)

def gen_levdiz(diz, n, tree, lev):
    if tree[n]:
        for child in tree[n]:
            gen_levdiz(diz, child, tree, lev+1)
    listlev=diz.setdefault(lev,[])+[n]
    diz[lev]=sorted(listlev)

def gen_parentdiz(tree):
    parentdiz={}
    for k,v in tree.items():
        for el in v:
            parentdiz[el]=k
    return parentdiz

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as f:
        tree=json.load(f)
    parentdiz=gen_parentdiz(tree)
    root=(set(tree.keys()) - set(parentdiz.keys())).pop()
    level_diz={}
    gen_levdiz(level_diz, root, tree, 0)
    with open(fout, 'w') as f:
        json.dump(level_diz, f)

def gen_diz_ga(diz, n, tree, y, antenaty):
    diz[n]=antenaty
    if len(tree[n])==y:
        antenaty+=1
    if tree[n]:
        for child in tree[n]:
            gen_diz_ga(diz, child, tree, y, antenaty)
    

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as f:
        tree=json.load(f)
    parentdiz=gen_parentdiz(tree)
    root=(set(tree.keys()) - set(parentdiz.keys())).pop()
    diz_ga={}
    gen_diz_ga(diz_ga, root, tree, y, 0)
    with open(fout, 'w') as f:
        json.dump(diz_ga, f)


    
if __name__ == "__main__":
    cancella_sottoalbero('Alb10.json','d','asd')
    dizionario_livelli('Alb10.json','asd')
    dizionario_gradi_antenati('Alb10.json',2,'asd')
