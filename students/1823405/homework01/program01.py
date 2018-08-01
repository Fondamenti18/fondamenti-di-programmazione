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



def is_primo(num):
    if num > 1:
        n = num // 2
        for i in range(2, n+1):
            if num % i == 0:
                return -1
        return 0
    else:
        return -1

def modi(ls,k):
    ls_primo = []
    ls2 = []
    for x in ls:
        div = []
        if is_primo(x) == 0:
            ls_primo.append(x)
        for n in range(2, x):
            if x % n == 0:
                div.append(n)
        if len(div) == k:
            ls2.append(x)
    print(ls_primo)
    return ls2
       

    