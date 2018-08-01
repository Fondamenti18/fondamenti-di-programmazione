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




from json import load
import json
from collections import defaultdict


def generazione(dizionarioFinale, listaDaCercare, dizionarioIniziale):
	nuovaLista = []
	for key in listaDaCercare:
		dizionarioFinale[key] = dizionarioIniziale[key]
		nuovaLista += dizionarioIniziale[key]
	if(nuovaLista != []):
		generazione(dizionarioFinale, nuovaLista, dizionarioIniziale)
	
def pulisciDizionario(dizionarioEliminazione, listaDaEliminare, nuovoDizionario):
	nuovaLista = []
	for key in dizionarioEliminazione:
		for chiave in listaDaEliminare:
			nuovaLista = [c for c in dizionarioEliminazione[key] if c != chiave]
		nuovoDizionario[key] = nuovaLista
			
def eliminaElementi(dizionarioEliminazione, listaDaEliminare):
	nuovaLista = []
	for key in listaDaEliminare:
		nuovaLista += dizionarioEliminazione[key]
		dizionarioEliminazione.pop(key)
	if(nuovaLista != []):	
		eliminaElementi(dizionarioEliminazione, nuovaLista)
		
def creaNuovoDizionario(dizionarioIniziale, listaDaCostruire, nuovoDizionario, valoreIntero):
	nuovaLista = []
	for elemento in listaDaCostruire:
		if dizionarioIniziale[elemento] != []:
			if(nuovoDizionario.get(str(valoreIntero)) == None):
				nuovoDizionario[str(valoreIntero)] = []
			nuovoDizionario[str(valoreIntero)] += sorted(dizionarioIniziale[elemento])
			nuovaLista += dizionarioIniziale[elemento]
	if(nuovaLista != []):
		nuovoDizionario[str(valoreIntero)] = sorted(nuovoDizionario[str(valoreIntero)])
		valoreIntero+=1
		creaNuovoDizionario(dizionarioIniziale, nuovaLista, nuovoDizionario, valoreIntero)


def GradiAntenatiDizionario(fileGeneraGradiAntenati, numeroGrado, chiave, numeroYGrado, nuovoDizionario, chiaveIniziale):
	for key, values in fileGeneraGradiAntenati.items():
		if(chiave in values):
			if(len(values) == numeroGrado):
				nuovoDizionario[chiaveIniziale] += 1
			GradiAntenatiDizionario(fileGeneraGradiAntenati, numeroGrado, key, numeroYGrado, nuovoDizionario, chiaveIniziale)
 
	
def genera_sottoalbero(fnome,x,fout):
	dizionarioFinale = dict()
	listaDaCercare = [x]
	with open(fnome) as file:
		fileGenerazione = load(file)
	generazione(dizionarioFinale, listaDaCercare, fileGenerazione )
	with open(fout, 'w') as fileOutput:
		json.dump(dizionarioFinale, fileOutput)
		
def cancella_sottoalbero(fnome,x,fout):
	listaDaEliminare = [x]
	nuovoDizionario = dict()
	with open(fnome) as file:
		fileEliminazione = load(file)
	eliminaElementi(fileEliminazione, listaDaEliminare)
	pulisciDizionario(fileEliminazione, listaDaEliminare, nuovoDizionario)
	with open(fout, 'w') as fileOutput:
		json.dump(nuovoDizionario, fileOutput)

def dizionario_livelli(fnome,fout):
	nuovoDizionario = dict()
	Intero = 1
	with open(fnome) as file:
		fileRistrutturazione = load(file)
	primoValore = PrimoValore(fileRistrutturazione)
	nuovoDizionario["0"] = [primoValore]
	listaDaUsare = [primoValore]
	creaNuovoDizionario(fileRistrutturazione, listaDaUsare, nuovoDizionario, Intero)
	with open(fout, 'w') as fileOutput:
		json.dump(nuovoDizionario, fileOutput)
 
def creaLista(dizionarioRibaltato, lista, elemento, elementoIniziale):
		if(elemento != ['0']):
			if(elemento != elementoIniziale):
				lista+=[elemento]
			creaLista(dizionarioRibaltato, lista, dizionarioRibaltato[elemento], elementoIniziale)
			
def PrimoValore(fileIniziale):
	listaValori = {valore for valore in fileIniziale.values() for valore in valore}
	primoValore = [elemento for elemento in fileIniziale if elemento not in listaValori]
	primoValore = primoValore[0]
	return primoValore
		
def dizionario_gradi_antenati(fnome,y,fout):
	nuovoDizionario = dict()
	dizionarioFinale = dict()
	with open(fnome) as file:
		fileGeneraGradiAntenati = load(file)
	primoValore = PrimoValore(fileGeneraGradiAntenati)
	for key, value in fileGeneraGradiAntenati.items():
		for element in value:
			nuovoDizionario[element] = key 
	nuovoDizionario[primoValore] = ['0']
	for elemento in nuovoDizionario:
		lista = []
		contatore = 0
		creaLista(nuovoDizionario, lista, elemento, elemento)
		for c in lista:
			if(len(fileGeneraGradiAntenati[c]) == y):
				contatore += 1
		dizionarioFinale[elemento] = contatore
	with open(fout, 'w') as fileOutput:
		json.dump(dizionarioFinale, fileOutput)
				
		
		
dizionario_livelli('Alb50000.json','tAlb50000_4.json')
	
	