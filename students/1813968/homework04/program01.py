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
dizionario={}
dizionario2={}
dizionario3={}

def apri_file(fnome):
	global dizionario
	with open(fnome,"r") as f:
		dizionario = json.load(f)

def salva_file(fnome):
	global dizionario2
	with open(fnome, 'w') as f:
		json.dump(dizionario2, f)

def genera_sottoalbero(fnome,x,fout):
	global dizionario,dizionario2
	dizionario={}
	dizionario2={}
	apri_file(fnome)
	c=[]
	c=[x]
	genera_sottoalbero2(c)
	salva_file(fout)

def genera_sottoalbero2(x):
	global dizionario,dizionario2
	for i in x:
		if i in dizionario:
			lista=dizionario[i]
			dizionario2[i]=lista
			genera_sottoalbero2(lista)

def cancella_sottoalbero(fnome,x,fout):
	global dizionario,dizionario2
	dizionario={}
	dizionario2={}
	apri_file(fnome)
	dizionario2=dizionario.copy()
	c=[]
	c=[x]
	cancella_sottoalbero2(c)
	cancella_sottoalbero3(x)
	salva_file(fout)
    
def cancella_sottoalbero2(x):
	global dizionario,dizionario2
	for i in x:
		if i in dizionario:
			lista=dizionario2.pop(i)
			cancella_sottoalbero2(lista)

def cancella_sottoalbero3(x):
	global dizionario2
	for i in dizionario2:
		if x in dizionario2[i]:
			del dizionario2[i][dizionario2[i].index(x)]
		
def dizionario_livelli(fnome,fout):
	global dizionario,dizionario2,dizionario3
	dizionario={}
	dizionario2={}
	dizionario3={}
	apri_file(fnome)
	lista=[]
	lista=radice_dellalbero(lista)
	dizionario2[lista[0]]=0
	dizionario3=inverti_dizionario1(dizionario)
	dizionario_livelli2(lista)
	dizionario2=inverti_dizionario2(dizionario2)
	ordinamento_valori()
	salva_file(fout)

def radice_dellalbero(lista):
	global dizionario
	a=set(dizionario.keys())
	for i in dizionario.values():
		for c in i:
			lista.append(c)
	b=set(lista)
	c=a-b
	lista=list(c)
	return lista
	
def dizionario_livelli2(list):
	global dizionario,dizionario2,dizionario3
	lista=[]
	for i in list:
		for c in dizionario[i]:
			dizionario2[c]=(dizionario2[dizionario3[c]])+1
			if len(dizionario[i])==dizionario[i].index(c)+1:
				lista=dizionario[i]
				dizionario_livelli2(lista)
	
def ordinamento_valori():
	for i in dizionario2:
		dizionario2[i].sort()
  
def inverti_dizionario1(dizi):
	dizi2={}
	for i in dizi:
		if dizi[i]!=[]:
			for x in dizi[i]:
				dizi2[x]=i
	return dizi2

def inverti_dizionario2(dizi):
	dizi2={}
	for i in dizi:
		if not dizi[i] in dizi2.keys():
			dizi2[dizi[i]]=[i]
		else:
			dizi2[dizi[i]]+=[i]
	return dizi2
	
def dizionario_gradi_antenati(fnome,y,fout):
	global dizionario,dizionario2
	dizionario={}
	dizionario2={}
	apri_file(fnome)
	cont=0
	q=set()
	lista=[]
	l=[]
	lista=radice_dellalbero(lista)
	l=controllo(y)
	dizionario2[lista[cont]]=cont
	dizionario_gradi_antenati2(lista[cont],cont,l)
	salva_file(fout)
	
def dizionario_gradi_antenati2(x,cont,lista):
	global dizionario2
	if x in lista:
		cont=cont+1
	for i in dizionario[x]:
		dizionario2[i]=cont
		dizionario_gradi_antenati2(i,cont,lista)
			
def controllo(y):
	lista=[]
	for i in dizionario:
		if len(dizionario[i])==y:
			lista.append(i)
	return lista
	
