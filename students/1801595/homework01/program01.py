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
    primi = []
    lista2 = []
    for x in ls:
        a = x
        numeri = []
        radice = int(math.sqrt(x)) +1
        for j in range(2,radice):
            while x%j == 0:
                numeri.append(j)
                x /= j
        b = 1
        for x in numeri:
            b = b*x
        f = a/b
        if f != 1:
            numeri.append(f)

        d = 1
        for x in set(numeri):
            c = numeri.count(x)
            d = d*(c+1)

        d = d-2
        if d == 0:
            primi.append(a)
        if d != k:
            lista2.append(a)
            
    for x in lista2:
        ls.remove(x)
    return primi

            

