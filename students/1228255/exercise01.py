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

ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

import math

def modi(ls,k):
    primi = []
    kdiv  = []
    for n in ls:
        d = divisori_propri(n,k)
        if d == 0:
            primi.append(n)
        if d == k:
            kdiv.append(n)
    ls[:] = kdiv
    return primi

def divisori_propri(N, k):
    divisori = 0
    last = int(math.sqrt(N)) # +2
    i = 2
    while i<=last and divisori <= k:
        if N%i:
            i += 1
            continue
        if i == last:
            divisori += 1
        else:
            divisori += 2
        i += 1
    return divisori

if __name__ == '__main__':
    ls = [121, 4, 37, 441, 7, 16]
    primi = modi(ls,3)
    print(primi)
    print(ls)
