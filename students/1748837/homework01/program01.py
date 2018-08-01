from math import sqrt
from functools import reduce
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
    daelim=[]
    primi=[]
    for i in range(len(ls)-1,-1,-1):
        numdiv=(div(ls[i],k) if len(str(ls[i]))<8 else len(factors(ls[i]))-2)
        if numdiv!=k:
            if numdiv==0:
                primi.append(ls[i])
            ls.remove(ls[i])
    return primi[::-1]

#presi in input un numero n ed uno k conta il numero di divisori di n fermandosi al più a k+1, e ritorna il contatore
def div(n,k):
    counter=0
    div=2
    while(div**2<n and counter<=k):
        if(n%div==0):
            counter+=2
        div+=1
    counter+=(1 if div**2==n else 0)
    return counter

#preso in input n ritorna il set dei divisori di n, metodo più efficente di div sui grandi numeri
def factors(n):
        div = 2 if n%2 else 1
        return set(reduce(list.__add__,([i, n//i] for i in range(1, int(sqrt(n))+1, div) if n % i == 0)))
