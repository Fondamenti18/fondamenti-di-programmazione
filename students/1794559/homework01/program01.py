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

def prima(i,k): 
    from math import sqrt
    a=2
    d=0
    while a <= int(sqrt(i)+1):
        
        if i % a == 0:
            d+=2
        a=a+1
    if d == 0:
        return "primo"
    elif d != k:
        return "bene"



def modi(ls,k):
    primi=[]
    secondi=[]
    for i in ls:             
            if prima(i,k)=='primo':
               primi.append(i)
            if prima(i,k)=='bene':
               secondi.append(i)
    for y in secondi:
        ls.remove(y)
    for z in primi:
        ls.remove(z)
    return (primi)
