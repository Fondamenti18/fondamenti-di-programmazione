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

from json import *
#funzioni ausiliari 

def genera_albero(dl,f,x):
	dl[x]=f[x]
	for x in dl[x]:
		genera_albero(dl,f,x)
	return dl

def find_rad(f): #trova la radice dell'albero
	insrad=set()
	insfig=set()
	for x in f: #insieme delle possibili radici
		insrad.add(x)
		for ch in f[x]:
			insfig.add(ch) #insieme di tutti i figli di un qualche nodo
	radic=insrad-insfig #radice
	#print(radic)
	return radic.pop()

def check_lvl(f,nodo,h=0,dl={}): #controlla il lvl di ognuno dei nodi
	#print(dl,'funzione aux')
	if f == {}: return dl #se il file è vuoto 
	if h not in dl: dl[h] = [nodo] #se l'altezza non è presente nel dizionario
	else: dl[h].append(nodo) #se è presente aggiungo l'elemento nel dizionario
	for x in f[nodo]: #per ogni nodo presente nel file
		check_lvl(f,x,h+1,dl) 
	return dl

def check_ant(f,nodo,grado,dl={},count=0): #controllo il grado degli antenati 
	if f=={}: return dl #se il file è vuoto
	dl[nodo]=count #aggiungo il contatore al nodo
	if len(f[nodo]) == grado: count += 1 #aumento in counter nel caso in cui il nodo abbia tot figli
	for x in f[nodo]:
		check_ant(f,x,grado,dl,count) #effettuo la ricorsione
	return dl

#funzioni principali

def genera_sottoalbero(fnome,x,fout):
	with open (fnome) as file1:
		f1=load(file1)
	dl={}
	genera_albero(dl,f1,x)
	f1c=open(fout,'w')
	dump(dl,f1c)
	f1c.close()
	#ricordati di salvare il file!! <- todo
	return

def cancella_sottoalbero(fnome,x,fout):
	with open (fnome) as file2:
		f2=load(file2)
	dl={}
	genera_albero(dl,f2,x)
	#print(dl)
	for k in dl:
		del f2[k]
	for v in f2:
		if x in f2[v] :
			f2[v].remove(x)
			break
	f2c=open(fout,'w')
	dump(f2,f2c)
	f2c.close()
	#ricordati di salvare il file!! <- todo
	return

def dizionario_livelli(fnome,fout):
	with open(fnome) as file3: #apro il file fnome
		f3=load(file3) #lo carico in f3
		#print(f3)
		#print(f3)
	dl={} #riazzero dl (non serve ma non capivo quale fosse il problema e quindi l'ho azzerato)
	#print(dl,' funzione principale')
	rad=find_rad(f3) #trovo la radice
	dl=check_lvl(f3,rad,0,dl) #mi cerco i livelli 
	for x in dl:  #riordino la lista in ordine crescente
		dl[x] = sorted(dl[x])

	f3c=open(fout,'w')  #salvo il file 
	dump(dl,f3c)
	f3c.close()
	return

def dizionario_gradi_antenati(fnome,y,fout):
	with open(fnome) as file4: 
		f4=load(file4)
		#print(f)
	rad=find_rad(f4)
	#print(y)
	dl={}
	dl=check_ant(f4,rad,y,dl) #controllo il grado 
	#print(dl)
	f4c=open(fout,'w') #salvo il file 
	dump(dl,f4c)
	f4c.close()
	return