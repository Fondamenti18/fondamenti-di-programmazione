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

from math import sqrt as radice

def modi(ls,k):
	'''
	Questa funzione prende come parametri una lista 'ls' contenente numeri interi ed un numero naturale k. Procede quindi a verificare se
	il parametro k e' negativo, e in tal caso lancia un'eccezione terminando il programma. Quindi salva una lista 'primi' in cui sono presenti
	solo i numeri della lista che hanno un numero di divisori propri pari a 0, ovvero i numeri primi della lista. Infine sovrascrive la lista 'ls'
	mantenendo solo i valori che hanno un numero di divisori propri pari a k e ritorna la lista 'primi'.
	'''
	if (k < 0):
		raise Exception("il parametro K inserito e' negativo")
	try:
		primi = [i for i in ls if divisori_propri(i, 0) == 0]
	except TypeError as Err:
		print("Errore di tipo: e' possibile effettuare divisioni solo tra numeri interi.")
		print(Err.args)
	else:
		lista_new = []
		for i in ls:
			if divisori_propri(i, k) == k:
				lista_new += [i]
		ls[:] = lista_new.copy()
		return primi
	
def divisori_propri(n, k):
	'''
	Questa funzione prende come parametro un numero intero n ed un numero naturale k. Tramite un ciclo for la funzione e' in grado di determinare
	il numero di divisori propri del numero, ovvero (numero dei divisori) - {1, n}.
	'''
	conta = 0
	if n < 0:
		for i in range(int(radice(n)), 1):
			if not conta > k:
				if n%i == 0:
					if i == int(radice(n)):
						conta += 1
					else:
						conta += 2
			else:
				break
	else:
		for i in range(2, int(radice(n))+1):
			if not conta > k:
				if n%i == 0:
					if i == int(radice(n)):
						conta += 1
					else:
						conta += 2
			else:
				break
	return conta

if __name__ == '__main__':
	a = [136]
	print(modi(a, 6))
	print(a)