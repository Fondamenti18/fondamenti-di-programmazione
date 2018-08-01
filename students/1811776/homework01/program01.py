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
    "inserite qui il vostro codice"

import math
def divisori(n):
    a=0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            a+=2
    if math.sqrt(n)==int(math.sqrt(n)):
        a-=1
    return a

def modi(ls,k):
    lista1=[]
    lista=[]
    for b in ls:
        if divisori(b)==0:
            lista1+=[b]
        if divisori(b)!=k:
            lista+=[b]
    for x in lista:
        ls.remove(x)
    return lista1
