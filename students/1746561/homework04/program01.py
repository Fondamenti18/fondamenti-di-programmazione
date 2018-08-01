'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero  e l'attributo della chiave e' la lista 
(eventualmente vuota) degli identificativi dei  figli del nodo. Gli identificativi dei nodi 
all'interno delle liste sono in ordine lessicografico crescente.



Ecco un esempio di dizionario d che rappresenta un dizionario-albero

d={
'a':['b'],           1
'b':['c','d'],       2
'c':['i'],           3
'd':['e','l'],       4
'e':['f','g','h'],   5
'f':[],              6
'g':[],              7
'h':[],              8
'i':[],              9
'l':[]              10 
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

4)
la funzione dizionario_gradi_antenati(fnome,y,fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fnome)
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

Il terzo punto dà errore di ricorsione, forse è perchè le liste vuote aggiunte sono troppe e andrebbero 
eliminate mano a mano
'''





import json, itertools, time

def albero(fnome): 
    with open(fnome,'r') as f:
        tree = json.load(f)
    return tree

def sottoalbero(fnome,x,dic):
    tree = albero(fnome)
    for k,v in tree.items():
        if k == x: 
            dic[k] = v
            for i in v:
                sottoalbero(fnome,i,dic)
    return dic

def genera_sottoalbero(fnome,x,fout):
    dic = {}
    with open(fout, 'w') as f:
        f.write(str(json.dumps(sottoalbero(fnome,x,dic))))

def rimozione(fnome, x,tree):
    for k,v in tree.copy().items():
        if x in v: v.remove(x)
        if k == x:
            del tree[k]
            for i in v:
                rimozione(fnome, i,tree)
    return tree
         
def cancella_sottoalbero(fnome,x,fout):
    tree = albero(fnome)
    with open(fout, 'w') as f:
        f.write(str(json.dumps(rimozione(fnome,x,tree))))
        
def lvl(fnome, dic, c, q):
   tree = albero(fnome)
   if c == len(tree): return
   k, v = list(tree.keys()), list(tree.values())
   if c == 0:
       q.extend([k[0], None])
       dic[c] = (q[:-1])
   qc = q.copy()
   for el in range(len(qc)):
       if qc[el] is None:
           q.remove(qc[el])
           q.append(None)
           c += 1
           dic[c] = sorted(q[:-1])
           lvl(fnome,dic,c,q)
           return dic
       q.extend(v[k.index(qc[el])])
       q.pop(0)
        
def dizionario_livelli(fnome,fout):
    c, q, dic = 0, [], {}
    dic = dict((k, v) for k, v in lvl(fnome,dic,c,q).items() if v)
    with open(fout, 'w') as f:
        f.write(json.dumps(dic))
     
def children(tree,val): #crea il percorso
    ls = []
    if tree[0][1] == []:
        val = tree[0]
    for i in tree:
        if val[0] in i[1]:
            val = i[0]
            ls.append(val)
    return ls

def crea_dizionario(fnome, ls): #ad ogni percorso associa i figli 
    dic = {}
    tree = list(albero(fnome).items())
    for i in range(len(ls)):
        for j in range(len(tree)):
            if ls[i] == tree[j][0]:
                dic[ls[i]]= tree[j][1]
    return dic
    
def gradi(d, y, grade, dic): #riceve crea_ che riceve children
    l = list(d.items())
    for i in range(len(l)):
        if i == 0:
            dic[l[i][0]] = 0
        if len(l[i-1][1]) == y:
            grade += 1
        dic[l[i][0]] = grade
    return dic

def nonni(fnome, tree, y, dict_f):
    if len(tree) == 0: return
    if tree[0][1] == []: 
        val, grade, dic = 0, 0, {}
        ls = list(reversed(list(children(tree,val))))+[tree[0][0]]
        diz = crea_dizionario(fnome,ls)
        dict_f.update(gradi(diz,y,grade,dic))
    nonni(fnome, tree[1:],y,dict_f)
    return dict_f

def dizionario_gradi_antenati(fnome,y,fout): 
    tree = list(reversed(list(albero(fnome).items())))
    dic = {}
    with open(fout, 'w') as f:
        f.write(json.dumps(nonni(fnome,tree,y,dic)))
