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
ls=[121, 4, 37,441,7,16]

def primo(x):
    i=2
    while i<x:
        if x%i==0:
            return False
        i+=1
    return True
        

        
def divisori(k):
    s=0
    for i in range(2,int (sqrt(k))+1):
        if k%i==0:
            s+=2
            if s>k+1:
                break
    r=sqrt(k)
    if r==int(r):
        s-=1
    return s
            
    
def modi(ls,k):
    lista1=[]
    lista2=ls.copy()
    for x in lista2:
        if primo(x):
            lista1+=[x]
        if divisori(x)!=k:
            ls.remove(x)
    return lista1
        

print(modi(ls,3))
print(ls)
