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

import math


def modi(ls,k):
	
	darimuovere=[]
	
	listaoriginale= ls.copy()
	for el in ls:
		if divisoreproprio(el)!=k:
			darimuovere.append(el)
	for e in darimuovere:
		ls.remove(e)
	print(ls)
	for e in listaoriginale:
		return numeriprimi(listaoriginale)
	
	
	
	

	
    	
		
		

def numeriprimi(ls):
    L=[]
    for el in ls:
	    if divisoreproprio(el)==0:
	        L.append(el)
    return L
        	
	

	
	
def divisoreproprio(n):
	N=0
	for i in range(2,(round(math.sqrt(n)))):
		if n%i==0:
			N+=2
	return N	
	
"inserite qui il vostro codice"
	
#ls=[70,330,293,154,128,113,178]
#print(modi(ls,6))