from math import sqrt

def modi(ls, k):
	numeri_primi = []
	for i in range(len(ls)-1, -1, -1):
		if ls[i]%2:
			divisori = dividi_dispari(ls, ls[i], k)
		else:	
			divisori = dividi(ls, ls[i], k)
		numeri_primi = primi(divisori, numeri_primi, ls[i])
		delete(divisori, k, ls, i)
	return numeri_primi
			
def dividi(ls, i, k):
	divisori = []
	j = 1
	limit = round(sqrt(i))
	return calcolo(i, j, limit, divisori, 1)
	
def dividi_dispari(ls, i, k):
	divisori = []
	j = 1
	limit = round(sqrt(i))
	return calcolo(i, j, limit, divisori, 2)

def primi(div, lista, num):
	if not div:
		lista = [num] + lista
	else:
		lista = lista
	return lista

def delete(div, cond, lista, index):
	temp = 1
	while div:
		temp *= div.count(div[0]) + 1
		div = [x for x in div if x != div[0]]
	if temp - 2 != cond:
		del lista[index]
		
def calcolo(i, j, limit, divisori, aumento):
	temp = j
	while i > 1 and temp <= limit + 1:
		temp += aumento
		if not i%temp:
			i = int(i/temp)
			divisori += [temp]
			temp = j
			limit = round(sqrt(i))
		elif limit -1 <= temp <= limit + 1 and divisori:
			divisori += [i]
			i = 1
	return divisori