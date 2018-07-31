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

def lunghezza (valori):
    l=0
    for valore in valori:
        l+=1
    return l

def modi(ls,k):
    a= lunghezza(ls)-1
    lsPrimi=[]
    for i in range(a,-1,-1):
        d=0
        if ls[i]<=1:
            ls.pop(i)
        for m in range(2,int(sqrt(ls[i]))+1):
            if ls[i]%m==0:
                d+=2     
        if d==0:
            lsPrimi.append(ls[i])
        if d!=k:
            ls.pop(i)

    return (sorted(lsPrimi))
