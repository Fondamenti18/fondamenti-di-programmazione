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
    ls2=[] #lista contenente i numeri primi
    la=ls[:] #lista sostitutiva della lista originale
    for i in la:
        if primo(i):
            ls2+=[i]
        if check(i,k):
            ls.remove(i)
    return ls2

def primo(a): #restituisce True se a è primo
    p=True
    for i in range(2,a//2+1):
        if a%i==0:
            p=False
            break
    return p

def check(a,k): #restituisce True quando nDiv!=k
    p=True
    nDiv=0
    for i in range(2,a//2+1):
        if a%i==0:
            nDiv+=1
        if nDiv>k:
            break
    if nDiv==k:
        p=False
    return p

    
