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
	listaPrimi=cercaPrimi(ls)	#richiama funzione cercaPrimi e passa la lista ls
	for numero in ls[::-1]:	#scorre lista ls al contrario
		if(numero in listaPrimi):	#se il numero ?? presente nella listaPrimi
			ls.remove(numero)	#rimuove il numero dalla lista ls
	listaNumeri=cercaDivisori(ls, k)	#richiama funzione cercaDivisori
	for numero in ls[::-1]:		#scorre lista ls al contrario
		if(numero not in listaNumeri):	#se il numero non ?? presente nella lista primi
			ls.remove(numero)	#rimuove numero dalla lista ls
	return(listaPrimi)
	
def cercaPrimi(lista):
	'''funzione che ritorna la lista dei numeri primi da 2 fino alla met?? +1 del numero indicato 
	'''
	from math import sqrt	#importa libreria math
	listaPrimi=[]
	count=0
	for numero in (lista):	#scorre lista
		for divisore in range(2, int(sqrt(numero)+1)):	#scorre un range tra 2 e la radice quadrata del numero +1
			if(numero % divisore == 0 and divisore!=numero):	#se il numero diviso il divisore restituisce reto 0 e il divisore ?? diverso dal numero
				count=0	#count uguale a zero
				break	#interrompi ciclo
			else:
				count=1	#count uguale a 1
		if(count>0):	#se count ?? maggiore di 0
			listaPrimi.append(numero)			#aggiungi numero alla listaPrimi	
	return(listaPrimi)
				
def cercaDivisori(lista, k):
	'''funzione che ritorna la lista dei numeri che hanno k divisori 
	'''
	from math import sqrt	#importa libreria math
	count=0	#contatore
	lstOk=[]	#lista divisori giusti
	for numero in (lista):	#scorre la lista ls
		for divisore in range(2, int(sqrt(numero)+1)):	#scorre un range tra 2 e la radice quadrata del numero più 1
			if(numero % divisore == 0):	#se il numero diviso il divisore da resto 0
				if(count > k):	#se il contatore ?? maggiore di k
					break	#interrompi il ciclo
				elif(divisore == numero):	#se il divisore è uguale al numero
					count+=1	#aumenta contatore di uno
				else:	#se il divisore è diverso dal numero
					count+=2	#aumenta il contatore di due
		if(count == k):	#se il contatore ?? uguale a k
			lstOk.append(numero)	#aggiungi il numero alla lista lstOk
		count=0	#reset contatore a zero		
	return(lstOk) 
				
if __name__ == '__main__':				
	print(modi([10000000116, 10000000431, 10000000469, 10000000548, 10000000697, 10000000711, 10000000768, 10000000924],16))