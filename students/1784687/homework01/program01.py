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

ls=[121,4,37,441,7,16]
k=3

def n_div(n):
    count = 0
    for x in range(2,n//2+1):
        if n % x == 0:
            count+=1
    return count

def modi(ls,k):
    lp = []
    for el in ls[:]:
        n_divisori = n_div(el)
        if n_divisori == 0:
            lp.append(el)
        if n_divisori != k:
            ls.remove(el)
    return lp
