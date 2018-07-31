'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[441,16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

import math

def divisori(x,k):
    ''' restituisce la lista dei divisori della radice quadrata di x'''
    l=[]
    for i in range(2,int(math.sqrt(x)+1)): 
        if x%i==0:
            l+=[i,x//i]
        if len(l)>k:
            break
    return sorted(l)

def modi(ls,k):
    "restituisce la lista dei numeri primi di ls"
    lprimi=[]
    ldivisori=[]
    for i in ls:
        lnuova=divisori(i,k)
        if len(lnuova)==0:
            lprimi+=[i]
        if len(lnuova)==k:
            ldivisori+=[i]
    ls[:]=ldivisori
    return lprimi

