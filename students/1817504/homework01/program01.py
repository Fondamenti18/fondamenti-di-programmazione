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
    ls_primi=[]
    for i in range(len(ls)-1,-1,-1):
        numero=ls[i]
        n=num_div(numero,k)
        if n==0:
            ls_primi+=[numero]
            del ls[i]
        elif n!=k:
            del ls[i]
    return ls_primi[::-1]

def num_div(x,k):
    n=0
    for a in range(2,int(x**0.5)+1):
        if x%a==0:
            if a==x**0.5:
                n+=1
            else:
                n+=2
        if n>k: return n        
    return n
