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

def numero_primo(x):
    '''controllo se i-esimo elemento della lista iniziale e' numero primo'''
    d = 2
    for d in range (2, int(sqrt(x)+1)):
        if x % d == 0:
            return False
        d += 1
    return True

def fattori_primi(ls, lista_div, i):
    '''scomposizione in fattori primi di i-esimo elemento della lista iniziale'''
    d = 2
    y = ls[i]
    while y >= d*d:
        if y % d == 0:
            lista_div.append(d)
            y //= d
        else:
            d += 1
    if y > 1:
        lista_div.append(y)

def conta_divisori(ls, i):
    '''conteggio dei divisori partendo dalla lista (lista_div) contenente la scomposizione in fattori primi'''
    lista_div = []
    fattori_primi(ls, lista_div, i)
    return numero_divisori(lista_div)

def numero_divisori(lista_div):
    '''ritorna il numero effettivo di divisori'''
    j = 0
    cont_uguali = 1
    n_div = 1
    while j < len(lista_div):
        cont_uguali = lista_div.count(lista_div[j])
        n_div = n_div * (cont_uguali+1)
        j += cont_uguali
    return n_div-2

def rimuovi_elemento(ls, i):
    '''rimozione di un elemento della lista'''
    del ls[i]
    return ls

def modi(ls, k):
    '''trovare numeri primi e numeri che hanno un numero di divisori uguale a k'''
    lista_primi = []
    for i in range(len(ls)-1, -1, -1):
        if numero_primo(ls[i]) == True:
            lista_primi.append(ls[i])
            ls = rimuovi_elemento(ls, i)
        elif conta_divisori(ls, i) != k:
            ls = rimuovi_elemento(ls, i)
    return lista_primi[::-1]