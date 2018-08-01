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

- il nome di un file json contenente un dizionario-albero  d (fnome)
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

- il nome di un file json contenente un dizionario-albero  d (fnome)
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
- il nome di un file json contenente un dizionario-albero  d (fnome)
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
'''


import json

def genera_sottoalbero(fnome,x,fout):
	fs=open(fnome,'r')
	dtree=json.load(fs)
	fs.close()
	rdtree={}
	rdtree=treefromx(x, dtree, rdtree)
	fileo=open(fout,'w')
	json.dump(rdtree,fileo)
	fileo.close()
	return None

def treefromx(x, dic, rdtree):
	if x not in dic.keys():
		return rdtree
	else:
		rdtree[x]=dic[x]
		for l in dic[x]:
			rdtree=treefromx(l, dic, rdtree)
	return rdtree

def cancella_sottoalbero(fnome,x,fout):
	fs=open(fnome,'r')
	dtree=json.load(fs)
	fs.close()
	rdtree={}
	rdtree=treefromx(x, dtree, rdtree)
	for l in rdtree.keys():
		del dtree[l]
		for i in dtree:
			if l in dtree[i]:
				dtree[i].remove(l)
	fileo=open(fout,'w')
	json.dump(dtree,fileo)
	fileo.close()
	return None

def dizionario_livelli(fnome,fout):
	fs=open(fnome,'r')
	dtree=json.load(fs)
	fs.close()
	level=0
	rdlevel={}
	ke=list(dtree.keys())
	root=search_root(dtree)
	rdlevel=levelfromd(level,[root],dtree,rdlevel)
	fileo=open(fout,'w')
	json.dump(rdlevel,fileo)
	fileo.close()
	return None

def levelfromd(lev, lis, dic,rdl):
	if lis!=[]:
		if rdl=={}: rdl[lev]=lis
		else:
			if lev in rdl.keys():
				rdl[lev].extend(lis)
			else: rdl[lev]=lis
		rdl[lev].sort()
		for l in lis:
			rdl=levelfromd(lev+1, dic[l], dic, rdl)
	return rdl

def search_root(dic):
    ins_keys=set(dic.keys())
    ins_values=set()
    for x in ins_keys:
        for y in dic[x]:
            ins_values.add(y)
    return ((ins_keys) - (ins_values)).pop()
			
def dizionario_gradi_antenati(fnome,y,fout):
	fs=open(fnome,'r')
	tree=json.load(fs)
	rad_tree=search_root(tree)
	dict_empty=dict()
	for x in tree.keys():
		dict_empty[x]=0
	a=open(fout,'w')

	b=search_grade(tree,rad_tree,dict_empty,y)
	json.dump(b,a)
	
	fs.close()
	a.close()
	 
def search_grade(tree,rad_tree,dict_empty,y):
        for i in tree[rad_tree]:
                count_fathery=dict_empty[rad_tree]
                if len(tree[rad_tree])==y:
                        dict_empty[i]=count_fathery+1
                else: dict_empty[i]=count_fathery
        for value in tree[rad_tree]:
                if tree[rad_tree]!=[]:
                        search_grade(tree,value,dict_empty,y)
        return dict_empty
		
