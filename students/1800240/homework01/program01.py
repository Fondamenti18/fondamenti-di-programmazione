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

def num_div_prop(x):
    from math import sqrt
    div = []
    for i in range(2,int(sqrt(x))+1) :
        if x % i == 0 :
            if x // i == i :
                div += [i]
            else :
                div += [i, x//i]
    return len(div)

def modi(ls,k):
    ls_primi = []
    for n in ls[:] :
        if num_div_prop(n) == 0 :
            ls_primi.append(n)
            ls.remove(n)
        elif num_div_prop(n) != k :
            ls.remove(n)
    return ls_primi