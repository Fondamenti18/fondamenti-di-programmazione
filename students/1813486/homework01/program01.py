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

    ls2 = r2(ls)
    r1(ls, k)
    return ls2


def r1(ls, k):
    for i in range(len(ls) - 1, -1, -1): # indici inversi [6, 5, 4...]
        n = 2
        op = int(math.sqrt(ls[i]))
        numero = ls[i]
        a = []
        b = 1
        conta = 0
        if nprimo(ls[i]) != True:
            while n < op:
                r = numero % n
                if r == 0:
                    numero = numero // n
                    conta += 1
                else:
                    n += 1
                    if conta != 0:
                        a = a + [conta + 1]
                        conta = 0
            for e in a:
                b *= e
            if b - 2 != k:
                del ls[i]
        else:
            if k != 0:
                del ls[i]


def r2(ls):
    ls2 = [] # nuova lista per l'output (2)
    for n in ls:
        if nprimo(n):
            ls2 = ls2 + [n] # aggiunta degli elementi con "k" divisori propri alla nuova lista
    return ls2


def nprimo(n): # test di primalità
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True