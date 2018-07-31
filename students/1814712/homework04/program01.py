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




import json


def genera_sottoalbero(fnome,x,fout):
	d = open(fnome,'r')
	s = json.load(d)
	d1 = {}
	d1 = ricorsione(s,x,d1)
	with open(fout, 'w') as outfile:
		json.dump(d1,outfile)
	  
	

def ricorsione(s,x,d1):
	if x not in s:
		return d1
	else:
		d1.update({x : s[x]})
		for i in s[x]:
			ricorsione(s,i,d1)
		return d1
		
def cancella_sottoalbero(fnome,x,fout):
	d = open(fnome,'r')
	s = json.load(d)
	ricorsione_canc(s,x)
	for i in s.keys() :
		if x in s[i] :
			s[i].remove(x)
	with open(fout, 'w') as outfile:
		json.dump(s,outfile)	
	
	
def ricorsione_canc(s,x):
	if x not in s:
		return
	else:
		for i in s[x]:
			ricorsione_canc(s,i)
		del s[x]
		return
		
		
def dizionario_livelli(fnome, fout):
	d = open(fnome,'r')
	s = json.load(d)
	k = list(s.keys())
	d1 = {0 : [k[0]]}
	l = 1
	ricorsione_liv(s,l,d1)
	with open(fout, 'w') as outfile:
		json.dump(d1,outfile)
	


def ricorsione_liv(s,l,d1):
	l_app = []
	for i in d1[l-1]:
		l_app = l_app + s[i]
	if len(l_app) == 0:
		return
	else :
		d1.update({l : sorted(l_app)})
		ricorsione_liv(s, l+1 , d1)
	return
	
	
	
def dizionario_gradi_antenati(fnome,y,fout):
	d = open(fnome,'r')
	s = json.load(d)
	k = list(s.keys())
	d1 = {i : 0 for i in k}
	ricorsione_ant(s,d1,k[0],y)
	with open(fout, 'w') as outfile:
		json.dump(d1,outfile)


def ricorsione_ant(s,d1,x,y):
	n = len(s[x])
	if n == 0:
		return
	for i in s[x]:
		if n == y:
			d1[i] = d1[x]+1
		else:
			d1[i] =	d1[x]
	for i in s[x] :
		ricorsione_ant(s,d1,i,y)
	return
	

	
	
	
		



	
	
	
		
	
	
    
    

