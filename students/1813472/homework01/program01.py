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


def modi(ls,k):
	Lista_k=[]
	Lista_numeri_primi=[]
	for x in ls:
		s=fattori(x)
		long=len(s)
		if long==k:
			Lista_k.append(x)
		elif long==0:
			Lista_numeri_primi.append(x)
	ls[:]=Lista_k
	return Lista_numeri_primi

from math import sqrt

def fattori(x):
        fattori=[]
        for y in range(2, int(sqrt(x))+1):
                if x%y==0:
                        fattori.append(y)
                        fattori.append(x//y)
        return fattori
