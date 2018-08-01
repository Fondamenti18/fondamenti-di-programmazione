

import json, sys
sys.setrecursionlimit(100000)

testa=''

def create (file, msg):
    with open( file, mode='w') as f:
        f.write(json.dumps(msg))

def extract (file):
    with open( file, mode='r') as f:
        return json.load(f)

def sottoalbero (tree, x, result={}):
    result[x]=tree[x]
    for nodo in result[x]:
        sottoalbero(tree, nodo, result)
    return

def delSottoalbero (tree, x):
    for nodo in tree[x]:
        delSottoalbero(tree, nodo)
    del tree[x]
    return
        
def genera_sottoalbero(fnome,x,fout):
    tree=extract(fnome)
    result= {}
    if x in tree.keys():
        sottoalbero(tree, x, result)
    create(fout, result)
    return result

    
    

def cancella_sottoalbero(fnome,x,fout):
    tree=extract(fnome)
    delSottoalbero(tree, x)
    for key, value in tree.items():
        if x in value:break
    tree[key].remove(x)
    create(fout, tree)
    return tree

def concatenaa(lista):
	if len(lista)<=1:
		return lista[0]
	else:
		return lista[0] + concatena(lista[1:]) 

def concatena(lista):
    while len(lista>1):
        lista[1]= lista[0] + lista[1]
        lista= lista[1:]
    return lista[0]

def dizionario_livelli(fnome,fout): 
    global testa
    tree=extract(fnome)
    head=list(tree.keys())
    #nodi= set(concatena(list(tree.values())))
    #head.difference_update(nodi)
    result={} 
    for value in tree.values():
        for nodo in value:
            if nodo:
                head.remove(nodo)
    
    testa= head[0]
    result[0]=head
    livelli (tree, result)
    create(fout, result)
    return result

def livelli(tree, result, level=0):
    livello=[]
    for nodo in result[level]:
        livello += tree[nodo]
    if livello==[]: return
    livello.sort()
    result[level+1]= livello
    livelli(tree, result, level+1)
    
 

def dizionario_gradi_antenati(fnome,y,fout):
    global testa
    tree= extract(fnome)
    result={}
    #head=list(tree.keys())
    #for value in tree.values():
    #    for nodo in value:
    #        head.remove(nodo)
    #head= head.pop()
    gradi(tree, result, testa, 0, y)
    create(fout, result)
    return result

def gradi (tree, result, head, g, y):
    result[head]= g
    if len(tree[head]) == y:
        g+=1
    for nodo in tree[head]:
        gradi(tree, result, nodo, g, y)
    
    

