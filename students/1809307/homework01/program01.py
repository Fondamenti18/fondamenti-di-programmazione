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
	lista1=[]
	lista2=[]
	for x in ls:
		d=0
		for b in range(2,int( x**0.5)+1):
			if x%b==0:
				d=d+2
				if x==x**0.5:
					d=d+1
                                
				if d>k:
					break
		if d==0:
			lista1=lista1+[x]
		elif d==k:
			lista2=lista2+[x]
	ls.clear()
	ls+=lista2
	
	return lista1

		
	
			
				
		
	
