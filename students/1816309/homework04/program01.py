'''
Diciamo che un dizionario dizionario rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di dizionario e' un identificativo di un nodo dell'albero  e l'attributo della chiave e' la lista 
(eventualmente vuota) degli identificativi dei  figli del nodo. Gli identificativi dei nodi 
all'interno delle liste sono in ordine lessicografico crescente.



Ecco un esempio di dizionario dizionario che rappresenta un dizionario-albero

dizionario={
'a':['b'],
'b':['carattere','dizionario'],
'carattere':['i'],
'dizionario':['e','l'],
'e':['f','g','h'],
'f':[],
'g':[],
'h':[],
'i':[],
'l':[]
}

L'albero rappresentato da dizionario e'

                             'a'
                              |
                _____________'b'____________             
               |                            |            
              'carattere'                  ________'dizionario'_______   
               |                  |                  |  
              'i'         _______'e'_______         'l'
                         |        |        |               
                        'f'      'g'      'h'


Implementare le seguenti funzioni:

1) 
la funzione genera_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  dizionario (fonome)
- un identificativo x
- il nome di un file json (fout)

produce   il  dizionario-albero che rappresenta   il sottoalbero  radicato 
nell'identificativo x che si ottiene dal dizionario-albero dizionario. 
Il dizionario-albero ottenuto va registrato nel file fout.
Se l'identificativo x non e' tra i nodi di dizionario allora  il dizionario-albero prodotto 
deve essere vuoto.

Ad esempio se fnome contiene il dizionario-albero dizionario allora dopo l'esecuzione di 
genera_sottoalbero(fname,'dizionario',fout)
il file fout conterra' il dizionario
{'f': [], 'g': [], 'h': [], 'e': ['f', 'g', 'h'], 'l': [], 'dizionario': ['e', 'l']}



2)
la funzione cancella_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  dizionario (fonome)
- un identificativo x
- il nome di un file json (fout)

ricava  da dizionario il sottoalbero radicato in x e lo salva nel file fout.
Se x non e' presente tra le chiavi di  dizionario allora  il dizionario-albero dizionario non viene modificato.

Ad esempio se fnome contiene il dizionario-albero dizionario allora dopo l'esecuzione di 
cancella_sottoalbero(fname,'dizionario',fout)
il file fout conterra' il dizionario
{'a': ['b'], 'b': ['carattere'], 'carattere': ['i'], 'i':[]}


3)
la funzione dizionario_livelli(fnome, fout) che, presi:
- il nome di un file json contenente un dizionario-albero  dizionario (fnome)
- il nome di un file json (fout)

costruisce il  dizionario che ha come  chiavi i livelli del dizionario-albero dizionario. L'attributo di una 
chiave di valore x e' la lista degli identificativi  dei nodi che si trovano a livello x  nell'albero rappresentato da dizionario. 
La lista e' ordinata lessicograficamente ed in modo crescente. 
Il dizionario cosi' costruito va registrato nel file fout.

Ad esempio se fnome contiene il dizionario-albero dizionario allora dopo l'esecuzione di  
dizionario_livelli(fname,fout)
il file fout conterra' il dizionario
{0: ['a'], 1: ['b'], 2: ['carattere', 'dizionario'], 3: ['e','i','l'], 4: ['f', 'g', 'h']}

4)
la funzione dizionario_gradi_antenati(fnome,y,fout) che, presi:
- il nome di un file json contenente un dizionario-albero  dizionario (fonome)
- un intero y
- il nome di un file json (fout)

costuisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero 
rappresentato dal dizionario-albero dizionario, Attributo di una chiave di valore x e' il numero 
di antenati di grado y che ha il nodo con identificativo x nell'albero.
Registra il dizionario costruito nel file fout.

Ad esempio se fnome contiene il dizionario-albero dizionario allora dopo l'esecuzione di  
dizionario_gradi_antenati(fnome,2,fout)
il file fout conterra' il dizionario 
{'a': 0, 'b': 0, 'carattere': 1, 'dizionario': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.
'''


import json
from collections import Counter

def genera_sottoalbero(fnome,x,fout):
	dizionario = json.loads(open(fnome).read())
	risultato = dict()
	save_tree(x,dizionario,risultato)
	open(fout,'w').write(json.dumps(risultato))

def save_tree(nodo,dizionario,risultato):
	risultato[nodo] = dizionario[nodo]
	for figlio in dizionario[nodo]:
		save_tree(figlio,dizionario,risultato)

def cancella_sottoalbero(fnome,x,fout):
	dizionario = json.loads(open(fnome).read())
	canc_tree(x,dizionario)
	for key in dizionario:
		if x in dizionario[key]:
			dizionario[key].remove(x)
	open(fout, 'w').write(json.dumps(dizionario))

def canc_tree(nodo,dizionario):
	for figlio in dizionario[nodo]:
		canc_tree(figlio,dizionario)
	del(dizionario[nodo])

def dizionario_livelli(fnome,fout):
	json_stringa = open(fnome).read()
	dizionario = json.loads(json_stringa)
	risultato = dict()
	gen_livelli(get_root(json_stringa),dizionario,risultato,0)
	for key in risultato:
		risultato[key] = sorted(risultato[key])
	open(fout,'w').write(json.dumps(risultato))

def gen_livelli(nodo,dizionario,risultato,livello):
	if not risultato.get(livello):
		risultato[livello] = []
	risultato[livello] += [nodo]
	for figlio in dizionario[nodo]:
		gen_livelli(figlio,dizionario,risultato,livello+1)

def dizionario_gradi_antenati(fnome,y,fout):
	json_stringa = open(fnome).read()
	dizionario = json.loads(json_stringa)
	risultato = dict()
	gen_gradi(get_root(json_stringa),dizionario,risultato,y,0)
	open(fout,'w').write(json.dumps(risultato))
def gen_gradi(nodo,dizionario,risultato,y,num_antenati_y):
	risultato[nodo] = num_antenati_y
	num_antenati_y += len(dizionario[nodo]) == y
	for figlio in dizionario[nodo]:
		gen_gradi(figlio,dizionario,risultato,y,num_antenati_y)
	
def get_root(json_stringa):
	clean = "".join([[' ',carattere][carattere.isalpha()] for carattere in json_stringa])
	return Counter(clean.split()).most_common()[-1][0]
	
	
	
	
	
	
	





