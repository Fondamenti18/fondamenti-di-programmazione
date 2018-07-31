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

def apri(fnome):
    with open(fnome, 'r') as f:
        return json.load(f)

def sottoalbero(d,x,diz):
	 
	for el in x:
		diz[el]=d[el]
		diz=sottoalbero(d,d[el],diz)
	return diz  
                       
def genera_sottoalbero1(fnome,x):
		'''if sys.getrecursionlimit()<2200:
			sys.setrecursionlimit(2200)'''
		d=apri(fnome)
		
		diz={}
		diz.setdefault(x)
		diz[x]=d[x]
		diz=sottoalbero(d,d[x],diz)
		
		return diz
    
def genera_sottoalbero(fnome,x,fout):
    
    with open(fout, 'w') as z:
        json.dump(genera_sottoalbero1(fnome,x),z)
        
		    

def cancella_sottoalbero(fnome,x,fout):
    
	d=apri(fnome)
	diz={}
	diz.setdefault(x)
	diz[x]=d[x]
	diz=genera_sottoalbero1(fnome, x)
	for el in diz:
		d.pop(el)
	for el in d:
		if x in d[el]:
			d[el].remove(x)
	with open(fout, 'w') as file:
		json.dump(d,file)
def lista(diz):
    x=[]
    f=[]
    l=[]
    for chiave in diz:
        for a in diz:
            if chiave in diz[a]:
                l.append(chiave)
    for b in diz.keys():
        f.append(b)
    for c in f:
        if c not in l:
            x.append(c)
    return x

def level(diz, x, livello=0):
	if not x:
		return {}
	d={}
	l=[]
	for el in x:
		d.setdefault(livello,[]).append(el)
		l.extend(diz.get(el,[]))
	d.update(level(diz,l,livello+1))
	for el in d:
		d[el]=sorted(d[el])
	return d

'''def dizionario_livelli1(diz):
	x=lista(diz)
	livello=0
	d={}
	d.update(level(diz, x, livello))
	for el in d:
		d[el]=sorted(d[el])
	return d'''

    


def dizionario_livelli(fnome,fout):
    diz=apri(fnome)
    with open(fout, 'w') as salve:
        json.dump(level(diz,lista(diz)),salve)
 

def dizionario_gradi_antenati(fnome,y,fout):
	with open(fout, 'w') as z:
		diz={}
		dizalb=apri(fnome)
		for b in dizalb.keys():
			conta=0
			conta=conta_avi(b,conta,dizalb,y)
			diz[b]=conta
			 
		json.dump(diz,z)
 
def conta_avi(b,conta,dizalb,y):
	for c in dizalb.keys():
		if b in dizalb[c]:
			if len(dizalb[c])==y:
				conta=conta+1
			conta=conta_avi(c,conta,dizalb,y)
			break
	return conta	
