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
def factorize(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def number_of_divisors(factor_list):
    number_of_factors = dict()
    number_of_divisors = 1
    for n in factor_list:
        if n in number_of_factors:
            number_of_factors[n] += 1
        else:
            number_of_factors[n] = 1
    for key, value in number_of_factors.items():
        number_of_divisors *= value+1
    return number_of_divisors

def modi(ls,k):
    prime_numbers = list()
    to_remove = list()
    for n in ls:
        n_divisors = number_of_divisors(factorize(n))
        if n_divisors == 2:
            prime_numbers.append(n)
            to_remove.append(n)
        elif n_divisors-2 != k:
            to_remove.append(n)
    for n in to_remove: ls.remove(n)
    return prime_numbers
