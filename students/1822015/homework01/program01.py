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
import copy

def modi(ls,k):
	numPrimi = []
	tmpList = copy.copy(ls)					#lista da definire temporanea in quanto serve solo ad iterarne gli elementi da cancellare da ls
	for num in tmpList:						
		numDivisori = contaDivisori(num,k)
		if numDivisori != k:					
			if numDivisori == 0:				#se i divisori risultano 0 e' necessariamente numero primo		
				numPrimi.append(num)
			ls.remove(num)						#elimino dalla lista l'elemento non risponde al criterio dato (divisori = k)
	return numPrimi
	
	
	
def contaDivisori(n,k):	
	conta=0
	max = int(sqrt(n))+1				#controllo i divisori fino alla radice+1 del numero preso in esame, in questo modo per ogni divisore trovato considero di averne trovati 2
	for i in range(2,max):
		if (n % i)==0:
			if conta > k:			#esco dal ciclo in quanto i divisori superano k, quindi non rispecchiano il criterio dato
				break				
			else:
				conta +=2
	return conta