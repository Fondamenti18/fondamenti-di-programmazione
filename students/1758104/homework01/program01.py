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

def HasKDivs(n: int, k: int):
    if n in [0, 1] and k not in [0, 1]: return False
    divs = []
    for i in range(2, k):
        if n%i == 0:
            divs.append(i)
        else:
            continue
        if len(divs) > k: return False
    if len(divs) < k: return False
    
    return True



def isPrime(num: int):
    
    if str(num)[-1] in ['0', '2', '4', '5', '6', '8']: return False
    cifre = list(str(num))
    cifre[:] = [int(e) for e in cifre]
    if sum(cifre) % 3 == 0: return False
    if num % 11 == 0: return False
    if num % 13 == 0: return False
    for c in range(2, 10000):
        if num%c == 0: return False
    
    return True




def modi(ls,k):
    
    primes = []
    for n in ls:
        print(f'lavoro su {n}')
        if isPrime(n):
            print(f'{n} PRIMO')
            primes.append(n)
        else:
            print(f'{n} NON PRIMO')
    c = ls.copy()
    ls[:] = [c for c in ls if HasKDivs(c, k)]
    
    return primes
