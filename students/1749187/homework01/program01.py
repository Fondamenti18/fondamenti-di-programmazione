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


def PrimeNumber(num):
    '''Calculate if The number is Prime or Not'''
    n = int(math.sqrt(num)) + 1
    for i in range(2, n):
        if num % i == 0:
            return False
    return True


def ScomFatt(n):
    '''Decompose the Big number in Prime Number'''
    fattore = []
    d = 2
    divisibile = True
    while divisibile:
        if n % d == 0:
            fattore.append(d)
            n = n / d
            if PrimeNumber(n):
                fattore.append(int(n))
                divisibile = False
        else:
            d = d + 1

    return fattore


def countNum(n):
    dicts = {}

    for i in n:  # for each value save how many times it appears in the list
        if not i in dicts:
            dicts[i] = 1
        else:
            dicts[i] += 1
    return dicts

def FindDivisori(n, k):
    '''Find all divisori for the number'''
    dicts = countNum(n)
    divisori = 1

    for key in dicts:
        divisore = dicts[key] + 1 #math apply : example 24 = 2^3 * 3^1
        divisori *= divisore  # so, we have to take (3+1)*(1+1)

    if divisori - 2 != k:
        return True

def pmList(ls):
    PrimeNumList = []
    for item in ls:
        if PrimeNumber(item):
            PrimeNumList.append(item)
            ls.remove(item)
    return PrimeNumList

def modi(ls, k):
    # inserite qui il vostro codice
    PrimeNumList = pmList(ls) # return prime list function
    result = list(ls)

    for i in range(len(result)):
        num = ScomFatt(result[i])
        if FindDivisori(num, k):
            ls.remove(result[i])

    return PrimeNumList
