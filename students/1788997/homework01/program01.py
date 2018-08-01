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
from functools import reduce
p = set()
def isPrime(n):
    '''verifica e ritorna true se il numero n  primo'''
    if n in p: return True
    d, sqrt = 3, n**0.5
    if n < 2 or not n % 2: return False
    while d <= sqrt:
        if not n % d: return False
        d += 2
    p.add(n)
    return True
def findDividers(n, k):
    '''scompone in fattori primi il numero n e ritorna il numero di divisori propri'''
    c, d = n, {}
    while c > 1:
        if isPrime(c):
            d[c] = d.setdefault(c, 1) + 1
            break
        for i in range(2 + int(c%2),n,2):
            if not c % i: 
                c /= i
                d[i] = d.setdefault(i, 1) + 1
                break
    return reduce(lambda x,y: x*y, d.values()) - 2 == k
def modi(ls,k):
    '''ritorna una lista con i numeri primi contenuti in ls e modifica ls eliminando i numeri che non hanno esattamente k divisori propri'''
    l = []
    for i in range(len(ls)-1, -1, -1):
        if isPrime(ls[i]):
            l.insert(0, ls.pop(i))
            continue
        if not findDividers(ls[i], k):
            ls.pop(i)
    return l