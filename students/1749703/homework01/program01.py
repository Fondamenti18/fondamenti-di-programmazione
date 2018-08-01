def calculateDivisors(num):
	''' Calcola i divisori di num e li restituisce come una lista '''
	
	# ds (divisors) e' una collezione disordinata di elementi unici 
	ds = set()
	
	# cerco i fattori sotto la radice quadrata del numero perche'
	# num = a * b ( eccetto per i numeri primi, dove a e b possono solo essere 1 e il numero stesso )
	# se (a oppure b) > sqrt(num) allora a * b > num, e quindi sicuramente non e' un fattore di num.
	# 
	# a / b = c	
	# a / c = b
	# c * b = a
	for n in range(2, int(num ** 0.5) + 1):
		if num % n == 0:		# e' un fattore, quindi aggiungilo (se sono uguali il secondo rimane fuori dato che e' un set)
			ds.add(n)			# n = b
			ds.add(num // n)	# num//n = c
			
	return list(ds)	# converti il set a lista

def modi(ls,k):
	primes = []	# lista che contiene i numeri primi di ls
	exactK = []	# lista che i numeri con k divisori propri di ls
	
	for num in ls:
		divisors = calculateDivisors(num)
		if len(divisors) == 0:	# se non ha divisori propri allora e' un primo
			primes += [num]
		elif len(divisors) == k: # se ha esattamente k divisori propri, aggiungilo alla lista
			exactK += [num] 
	
	# sostituisci l'intera lista ls con quella dei numeri che hanno esattamente k divisori propri
	ls[:] = exactK
	return primes
