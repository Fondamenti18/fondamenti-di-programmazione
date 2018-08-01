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
def modi(ls,k):
    lista_primi=[]
    fact= 0
    rad = 0
    p = 0
    for num in range(len(ls)-1,-1,-1):
        fact = 0
        rad = int(sqrt(int(ls[num])))+1
        for i in range(2,rad):
            p = int(ls[num]) % int(i)
            if p == 0:  
                fact+=1
            else:
                pass
        fact = (fact *2)
        print(fact)   
        if fact == 0:
            lista_primi.append(ls[num])
        if fact != k:
            del ls[num]
    lista_primi.reverse()    
    return(lista_primi)