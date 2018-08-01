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
    "inserite qui il vostro codice"
    primi = []
    ls1 = ls.copy()
    for x in ls1:
        if primo(x):
            primi += [x]
            ls.remove(x)
        else:
            if divisori(x) != k:
                ls.remove(x)
    return primi

def primo(n):
    "restituisce true se x è primo altrimenti false"
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n%x == 0:
            return False
    return True

def formatta(ls):
    res = []
    flag = False
    for x in ls:
        for elem in res:
            if elem[0] == x:
                elem[1] += 1
                flag = True
                break
        if flag == False:
            res += [[x, 1]]
        flag = False
    return res

def divisori(n):
    l = scomposizione(n)
    tab = formatta(l)
    count = 1
    for x in tab:
        count *= x[1]+1
    return count-2

def scomposizione(n):
    lista = []
    while n%2 == 0:
        lista.append(2)
        n/=2
    d = 3
    while n>=d:
        if n%d==0:
            lista.append(d)
            n/=d
        else:
            d+=2
    return lista
