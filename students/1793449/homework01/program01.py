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
	primi = []
	l = []
	#Eseguo un for per ogni elemento n di ls
	for n in ls:
		prime = True
		#Escludo i numeri minori di 2
		if n < 2:
			prime = False
		#Per tutti gli altri numeri eseguo un for che va da 2 (escluso) alla radice di n + 1
		else:
			divisors = set()
			for a in range(2,int(n**0.5) + 1):
				if not n % a:
					prime = False
					div, mod = divmod(n, a)
					if mod == 0:
						divisors |= {a, div}
			#Controllo se il la lunghezza della lista dei divisori che ha memorizzato e' uguale al parametro k, in tal caso aggiungo nella mia lista il numero n
			if len(divisors) == k:
				l.append(n)
			#Se la variabile prime risulta ancora True, allora il numero sara' primo e dunque verrà aggiunto in lista
			if prime:
				primi.append(n)
	#Sovrascrivo alla lista ls la lista l contenente tutti  i numeri con divisore uguale a k creata nella funzione
	ls[:] = list(l)
	#Restituisco la lista dei numeri primi trovati
	return primi
