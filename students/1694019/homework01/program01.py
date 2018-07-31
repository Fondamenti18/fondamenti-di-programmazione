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

def primo(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def modi(ls,k):
    '''inserite qui il vostro codice'''
    lista1 = list()
    for elemento in ls:
        if primo(elemento) == True:
            lista1.append(elemento)
            #ls.remove(elemento)
    lista0 = ls.copy()
    for x_input in lista0:
        c = (-2)
        for i in divisore_proprio(x_input):
            c += 1
        if c != k:
            ls.remove(x_input)
    return lista1

def divisore_proprio(n):
    divisore = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                divisore.append(n / i)
    for divisori in reversed(divisore):
        yield divisori
