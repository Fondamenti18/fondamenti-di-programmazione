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


import math

def modi(ls,k):
    "inserite qui il vostro codice"
    if k < 0:
        return "il secondo parametro deve essere un numero intero positivo!"
    else:
        new_lista = [a for a in ls if is_prime(a)]
        for x in ls[:]:
            to_delete(ls, x, fattori(x), k)
    return new_lista



def is_prime(n):
    n - abs(int(n))
    if n is 2:
        return True
    if n % 2 is 0:
        return False
    if not n & 1:
        return False
    radice = math.sqrt(n)
    condizione = int(radice) + 1
    for x in range(3, condizione, 2):
        if n % x is 0:
            return False
    return True


def fattori(n):
    factors = []
    controllo = 2
    sqrt = math.sqrt(n)
    while controllo < sqrt:
        if n % controllo == 0:
            factors.append(controllo)
            factors.append(n/controllo)
        controllo += 1

        if sqrt == controllo:
            factors.append(controllo)
        if 1 in factors:
            factors.remove(1)
        if n in factors:
            factors.remove(n)
    return len(factors)


def to_delete(ls, i, x, k):
    if x != k:
        if i in ls:
            ls.remove(i)
    return

ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3)
