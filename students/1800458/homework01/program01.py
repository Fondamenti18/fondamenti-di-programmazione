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

import time
import math



def modi(ls,k):
    numeriPrim = []
    #we create a copy of the list to be able to remove elements from it while iterating
    for elem in ls[:]:
        #counts num of divisors for each element
        count = 0
        #from 2 to square root of the number + 1
        for i in range(2, int(math.sqrt(elem))+1):
            if elem % i == 0:
                count += 1
                if elem // i != i:
                    count += 1
        # Program01.1
        if count is not k:
            #remove element that does not have same number of dividers as k
            ls.remove(elem)
        # Program01.2
        if count == 0:
            #no dividers so we have prim number
            numeriPrim.append(elem)
    return numeriPrim
