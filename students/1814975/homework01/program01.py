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
def modi(ls,k):
    "inserite qui il vostro codice"'''
from math import sqrt
def conta_div_num(L):
    div = []
    cont=0
    for x in range(len(L)-1,-1,-1):
        for n in range(2,int(sqrt(L[x]))+1):
            if L[x]%n==0:
                cont+=2
            elif n/L[x]==0:
                cont+=1
        div+=[cont]
        cont=0
    return div               
     
def modi(L,k):
    modi=[]
    L1=[]
    div = conta_div_num(L)
    div = list(reversed(div))
    for el in range(len(div)-1,-1,-1):
        if div[el]==0:
            modi+=[L[el]]
        if div[el] == k:
            L1+=[L[el]]
        else:
            del L[el]
    return list(reversed(modi))