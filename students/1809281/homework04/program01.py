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

{0: ['a'],
1: ['b'],
2: ['c', 'd'],
3: ['e','i','l'],
4: ['f', 'g', 'h']}
                        
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



import json


################################ FUNCTION N.1 ################################
def genera_sottoalbero(fnome,x,fout):
    result = {}
    tree = {}
    
    with open(fnome, encoding = 'utf-8') as infile:
        tree = json.load(infile)
    
    result = build_subtree(tree, x)
    
    with open(fout, mode = 'w', encoding = 'utf-8') as outfile:
        json.dump(result, outfile)
    # print(result)
        
def build_subtree(tree, x):
    if tree[x] == []:
        return {x : tree[x]}
        
    else:
        subtree = {x : tree[x]}
        for branch in tree[x]:
            subtree.update(build_subtree(tree, branch))
        return subtree

        
     

        
################################ FUNCTION N.2 ################################        
def cancella_sottoalbero(fnome,x,fout):
    with open(fnome, encoding = 'utf-8') as infile:
        tree = json.load(infile)
    
    subtree = build_subtree(tree, x)
    
    for k in subtree.keys():
        if k in tree.keys():
            del tree[k]
         
        for v in tree.values():
            if k in v:
                v.remove(k)
                continue
    
    with open(fout, mode = 'w', encoding = 'utf-8') as outfile:
        json.dump(tree, outfile)
    # print(tree)

    
    
    
    
    
################################ FUNCTION N.3 ################################   
def dizionario_livelli(fnome,fout):
    with open(fnome, encoding = 'utf-8') as infile:
        tree = json.load(infile)
        
    result = {}
        
    for key in tree.keys():
        result = {0 : [key]}
        organize(tree, key, 1, result)
        break
        
    for value in result.values():
        value.sort()
        
    # print(result)
        
    with open(fout, mode = 'w', encoding = 'utf-8') as outfile:
        json.dump(result, outfile)
    
   
   
def organize(tree, key, level, result):
    if tree[key] == []:
        return []
    else:      
        a = result.get(level, [])
            
        for branch in tree[key]:
            a.append(branch)
        result[level] = (a)
        
        # print(a)
        # print(result)
        
        for branch in tree[key]:
            organize(tree, branch, level + 1, result)
        
        return result 
    
    
    
    
################################ FUNCTION N.4 ################################  
def dizionario_gradi_antenati(fnome,y,fout):  
    with open(fnome, encoding = 'utf-8') as infile:
        tree = json.load(infile)
        
    result = {}
    for key in tree.keys():
        result.update({key : 0})
        
    for key in result.keys():
        if len(tree[key]) == y:
            increase_branch_grade(tree, key, result)
        
    # print(result)
    
    with open(fout, mode = 'w', encoding = 'utf-8') as outfile:
        json.dump(result, outfile)
    
    
    
    
def increase_branch_grade(tree, key, result, first_run = True):
    if not first_run:
        result[key] += 1
        
    if not tree[key] == []:
        for branch in tree[key]:
            increase_branch_grade(tree, branch, result, False)
    
    
if __name__ == '__main__':
    # genera_sottoalbero('Alb10.json','d','test1.json')
    # cancella_sottoalbero('Alb10.json','d','test2.json')
    # dizionario_livelli('Alb10.json','test3.json')	
    dizionario_gradi_antenati('Alb10.json',2,'test4.json')
    pass
    