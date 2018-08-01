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

import math

def modi(ls,k):
    lsp = []

    i=0
    l=len(ls)
    while i<l:      
        
        j=2 
        ceil=math.sqrt(ls[i])
        counter=0
        while j<=ceil:
            if ls[i]%j==0:
                counter+=2
            j+=1    
        if float.is_integer(ceil):
            counter-=1
        
        elif counter==0:
            lsp.append(ls[i])
            
        
        if counter!=k:
            ls.remove(ls[i])
            
            l-=1
        else:
            i+=1
            
    return lsp

