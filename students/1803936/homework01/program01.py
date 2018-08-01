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

lista=[]
tmp1 = []



from math import *


def div(k):
    tl = []
    x = ceil(sqrt(k) + 1) 
    for i in range (1, x):
        if k % i == 0:
            z = k // i
            tl += [i] + [z]
            
    del tl[0:2]
    tl2 = list(set(tl))
    return tl2



def modi(lista, k):
    tmp1 = lista.copy()
    primi = []
    for j in lista:
        if len(div(j)) == 0:
            primi += [j]
          
        if k == len(div(j)):
            tmp1.remove(j)
    
    for y in tmp1:
        lista.remove(y)
                
            
    return primi











