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


def initialCheck(num):
    if num <= 3:
        return True
    else:
        return False


def squareRoot(num):
    return num ** 0.5


def checkProperDivisors(num, k):
    pDivisors = 0
    sqrroot = int(squareRoot(num)) + 1
    half = num // 2 + 1

    for i in range(2, half):  # checking 2 to sqrt of num
        if i > sqrroot and pDivisors == 0:
            break
        elif num % i == 0:
            pDivisors += 1
            if pDivisors > k:
                break
    return pDivisors


def modi(ls, k):
    "inserite qui il vostro codice"

    primesList = []
    for num in list(ls):
        if initialCheck(num):
            pDivisors = 0
        else:
            pDivisors = checkProperDivisors(num, k)

        if pDivisors == 0:
            primesList.append(num)
        if pDivisors != k:
            ls.remove(num)

    return primesList
