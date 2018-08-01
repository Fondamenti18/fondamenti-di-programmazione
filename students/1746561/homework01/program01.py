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

from collections import Counter

def fatt_primi(n): #Trova i fattori primi
    fatt = []
    q = 2
    while q*q <= n:
        while  n%q == 0:
            fatt.append(q)
            n //= q
        q += 1
    if n > 1:
       fatt.append(n)
    return fatt

def div_propri(ls): #Restituisce il numero di divisori propri
    n = 1
    i = 0
    diz = Counter(ls)
    val = list(diz.values())
    for i in range(len(diz)):
        n *= val[i]+1
        i+=1
    return n-2

def modi(ls,k):
    ld = [] #lista per i divisori
    lp = [] #lista per i primi
    for i in ls:
        if div_propri(fatt_primi(i)) == k: ld.append(i) #Divisori
        if len(fatt_primi(i)) <= 1: lp.append(i) #Numeri primi
    ls[:] = ld[:]
    return lp
