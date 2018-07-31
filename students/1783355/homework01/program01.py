'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno
e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed
un intero non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7]
mentre al termine della funzione si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi
il punteggio dell'esercizio e' zero.
'''

from math import sqrt

def primo(n):
    l = int(n / 2) + 1
    for x in range(2, l):
        if n % x == 0:
            return False
    return True

def num_divisori(n):
    divisori = 0
    l = int(sqrt(n)) + 1
    for j in range(2, l):
        if n % j == 0:
            divisori += 2
    return divisori

def modi(ls, k):
    lista_primi=[]
    da_rimuovere=[]
    for i in ls:
        if primo(i) is True:
            lista_primi.append(i)
        if num_divisori(i) != k:
            da_rimuovere.append(i)
    for i in da_rimuovere:
        ls.remove(i)
    return lista_primi