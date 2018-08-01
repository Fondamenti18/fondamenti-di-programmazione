'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[441,16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

import math
def modi(ls,k):
	primi=[]
	lista=[]
	for l in ls:
		c=2
		primo=True
		divisori=[]
		divisori2=[]
		for n in range (2,(l//c)+1):
			if l//n>=(math.sqrt(l)):
				if l%n==0:
					primo=False
					divisori+=[n]
			else:
				break;
			c+=1
			divisori2=list(divisori)
		for n in divisori:
			if not l/n in divisori:
				divisori2+=[int(l/n)]
		if primo:
			primi+=[l]
		elif len(divisori2)==k:
			lista+=[l]
	ls[:]=list(lista)
	return primi
	
	