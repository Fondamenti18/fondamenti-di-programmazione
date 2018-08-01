'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''
from math import sqrt

def modi(ls,k):
	primi=[]
	i=0
	dim=len(ls)
	while i<dim:
		#visto che andrò a cancellare gli elemtni direttamente dalla lista di partenza, un ciclo for non è
		#mi permette di lavorare completamente con una lista in continuo cambiamento, visto i pop successivi
		n=ls[i]
		cont=0
		root=round(sqrt(n))
		#per "alleggerire" i numeri piu grandi si puo lavorare direttamente con la loro radice quadrata
		#cosi facendo appena si trova un divisore, il contatore dei div. si incrementerà di due 
		for a in range(2,root+1):
			if n%a==0:
				cont+=2
			if cont>k:
				#inutile continuare de il contatore supera k che è il nostro "limite" massimo dei divisori
				break
		if cont==0:
			#se il cont rimane a 0 vorrà dire che il numero è primo
			primi+=[n]
		if cont!=k:
			#se invece il cont è diverso da K, il numero verrà eliminato dalla lista originale
			ls.pop(i)
			dim=dim-1
		else:
			i+=1

	return primi