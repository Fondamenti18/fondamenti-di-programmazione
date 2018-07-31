'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 è primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avrà che la lista ls=[441,16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def conta_divi(x,k):
    '''restituisce il numero di divisori propri o -1 se sono piu' di k'''
    q=int(x**0.5)
    if x%q==0: return 1
    t=1
    i=2
    s=0
    while i<=x :
        if i==q+1:
            if t==1: return 0
            if 2*t==k +2: return k
            return -1
        if x%i==0:
            s+=1
            x=x//i
        else: 
            if s>0:
                t=t*(s+1)
                if t>k: return -1
                s=0
            i+=1
    if s>0:t=t*(s+1)
    return t-2

def modi(ls,k):
    lista1=[]
    lista2=[]
    for x in ls:
        t=conta_divi(x,k)
        if t==k: lista1+=[x]
        elif t==0: lista2+=[x]
    ls[:]=lista1
    return lista2    
        