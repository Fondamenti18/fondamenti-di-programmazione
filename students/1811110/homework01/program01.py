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

import math

def div(n, k):
    c = 0
    r = math.ceil(math.sqrt(n))
    d = 2
    while c <= k and d <= r:
        if n % d==0 :
            if n / d == d:
                c += 1
                return c
            c += 2
        d += 1

    return (c)


def primi(n):
    c = 0
    r = math.ceil(math.sqrt(n))
    d = 2
    while d <= r:
        if n % d == 0:
            return -1
        d += 1


def modi(ls, k):
    lp = []
    for n in ls[:]:
        if primi(n) != -1:
            lp += [n]
        if div(n, k) != k:
            ls.remove(n)

    return lp
