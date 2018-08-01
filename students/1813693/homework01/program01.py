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
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.'''


from copy import copy
from math import sqrt
def calcola_divisori(x):
    '''calcola...'''
    i=2
    somma_div=0
    while i<sqrt(x)+1 :
        if x%i==0:
            somma_div+=2
        i+=1
    return somma_div
def num_primi_inls(ls):
    lp=[]
    for x in ls:
        if calcola_divisori(x)==0:
            lp+=[x]
    return lp
def modi(ls,k):
    lpr=num_primi_inls(ls)
    lp=copy(ls)
    for x in lp:
        if calcola_divisori(x)!=k:
            ls.remove(x)
    return lpr



