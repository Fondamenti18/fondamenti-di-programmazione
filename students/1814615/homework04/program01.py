# -*- coding: utf-8 -*-
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
                                  |
                                 'i'


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

def dfs_ricorsivo(albero, nodo, path=[]):
    path += [nodo]
    for vicino in albero[nodo]:
        if vicino not in path:
            path = dfs_ricorsivo(albero, vicino, path)

    return  path

#==========================================================================

def  genera_sottoalbero (fnome,x,fout):
    import json
    path=[]
    dizz={}
    with open(fnome) as json_data:
        tree = json.load(json_data)
    diz=tree
    dfs_ricorsivo(tree, x,path)
    for k in path:
        dizz[k]=diz[k]
    with open(fout, 'w') as f:
        json.dump(dizz, f)
    return

#==========================================================================

def cancella_sottoalbero(fnome,nodo_origine,fout):
 
    import json
    path=[]
    dizz={}
    with open(fnome) as json_data:
        tree = json.load(json_data)
    diz=tree
    dfs_ricorsivo(tree, nodo_origine,path)
    for k in path:
        dizz[k]=diz[k]
    for k in (path) :
        diz.pop(k)
    for v in diz.values():
        if (nodo_origine) in v:
            v.remove((nodo_origine))
    with open(fout, 'w') as f:
        json.dump(diz, f)
    return  
#==========================================================================

def inverti_diz(d):
    inverso = dict()
    for chiave in d:
        val = d[chiave]
        if val not in inverso:
            inverso[val] = [chiave]
        else:
            inverso[val].append(chiave)
        inve=inverso[val]
        inve.sort()
    return inverso
#==========================================================================

def generazione_rami(albero):
    rami = []
    for nodo in albero:
        for vicino in albero[nodo]:
            rami.append((nodo, vicino))

    return rami
#==========================================================================
def backtrace(genitore, inizio, fine):
     path = [fine]
     while path[-1] != inizio:
         path.append(genitore[path[-1]])
     path.reverse()
     return path
#==========================================================================

def bfs(albero, inizio, fine):
    coda = []
    coda.append([inizio])
    while coda:
        path = coda.pop(0)
        nodo = path[-1]
        if nodo == fine:
            return path
        for adiacente in albero.get(nodo, []):
            nuovo_path = list(path)
            nuovo_path.append(adiacente)
            coda.append(nuovo_path)
    return

  #==============================================================================

def dizionario_gradi_antenati(fnome,y,fout):
    import json
    with open(fnome) as json_data:
        tree = json.load(json_data)
    diz_grado_antenati={}
    percorso=[]
   
    spigoli=generazione_rami(tree)
    mylist= [elem[0] for elem in spigoli]
    mylist1= [elem[1] for elem in spigoli]
    list1=set(mylist)
    list2=set(mylist1)
    aa=list1.difference(list2)
    radice=aa.pop()
    nodi1=dfs_ricorsivo(tree, radice,percorso)
    nodi=nodi1[::-1] 
    num_grado=[]
    lista_nodi=[]
    diz_antenati={}
    for i in range (len(nodi)):
        kk=nodi[i]
        num_grado.append(mylist.count(kk))
        diz_antenati[kk]=mylist.count(kk)
        diz_grado_antenati[kk]=-1
        lista_nodi.append(kk)
    tupla_radice=tree[radice]
    lun_tupla=len(tupla_radice)
    
    diz_antenati[radice]=lun_tupla
    diz_grado_antenati[radice]=0
    ktot_nodi=0
    for ki in nodi: 
        ktot_nodi=ktot_nodi+1
        if diz_grado_antenati[ki]!=-1:
            continue
        percorso1=bfs(tree,radice, ki)
        percorso=percorso1[::-1]
        lung=len(percorso)
        for j in range (lung-1):
            if diz_grado_antenati[percorso[j]]!=-1:continue
            lista_nodi.remove(percorso[j])
            kcont=0
            for i in range (j+1,lung):
                if diz_antenati[percorso[i]]==2:
                    kcont=kcont+1
                diz_grado_antenati[percorso[j]]=kcont
        if lista_nodi==[radice]: 
             break
    with open(fout, 'w') as f:
        json.dump(diz_grado_antenati, f)
    return

#==========================================================================

def dizionario_livelli(fnome,fout):
    import json
    percorso=[]
    nodi=[]
    lung=[]
    diz_livelli={}
    lista_nodi=[]

    with open(fnome) as json_data:
        tree = json.load(json_data)
    spigoli=generazione_rami(tree)
    mylist= [elem[0] for elem in spigoli]
    mylist1= [elem[1] for elem in spigoli]
    list1=set(mylist)
    list2=set(mylist1)
    aa=list1.difference(list2)
    radice=aa.pop()
    nodi1=dfs_ricorsivo(tree, radice,percorso)
    nodi=nodi1[::-1]
    for i in range (len(nodi)):
        kk=nodi[i]
        diz_livelli[kk]=-1
        lista_nodi.append(kk)
    diz_livelli[radice]=0
    ktot_nodi=0
    ktot=0
    for ki in nodi: 
        ktot=0
        ktot_nodi=ktot_nodi+1
        if diz_livelli[ki]!=-1:
            continue
        percorso1=bfs(tree,radice, ki)
        percorso=percorso1[::-1]
        lung=len(percorso)
        diz_livelli[percorso[ktot]]=lung-1
        lista_nodi.remove(percorso[ktot])
        for i in range (1,lung-1):
           if diz_livelli[percorso[i]] != -1: 
               break
           diz_livelli[percorso[i]]=lung-i-1
           lista_nodi.remove(percorso[i])
        if lista_nodi==[radice]: 
             break
    inv_diz=inverti_diz(diz_livelli)
    with open(fout, 'w') as f:
        json.dump(inv_diz, f)
    return