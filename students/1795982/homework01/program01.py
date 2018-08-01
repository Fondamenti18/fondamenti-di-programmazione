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
def conta_divisori(n,k):
    d=0
    r=sqrt(n)
    for i in range(2,int(r)+1):
        if n%i==0:
            d+=2
            if d>k+1:
                break
    if r==int(r):
        d-=1
    return d

def modi(ls,k):
    nprimi=[]
    i=0
    while i<len(ls):
        if conta_divisori(ls[i],k)==0:
            nprimi.append(ls[i])
        if conta_divisori(ls[i],k)!=k:
            ls.remove(ls[i])
            i-=1
        i+=1
    return nprimi
