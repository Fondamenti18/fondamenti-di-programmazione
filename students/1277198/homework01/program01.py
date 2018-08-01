'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[441,16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''
#la funzione primes_factors fornisce il numero dei divisori di un numero, compresi 1 e se stesso e li passa a modi
#la funzione modi ha il solo compito di riempire una lista di numeri primi e di cancellare da ls quelli non desiderati usando il numero di divisori.
def modi(ls,k):
    primes=[]
	#gira gli elementi in ls analizzando il numero di divisori restituito da primes_factor (2 se primo primes_factor-2 per i divisori propri)
	#poi toglie elementi da ls 
    for el in ls[:]:
        dp=primes_factors(el)
        if dp==2: primes.append(el)
        if dp-2!=k: ls.remove(el)
   
    return primes

def primes_factors(n):
    div=2
    prod=1
    i=0 
	#trova i fattori primi, cercandoli fino a (n^0.5), per ogni fattore incrementa il counter di 1
    while div*div<=n:
        count=0
        while n%div==0:
           n/=div
           count+=1
        div+=i+1
        i=1
	#il numero dei divisori propri e' pari al prodotto di tutti gli esponenti dei fattori primi, ognuno aumentato di 1, quindi incrementiamo prod
        prod*=count+1
	#se n e' rimasto maggiore di uno, vuol dire che il numero ha un divisore in piu', primo e maggiore della radice,
	# o che e' primo esso stesso, si incrementa prod
    if n>1:
        prod*=2
    return prod
