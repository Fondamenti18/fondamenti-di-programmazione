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
    c=0
    p=[]
    l=len(ls)
    while c<l:
        a = []
        n=ls[c]
        m=math.sqrt(n)
        m=int(n/m)
        for x in range(1,m+1):
            if n%x==0:
                a.append(int(x))
        ld=len(a)*2
        if (ld-2)!= k:
            del ls[c]
            c-=1
        if ld<=2:
            p.append(n)
        l=len(ls)
        c+=1
    return p