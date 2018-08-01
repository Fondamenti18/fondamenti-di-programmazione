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



def gen_subdict_tree(dictionary,node,subdict_tree):
	
#	if subdict_tree is None:
#		subdict_tree = {}

	if node in set(dictionary.keys()):
		subdict_tree[node] = dictionary[node]
		
		for child in dictionary[node]:
			gen_subdict_tree(dictionary,child,subdict_tree)

	return subdict_tree



def gen_dict_levels(dictionary,node,level,dict_levels):
	
#	if dict_levels is None:
#		dict_levels = {}

	if level in dict_levels.keys():
		dict_levels[level].append(node)
	
	else: 
		dict_levels[level] = [node]
	
	for child in dictionary[node]:
		gen_dict_levels(dictionary,child,str(int(level)+1),dict_levels)

	return dict_levels



def get_ancestors_grade_tree(dictionary,curr_level,max_level,y,dict_levels,grade_dict,ancestors_grade_tree):

	if curr_level<max_level:
		for node_level in dict_levels[str(curr_level)]:
			if grade_dict[node_level] == y:
				for child in dictionary[node_level]:
					ancestors_grade_tree[child]= ancestors_grade_tree[node_level]+1
			else:
				for child in dictionary[node_level]:
					ancestors_grade_tree[child]= ancestors_grade_tree[node_level]
		get_ancestors_grade_tree(dictionary,int(curr_level)+1,max_level,y,dict_levels,grade_dict,ancestors_grade_tree)
	
	return ancestors_grade_tree



def genera_sottoalbero(fnome,x,fout):
	
	with open(fnome, mode="r", encoding="utf-8") as file_being_read:
		json_string = file_being_read.read()
		
		dict_tree = json.loads(json_string)

		subdict_tree = {}
		subdict_tree = gen_subdict_tree(dict_tree,x,subdict_tree)

	with open(fout, mode="w", encoding="utf-8") as file_being_written:
		json.dump(subdict_tree, file_being_written)



def cancella_sottoalbero(fnome,x,fout):
	
	with open(fnome, mode="r", encoding="utf-8") as file_being_read:
		json_string = file_being_read.read()
		
		dict_tree = json.loads(json_string)
		dict_tree_clone = dict_tree.copy()

		dict_to_remove = {}
		dict_to_remove = gen_subdict_tree(dict_tree,x,dict_to_remove)
		
		for node,children in dict_tree.items():
			if x in children:
				dict_tree_clone[node].remove(x)
			if node in dict_to_remove.keys():
				del dict_tree_clone[node]

	with open(fout, mode="w", encoding="utf-8") as file_being_written:
		json.dump(dict_tree_clone, file_being_written)



def dizionario_livelli(fnome,fout):
	
	with open(fnome, mode="r", encoding="utf-8") as file_being_read:
		json_string = file_being_read.read()
		
		dict_tree = json.loads(json_string)
		
		all_keys=set(dict_tree.keys())
		
		all_values=set()
		for children in dict_tree.values():
			all_values |= set(children)
		
		root_singleton = (all_keys - all_values)
		root = root_singleton.pop()
		
		dict_levels = {}
		dict_levels = gen_dict_levels(dict_tree,root,"0",dict_levels)

		for v in dict_levels.values():
			v.sort()

	with open(fout, mode="w", encoding="utf-8") as file_being_written:
		json.dump(dict_levels, file_being_written)



def dizionario_gradi_antenati(fnome,y,fout):
	
	with open(fnome, mode="r", encoding="utf-8") as file_being_read:
		json_string = file_being_read.read()
		
		dict_tree = json.loads(json_string)
		
		all_keys=set(dict_tree.keys())
		
		all_values=set()
		for children in dict_tree.values():
			all_values |= set(children)
		
		root_singleton = (all_keys - all_values)
		root = root_singleton.pop()
		
		grade_dict={}
		for node in dict_tree.keys():
			grade_dict[node] = len(dict_tree[node])
		
		dict_levels = {}
		dict_levels = gen_dict_levels(dict_tree,root,"0",dict_levels)
		
		max_level = int(max(dict_levels.keys()))
		
		ancestors_grade_tree = {}
		for k in dict_tree.keys():
			ancestors_grade_tree.setdefault(k, 0)
		
		ancestors_grade_tree = get_ancestors_grade_tree(dict_tree,0,max_level,y,dict_levels,grade_dict,ancestors_grade_tree)

	with open(fout, mode="w", encoding="utf-8") as file_being_written:
		json.dump(ancestors_grade_tree, file_being_written)