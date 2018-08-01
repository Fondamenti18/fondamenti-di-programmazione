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

def divisori (n, k):
    conto = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            conto += 2
    if n % math.sqrt(n) == 0:
            conto += 1
    return conto

def modi(ls, k):
    if k >= 0:
        lista_primi = []
        i = 0
        while i < len(ls):
            el = ls[i]
            d = divisori(el, k)
            if d != k:
                ls.remove(el)
            else:
                i += 1
            if d == 0:
                lista_primi.append(el)
        print(ls)
        return lista_primi
    else:
        print('parametro non corretto')
                
