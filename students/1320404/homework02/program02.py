'''
Un  file di compiti contiene  informazioni su un insieme  di compiti da eseguire.
Esistono  due tipologie di compiti:
- compiti che possono essere eseguiti indipendentemente dagli altri.
- compiti da svolgere  solo al termine di un compito preliminare.
I compiti del primo tipo sono codificati nel file mediante una linea che contiene
in sequenza le due sottostringhe "comp" ed "N" (senza virgolette) eventualmente inframmezzate, 
precedute e/o seguite da  spazi. "N" e' l'ID del compito (un numero positivo).
Compiti del secondo tipo sono codificati nel file mediante due linee di codice.
-- la prima  linea,  contiene in sequenza le due sottostringhe "comp" ed "N" 
(senza virgolette) eventualmente inframmezzate, 
precedute e/o seguite da  spazi. "N" e' l'ID del compito (un numero positivo).
-- la seconda linea (immediatamente successiva nel file) contiene 
in sequenza le due sottostringhe "sub" ed "M" (senza virgolette) eventualmente inframmezzate, 
precedute e/o seguite da  spazi. "M" e' l'ID del compito preliminare.

il seguente file di compiti contiene informazioni su 4 compiti (con identificativi 1,3,7 e 9). 
I compiti con identificativi 1 e 9 possono essere svolti indipendentemente dagli altri mentre i compiti 
con identificativo 3 e 7 hanno entrambi un compito preliminare.

comp 3
 sub 9
        comp1
comp              9
    comp 7
sub3

Scrivere la funzione pianifica(fcompiti,insi,fout) che prende in input:
- il percorso di un file (fcompiti) 
- un insieme  di ID di compiti da cercare (insi)
- ed il percorso di un file (fout) 
e che salva in formato JSON nel file fout un dizionario (risultato).

Il dizionario (risultato) dovra' contenere come chiavi gli identificativi (ID) dei compiti 
presenti in fcompiti e richiesti nell'insieme insi.
Associata ad ogni ID x del dizionario deve esserci una lista contenente  gli identificativi (ID) dei compiti 
che bisogna eseguire prima di poter eseguire il compito x richiesto
(ovviamente la lista di un ID di un compito che non richie un compito preliminare risultera' vuota ). 
Gli (ID) devono comparire nella lista nell'ordine di esecuzione corretto, dal primo fino a quello precedente a quello richiesto 
(ovviamente il primo ID di una lista non vuota corripondera' sempre ad un compito che non richiede un compito preliminare). 


Si puo' assumere che:
 - se l' ID di un compito che richieda un compito preliminare e' presente  in fcompiti 
    allora anche l'ID di quest'ultimo e' presente in fcompiti
 - la sequenza da associare al compito ID del dizionario esiste sempre
 - non esistono cicli (compiti che richiedono se' stessi anche indirettamente)


Ad esempio per il file di compiti  fcompiti contenente:

comp 3
 sub 9
        comp1
comp              9
    comp 7
sub3

al termine dell'esecuzione di  pianifica(fcompiti,{'7','1','5'}, 'a.json')
il file 'a.json' deve contenere il seguente dizionario
{'7':['9','3'],'1':[]}


Per altri esempi vedere il file grade02.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''

import json
        
def pianifica(fcompiti,insi,fout):
	rub={}
	chiave={}
	valore=[]
	var=''
	v=[]
	
	with open(fcompiti, 'rU') as f:
		testo=f.read()
		testo=testo.splitlines()
		for i in range(0,len(testo)):
			var1=testo[i]
			for j in range(0,len(var1)):
				if var1[j] == ' ':
					continue
				else:
					var=var+var1[j]
		
		var=var.split('comp')
		for i in range(1,len(var)):
			var1=var[i]
			var1=var1.split('sub')
			if len(var1) > 1:
				rub[var1[0]]=var1[1]
			else:
				rub[var1[0]]=''
		
		for x in insi:
			v=v+[x]
		
		for i in range(0,len(v)):
			key=[v[i]]
			test=v[i]
			if test in rub:
				chiave[v[i]]=eseg(rub,key)
			
	c=str(chiave)
	c=c.replace('\'','\"')
	
	
	with open(fout, 'w') as out:
		out.write(c)
		
				
	
		
def eseg(rub,insi):
	v=[]
	ris=[]
	for x in insi:
		v=v+[x]
	for i in range(0,len(v)):
		a=v[i]
		while rub[a] != '':
			ris=ris+[rub[a]]
			a=rub[a]
	
	ris=ris[::-1]
	return ris
	
	
	
	
	
	
