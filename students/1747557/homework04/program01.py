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
import collections

def apri(fnome):
	with open(fnome) as f:
		diz_albero=json.load(f)
	return diz_albero

def salva(fout, data):
	#print('sto salvando in :   ', fout)
	with open(fout, 'w') as f:
		json.dump(data, f)
	
def leggi_sottoalbero(albero, sottoalbero, x ):
	valore = albero.get(x)
	if valore== None:
		return 
	if valore== []:
		sottoalbero[x]= valore
	else:
		sottoalbero[x]= valore
		for i in valore:
			leggi_sottoalbero(albero, sottoalbero, i)
	

	
def stampaAlbero(diz, nodo):
	#print('nodo = ',nodo)
	valore = diz.get(nodo)
	if valore == []:
		return
	for i in valore:		
		stampaAlbero(diz,i)		

def contaNodi(diz, nodo):

	count = 1
	valore = diz.get(nodo)
	for i in valore:		
		count+= contaNodi(diz,i)
	return count;


def updateDaEvitare(diz,key,daEvitare):
	valore = diz.get(key)
	daEvitare.append(key)
	if valore == []:
		return
	for i in valore:		
		updateDaEvitare(diz,i,daEvitare)	

def fixLivelli(diz,x,livelli,h):
	if h not in livelli:
		livelli[h] = [x]
	else:
		livelli[h].append(x)
	for i in diz.get(x):
		fixLivelli(diz,i,livelli,h+1)



def trovaradice(diz):
	#stampaAlbero(diz,'a')
	daEvitare = []
	totaleNodi = len(diz.keys())
	for key in diz.keys():
		if key in daEvitare:
			continue
		subtot = contaNodi(diz,key)
		if(subtot == totaleNodi):
			return key
		else:
			updateDaEvitare(diz,key,daEvitare)

	
		
	
	
def genera_sottoalbero(fnome,x,fout):
	'''inserire qui il vostro codice'''
	
	diz=apri(fnome)
	
	sottoalbero={}
	leggi_sottoalbero(diz, sottoalbero, x)
	
	salva(fout, sottoalbero)
	
def cancella(diz, x):
	sottoalbero={}
	leggi_sottoalbero(diz, sottoalbero, x)
	
	for key in sottoalbero.keys():
		diz.pop(key, None)
	for key in diz.keys():
		if x in diz.get(key):
			diz.get(key).remove(x)
	

def cancella_sottoalbero(fnome,x,fout):
	'''inserire qui il vostro codice'''
	
	diz=apri(fnome)
	sottoalbero={}
	leggi_sottoalbero(diz, sottoalbero, x)
	
	for key in sottoalbero.keys():
		diz.pop(key, None)
	for key in diz.keys():
		if x in diz.get(key):
			diz.get(key).remove(x)
	
	
	
	salva(fout, diz)

	
	
	
def dizionario_livelli(fnome,fout):
	'''inserire qui il vostro codice'''
	diz=apri(fnome)
	radice = trovaradice(diz)
	livelli = {}
	livelli[0] = [radice];
	for key in diz.get(radice):
		fixLivelli(diz,key,livelli,1)
	for key in livelli:
		livelli.get(key).sort()
	#print('DIZ = ',diz);
	#print('RADICE = ',radice)
	#print('LIVELLI = ',livelli)
	
	salva(fout, livelli)
	

def propagaAntenati(diz, antenati, x):
	if x not in antenati:
		antenati[x]=1
	else:
		antenati[x] +=1
	for  i in diz.get(x):
		propagaAntenati(diz, antenati, i)
		
	
	
def fixAntenati(diz, antenati, x, k):
	#print('k = ',k)
	#print('figli di ',x,' sono  ',len(diz.get(x)))
	if len(diz.get(x))==k:
		for i in diz.get(x):
			if x not in antenati:
				antenati[x]=0
			propagaAntenati(diz, antenati, i)
	else:
		if x not in antenati:
			antenati[x]=0
	for i in diz.get(x):
		fixAntenati(diz, antenati, i, k)
		

	
 

def dizionario_gradi_antenati(fnome,y,fout):
	'''inserire qui il vostro codice'''
	diz=apri(fnome)
	radice = trovaradice(diz)
	antenati={}
	antenati[radice]=0
	'''
	for i in diz.get(radice):
		propagaAntenati(diz,antenati,i)
	for i in diz.get('d'):
		propagaAntenati(diz,antenati,i)
	'''
	#for i in diz.get(radice):
	fixAntenati(diz, antenati, radice, y)
	
	
	#antenati = collections.OrderedDict(sorted(antenati.items()))


	orderedKeys = sorted(antenati)
	#print('ORDERED KEYS === ',orderedKeys)
	antenatiOrdinati = []
	for key in orderedKeys:
		#print('STO INSERENDO LA KEY ',key)
		antenatiOrdinati.append((key,antenati[key]))
	d  =dict(antenatiOrdinati)
	#print('ANTENARI BELLAMENTE ORDINATI  === ', d)
	#print('DIZ = ',diz);
	#print('RADICE = ',radice)
	
	
	salva(fout, d)

	
	
	
'''	

diz=apri('Alb20000.json')
radice = trovaradice(diz)
antenati={}
antenati[radice]=0
for i in diz.get(radice):
	fixAntenati(diz, antenati, i, 2)


#antenati = collections.OrderedDict(sorted(antenati.items()))


orderedKeys = sorted(antenati)
#print('ORDERED KEYS === ',orderedKeys)
antenatiOrdinati = []
for key in orderedKeys:
	#print('STO INSERENDO LA KEY ',key)
	antenatiOrdinati.append((key,antenati[key]))
d  =dict(antenatiOrdinati)
#print('ANTENARI BELLAMENTE ORDINATI  === ', d)
#print('DIZ = ',diz);
print('RADICE = ',radice)

soluzione = apri('risAlb20000_4.json')

ok = True
for key in d:
	if key not in soluzione:
		print('KEY ',key,' non e nella soluzione!!!!!')
		ok = False;
		break;
	else:
		if d[key] != soluzione[key]:
			print('OH NO DIFFERENZA!!!', d[key], '  !=   ',soluzione[key])
			ok = False
			
print('RISUTATO = ',ok)

'''

