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

def modi(ls,k):
    import math
    from math import sqrt
    primi=[]
    f=0
    c=0
    r=0
    for el in range(len(ls)-1,-1,-1):
        f=0
        r=int(sqrt(int(ls[el])))+1
        for i in range(2,r):
            c=int(ls[el])%int(i)
            if c==0:
                f+=1
            else:
                pass
        f=(f*2)
        if f==0:
            primi.append(ls[el])
        if f!=k:
            del ls[el]
    primi.reverse()
    print(ls)
    return primi

