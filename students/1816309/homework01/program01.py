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
	divis=dict()
	for num in ls:
		if num%2 == 0:
			divis[num] = []
			addDivs(divis,num,2)
		else:
			divis[num] = []
	findDivs(ls,divis,3)
	primes=[]
	for key in divis.keys():
		if len(divis[key]) == 0:
			primes.append(key)
			del(ls[ls.index(key)])
	findDivs(ls,divis,4)
	ls[:] = filter(lambda x: len(divis[x])==k,ls)
	return primes
		
def findDivs(ls,divis,s):
	top = int(max(ls)**0.5)
	for divisore in range(s,top+1,2):
		for num in ls:
			checkDivs(divisore,num,divis)
			
def checkDivs(divisore,num,divis):
	if divisore < num:
		if num%divisore == 0:
			addDivs(divis,num,divisore)
		
def addDivs(divis,num,div):
	if div not in divis[num]:
		divis[num].append(div)
	if num/div not in divis[num]:
		divis[num].append(num/div)
		
lista=[70,330,293,154,128,113,178]
modi(lista,6)