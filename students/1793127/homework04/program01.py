# -*- coding: utf-8 -*-
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
	with open(fnome) as f:
		dati={}
		diz=json.load(f)
		dati=genera_ric(x,dati,diz)
		with open(fout,'w') as f:
			json.dump(dati,f)

def genera_ric(a,dat,diz):
	m=0
	dat[a]=diz[a]
	while m<len(diz[a]):
		dat=genera_ric((diz[a])[m],dat,diz)
		m+=1
	return dat

def cancella_sottoalbero(fnome,x,fout):
	with open(fnome) as f:
		diz=json.load(f)
		dat=diz.copy()
		m=0
		for chiave in diz:
			if x in diz[chiave]:
				while m<len(diz[chiave]):
					if (diz[chiave])[m]==x:
						del (diz[chiave])[m]
						break
					m+=1
				break
		diz=elimina_ric(x,diz,dat)
		with open(fout,'w') as f:
			json.dump(diz,f)

def elimina_ric(x,diz,dat):
	m=0
	del diz[x]
	while m<len(dat[x]):
		diz=elimina_ric((dat[x])[m],diz,dat)
		m+=1
	return diz

def dizionario_livelli(fnome,fout):
	with open(fnome) as f:
		diz=json.load(f)
		dlv={}
		lst=[]
		radice=ottieni_radice(diz)
		dlv=check_level(diz,radice,lst,dlv)
		with open(fout,'w') as f:
			json.dump(dlv,f)

def check_level(d,r,l,dlv):
	if r!=[]:
		l.append(r)
	m=0
	q=[]
	while m<len(r):
		for a in d[(r[m])]:
			q.append(a)
		m+=1
		if m==len(r):
			check_level(d,q,l,dlv)
	m=0
	while m<len(l):
		l[m].sort()
		m+=1
	m=0
	while m<len(l):
		dlv[m]=l[m]
		m+=1
	return dlv

def ottieni_radice(diz):
	for chiave in diz:
		rand=chiave
		break
	rad=0
	rad=ric_rad(rand,diz)
	return [rad]

def ric_rad(rand,diz):
	for chiave in diz:
		if rand in diz[chiave]:
			rand=ric_rad(chiave,diz)
	return rand

def dizionario_gradi_antenati(fnome,y,fout):
	with open(fnome) as f:
		diz=json.load(f)
		d={}
		n=0
		rad=ottieni_radice(diz)
		r=rad[0]
		d=calc_ant_grad(r,diz,d,n)
		with open(fout,'w') as f:
			json.dump(d,f)

def calc_ant_grad(r,diz,d,n):
	m=0
	d[r]=n
	while m<len(diz[r]):
		if len(diz[r])==2 and m==0:
			n+=1
		d=calc_ant_grad((diz[r])[m],diz,d,n)
		m+=1
	return d
