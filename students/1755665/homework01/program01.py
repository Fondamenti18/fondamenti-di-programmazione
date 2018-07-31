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

def fatt(n):
    fattori=[]
    d=2
    x=int(sqrt(n))+1
    while d<=x:
        if n%d==0:
            fattori.append(d)
            n=n//d
        else:
            d=d+1
    if d>=x and n!=1:
        fattori.append(n)
    return fattori

def divisori(n):
    lista=fatt(n)
    ins=set(lista)
    x=1
    for i in ins:
        x=x*(lista.count(i) + 1)
    return x

def modi(ls,k):
    listaReturn=[]
    l=[]
    for item in ls:
        if divisori(item)==2:
            listaReturn.append(item)
            l.append(item)
        else:
            if divisori(item)!=k+2:
                l.append(item)
    for i in l:
        ls.remove(i)
    return listaReturn