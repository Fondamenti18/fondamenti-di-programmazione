"""
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
"""


def prime_factorization(n):
    for x in range(2, n + 1):
        if n % x:
            continue  # !DIVISOR

        return [x, *prime_factorization(n // x)]

    return []


def modi(ls, k):
    response = []
    for n in ls[::]:
        if n > 0:
            factorization = prime_factorization(n)
            prime_factors = set(factorization)

            if n in prime_factors:
                response.append(n)  # PRIME

            else:
                divisors = 1
                for pf in prime_factors:
                    divisors *= factorization.count(pf) + 1

                if (divisors - 2) == k:  # DIVS - (1 and SELF)
                    continue

        del ls[ls.index(n)]

    return response
