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

def modi(ls, k):
    lst_primi = []
    ls_eletodelete = []

    for value in ls:
        counter_k = 0
        ls_numerodivisori = []

        if is_prime(value):
            lst_primi.append(value)
            ls_eletodelete.append(value)

        else:
            if factorize(value,k)!= True:
                ls_eletodelete.append(value)

    for _ in ls_eletodelete:
        ls.remove(_)

    return lst_primi


def is_prime(num):

    i , w = 5 , 2

    if num == 2:
        return True
    if num == 3:
        return True
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False

    while i * i <= num:
        if num % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def factorize(num , k_div):
    lst = []
    if num > 9999999999:
        return False
    for value in range(num):
        if value != 0:
            if value != 1:
                if value in lst:
                    break
                if num % value == 0:
                    lst.append(value)
                    lst.append(int(num / value))
                    if len(lst) > k_div:
                        return False
    if len(lst) != k_div:
        return False
    else:
        return True
