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

def leggi(path):
	with open(path, 'r') as f:
		return json.load(f)

def scrivi(path, a):
	with open(path, 'w') as f1:
		json.dump(a, f1)

def genera_sottoalbero(fnome, x, fout):
	albero = leggi(fnome)
	if x not in albero.keys():
		return {}
	scrivi(fout, gen(albero, {}, x))
		
def gen(old, new, x):
	new[x] = old[x]
	for i in old[x]:
		new = gen(old, new, i)
	return new

def cancella_sottoalbero(fnome, x, fout):
	albero = leggi(fnome)
	if x not in albero.keys():
		return albero
	albero = canc(albero, x)
	scrivi(fout, elemento(albero, x))
	
def canc(alb, elem):
	for i in alb[elem]:
		canc(alb, i)
	del alb[elem]
	return alb

def elemento(al, el):
	for i in al.keys():
		if el in al[i]:
			al[i].remove(el)
			break
	return al	

def altezza(albero, radice):
	l = []
	if not albero[radice]:
		return 0
	for i in albero[radice]:
		l += [altezza(albero, i)]
	return 1 + max(l)
	
def dizionario_livelli(fnome, fout):
	albero = leggi(fnome)
	testa = trovaradice(albero)
	dlvl = {}
	for i in range(altezza(albero, testa) + 1):
		dlvl[str(i)] = []
	dlvl = gendlvl(albero, dlvl, testa, 0)
	scrivi(fout, ordina(dlvl))
  
def gendlvl(albero, dictlvl, radice, lvl):
	dictlvl[str(lvl)] += [radice]
	if not albero[radice]:
		return dictlvl
	for i in albero[radice]:
		dictlvl = gendlvl(albero, dictlvl, i, lvl+1)
	return dictlvl

def ordina(d):
	for i in d.keys():
		d[i].sort()
	return d
 
def dizionario_gradi_antenati(fnome, y, fout):
	albero = leggi(fnome)
	radice = trovaradice(albero)
	scrivi(fout, gradi(albero, radice, {}, y, 0))

def gradi(albero, radice, d, y, lvl):
	d[radice] = lvl
	if not albero[radice]:
		return d
	ad = 0
	if len(albero[radice]) == y:
		ad = 1
	for i in albero[radice]:
		d = gradi(albero, i, d, y, d[radice] + ad)
	return d
	
def trovaradice(albero):
	for i in albero.keys():
		a = True
		for j in albero.keys():
			a = a and (i not in albero[j])
		if a: 
			return i
