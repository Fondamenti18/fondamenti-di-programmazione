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
'''branch={}
    treegen(branch,tree,[x])
    toremove=set(branch.keys())
    allkeys=set(tree.keys())
    newdic={}
    for el in (allkeys-toremove):
        if x in tree[el]:del(tree[el][tree[el].index(x)])
        newdic[el]=tree[el]'''
import json
#from functools import lru_cache as cache

#@cache(maxsize=None)

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    tree=json.loads(open(fnome).read())
    branch={}
    treegen(branch,tree,[x])
    fo=open(fout,mode='w')
    json.dump(branch,fo)
    fo.close()
    return

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    tree=json.loads(open(fnome).read())
    rmv(tree,[x])
    for el in tree.values():
        if x in el:
            del(el[el.index(x)])
            break
    fo=open(fout,mode='w')
    json.dump(tree,fo)
    fo.close()
    return

def rmv(tree,ls):
    if ls==[]:return
    else:
        sons=[]
        for el in ls:sons+=tree.pop(el)
        return rmv(tree,sons)

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    tree=json.loads(open(fnome).read())
    for k in tree.keys():
        leaf=k
        break    
    root=rootfinder(tree,leaf)
    level={0:[root]}
    treelvl(tree,level,[root],1)
    fo=open(fout,mode='w')
    json.dump(level,fo)
    fo.close()
    return

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    tree=json.loads(open(fnome).read())
    for k,v in tree.items():
        if v==[]:
            leaf=k
            break      
    root=rootfinder(tree,leaf)
    grades={root:0}
    ancients(tree,grades,y,[root],0)
    fo=open(fout,mode='w')
    json.dump(grades,fo)
    fo.close()
    return

def treegen(branch,tree,ls):
    if ls==[]:return
    else:
        leaf=[]
        for x in ls:
            branch[x]=tree[x]
            leaf+=tree[x]
    return treegen(branch,tree,leaf)

def treelvl(tree,level,ls,lvl):
    if ls==[]:return
    else:
        leaf=[]
        for x in ls:
            leaf+=tree[x]
        if leaf!=[]:    
            level[lvl]=sorted(leaf)   
    return treelvl(tree,level,leaf,lvl+1)
 
def rootfinder(tree,leaf):
    a=0
    for k,v in tree.items():
        if leaf in v:return rootfinder(tree,k)
        else:a+=1
    if a==len(tree):return leaf
        
def ancients(tree,grades,y,ls,k):
    branches=[]
    if ls==[]:return
    for i in ls:
        br=tree[i]
        if len(br)==y:
            grades[i]=k
            ancients(tree,grades,y,br,k+1)
        else:
            grades[i]=k
            branches+=tree[i]
    return ancients(tree,grades,y,branches,k)    
        
    
    
if __name__=='__main__':
    genera_sottoalbero('Alb100.json','ultras','tAlb100_1.json')
    cancella_sottoalbero('Alb10.json','d','tAlb10_2.json')
    dizionario_livelli('Alb20000.json','tAlb20000_3.json')
    dizionario_livelli('Alb10.json','tAlb10_3.json')
    dizionario_gradi_antenati('Alb10.json',2,'tAlb10_4.json')
    dizionario_gradi_antenati('Alb20000.json',2,'tAlb20000_4.json')