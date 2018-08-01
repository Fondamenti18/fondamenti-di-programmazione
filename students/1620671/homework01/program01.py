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
    l = []
    i = 0
    while i<len(ls) :
        if primo(ls[i], k):
            l += [ls[i]]
        if conta_divisori(ls[i], k) != k:
            ls.remove(ls[i])
            i -= 1
        i += 1
    return l

def conta_divisori(x, k): #funzione che conta i divisori dell'intero x
    c = 0
    i = 2
    while i <= int(math.sqrt(x)):
        if x%i==0:
            c += 2
        if c > k:
            return c
        i+=1
    return c


def primo(x, k): #funzione che restituisce True se il numero x e primo, False altrimenti
    return conta_divisori(x, k) == 0
