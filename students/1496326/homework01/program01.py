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

def isPrime(n):
	#calcola se un numero e' primo
	for divider in range(2, int (math.sqrt(n)+1)):
		if(n % divider == 0):
			#print(str(n) + ' numero NON primo!')
			return False
	#print(str(n) + 'numero primo')
	return True

def scomposizione(n):
	#scompongo il numero in fattori primi
	factorlist=[]
	loop=2
	increment = 1
	while loop<=n:

		if n%loop==0:
			
			n//=loop
			factorlist.append(loop)
		else:
			if(loop==2):
				#escludo i pari
				loop +=1
				increment = 2
			else:
				loop+=increment
		
	#print('exiting')
	return factorlist

def divisori(primes, k):
	#a partire da una matrice di divisori primi moltiplico ogni riga della matrice per la successiva per ottenre tutti i divisori possibili
	oldprime = {}
	dividers = []
	
	for prime in primes:
		if(prime in oldprime):
			#se il numero e' già presente uso la posizione nella lista come potenza del numero
			count = oldprime[prime]
			lenght = len(count)+1
			count.append(prime**lenght)
		else:
			count = []
			count.append(prime)
			oldprime[prime] = count
			
	count = next(iter(oldprime))
	count = oldprime.pop(count)

	for value in count:
		dividers.append(value)
	
	#moltiplico ogni riga della matrice per la successiva per ottenre tutti i divisori possibili
	for key,value in oldprime.items():
		newDividers = []
		for prime in value:
			newDividers.append(prime)
			for div in dividers:
				val = div*prime

				if(val not in dividers and val not in newDividers):
					newDividers.append(val)
					
		dividers = dividers + newDividers
		if(len(dividers) > k):
			break
	
	dividers.sort()
	#print(dividers)
	return dividers

def modi(ls,k):
	
	#copio la lista per poter modificare ls originale mentre ciclo sui suoi valori
	newLs = list(ls)
	primeList = []
	
	for number in newLs:
		
		#se e' primo esco subito
		if(isPrime(number)):
			primeList.append(number)
			ls.remove(number)
			continue
		
		
		primes = scomposizione(number)
	
		if(len(primes) > k+1):
			ls.remove(number)
			continue
		
		dividers = divisori(primes, k)

		if(number in dividers):
			dividers.remove(number)

		if(len(dividers) != k):
			ls.remove(number)
		if(len(dividers) == 0):
			primeList.append(number)
		
	
	#ritorno la lista di numeri primi presenti in ls
	#print(dividers)
	return primeList