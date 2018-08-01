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
genera_sottoalbero('Alb10.json','d','tAlb10_1.json')'''




import json
d={}
risultato={}

def genera_sottoalbero(fnome,x,fout):
	with open (fnome) as dati:
		global d
		global risultato
		risultato={}
		d=json.load(dati)
		ricerca(x)
		with open(fout,'w') as out:
			json.dump(risultato,out)

			

def ricerca(chiave):
	global d
	global risultato	
	risultato[chiave]=d[chiave]
	if d[chiave]!=[]:
		for i in d[chiave]:
			ricerca(i)

			

def cancella_sottoalbero(fnome,x,fout):
	with open (fnome) as dati:
		global d
		global risultato
		risultato={}
		d=json.load(dati)
		ricerca(x)
		
		for key in risultato.keys():
			del d[key]
		for i in d.keys():
			if x in d[i]:
				d[i].remove(x)
				
		with open(fout,'w') as out:			
			json.dump(d,out)

			
    

def dizionario_livelli(fnome,fout):
	with open (fnome) as dati:
		global d
		global risultato
		risultato={}
		d=json.load(dati)
		#trova il primo elemento con sottrazione tra insieme
		set1=set(d.keys())
		elementi=[]
		for i in d.values():
			for j in i:
				elementi.append(j)

		set2=set(elementi)
		inizio=set1-set2		
		risultato[0]=list(inizio)
		#trovata la radice si ricava facilmente il resto
		livello(1)
		with open(fout,'w') as out:
			json.dump(risultato,out)

			

def livello (count):
	global d
	global risultato
	trovato=False
	now=[]
	for x in risultato[count-1]:
		if d[x]!= []:

			now=now+d[x]
			trovato=True
	if trovato:
		now.sort()
		risultato[count]=now
		livello(count+1)


		
yy=0

def dizionario_gradi_antenati(fnome,y,fout):
	#stesso inizio di dizionario_livelli
	with open (fnome) as dati:
		global d
		global risultato
		global yy
		yy=y
		risultato={}
		d=json.load(dati)
		set1=set(d.keys())
		elementi=[]
		for i in d.values():
			for j in i:
				elementi.append(j)

		set2=set(elementi)
		inizio=set1-set2
		l=list(inizio)
		risultato[l[0]]=0
		
		gradi(l[0],0)
		with open(fout,'w') as out:
			json.dump(risultato,out)

			

def gradi(chiave,genitori):
	global d
	global risultato
	global yy	
	if len(d[chiave])==yy:
		genitori+=1
	for i in d[chiave]:		
		risultato[i]=genitori
		gradi(i,genitori)
		
