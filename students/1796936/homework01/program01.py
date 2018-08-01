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





def div(n, m):
    cnt = 0
    step = 2
    if n % 2 == 0:
        step=1
        cnt+=1
    for x in range(3, int(n//2) + 1, step):
        if(n % x == 0):
            cnt += 1
            if cnt > m:
                return cnt
    return cnt
import math
def modi(lista, k):
    lp = []
    for el in lista[:]:
        if len(str(el)) > 10:
            a = []
            for x in range(2, math.sqrt(int(el)) +1):
                if el % x == 0:
                    a.append(x)
                if x == el:
                    a.remove(x)
                if len(a) > k:
                    return a
            if len(a) == 0:
                lp.append(el)
            if len(a) != k:
                lista.remove(el)
        else:
            n = div(el, k)
            if n==0:
                lp.append(el)
            if n!=k:
                lista.remove(el)
    return lp