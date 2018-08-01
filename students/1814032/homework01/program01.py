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

from functools import reduce

def modi(ls,k):
	exps = [[] for el in ls]
	ls_fact = ls[:]
	opt(ls,ls_fact,exps)
	cleanUpRemaining(ls_fact,exps)
	return finish(ls,exps,k)
	
def opt(ls,ls_fact,exps):
	if max(ls)-min(ls) >= 1000000:
		for i in range(len(ls)):
			factorize_s(ls,ls_fact,i,exps)
	else:
		for prime in eratoast(int(max(ls)**0.5)+1):
			if factorize_l(ls,ls_fact,prime,exps):
				break
	
def eratoast(m):
	D = {}
	pri = 2
	while pri<=m:
		num = D.pop(pri, None)
		if num:
			x = num + pri
			while x in D: x += num
			D[x] = num
		else:
			D[pri*pri] = pri
			yield pri
		pri += 1
	
def factorize_l(ls,ls_fact,prime,exps):
	quit = True
	for i in range(len(ls)):
		if prime <= ls_fact[i] and prime != ls[i]: #if ls[i1] is lower than sqrt(ls[i2]), ls[i1] could result not prime even if it's prime.
			decomp(i,ls_fact,prime,exps)
			quit = False
	return quit
	
def factorize_s(ls,ls_fact,i,exps):
	for prime in eratoast(int(ls[i]**0.5)+1):
		if prime <= ls_fact[i] and prime != ls[i]: #if ls[i1] is lower than sqrt(ls[i2]), ls[i1] could result not prime even if it's prime.
			decomp(i,ls_fact,prime,exps)
		else: 
			break
			
def decomp(i,ls_fact,prime,exps):
	tmp_exp = 0
	while ls_fact[i]%prime == 0:
		ls_fact[i] /= prime
		tmp_exp += 1
	if tmp_exp != 0:
		exps[i].append(tmp_exp+1)
		
def cleanUpRemaining(ls_fact,exps):
	for i in range(len(ls_fact)):
		if ls_fact[i] != 1:
			ls_fact[i] /= ls_fact[i] #redundant
			exps[i].append(2)
			
def finish(ls,exps,k):
	tup = list(enumerate([reduce(lambda x,y: x*y,exps[i]) for i in range(len(ls))]))
	ls_bkp = ls[:]
	ls[:] = skim(ls,tup,k)
	return skim(ls_bkp,tup,0)
	
def skim(ls,tup,k):
	return [ls[t[0]] for t in tup if t[1]-2==k]