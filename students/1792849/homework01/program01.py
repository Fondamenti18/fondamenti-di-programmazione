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
from math import sqrt
def factors(n):
    result = []
    for i in range(2, int(sqrt(n)) + 1):
        div, mod = divmod(n, i)
        if mod == 0 and result.count(div) < 1 :
            result += [div]
        if mod == 0 and result.count(i) < 1 :
            result += [i]
    return result
    
def primo(n):
    return factors(n) == []

def modi(ls,k):
    ls2 = []
    for el in range(len(ls)-1, -1, -1):
        if primo(ls[el]):
            ls2.append(ls[el])
            ls.remove(ls[el])
        elif len(factors(ls[el])) != k:
                ls.remove(ls[el])
    ls2.reverse()
    return ls2

