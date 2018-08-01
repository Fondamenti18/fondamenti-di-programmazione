"""Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
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
import math

def conto(x):
    contodiv=0
    ePari = x % 2 == 0
    if not ePari:
        y = 3
    else:
        y = 2
    sqrt = int(math.sqrt(x) + 1)
    while y < sqrt:
        if x%y ==0:
            contodiv+=1
            if y != x / y:
                contodiv += 1
        if not ePari:
            y += 2
        else:
            y += 1
    return (contodiv)

def modi(ls,k):
    primi=[]
    i = 0
    while i < len(ls):
        element = ls[i]
        divisori = conto(element)
        if divisori != k:
            del ls[i]
            i -= 1
        if divisori == 0:
            primi.append(element)
        i += 1
    return primi



