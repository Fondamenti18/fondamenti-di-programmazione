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
def modi(ls, k):
    i=0
    primi=[]
    while i<len(ls): 
        if (ls[i]%2==0):
            if (funzione_standard (ls, i, k , 2, 1, primi)==1):
                i+=1
        else:
            if(funzione_standard(ls, i, k,3,2,primi)==1):
                i+=1
    return primi
    
def funzione_standard( ls, i, k, partenza, intervallo, primi):
    divisori=[]        
    n=ls[i]
    for j in range(partenza,round(math.sqrt(ls[i])+1),intervallo):   
        if (n%j)==0:
            if j not in divisori:
                divisori.append(j)
            if n/j not in divisori:
                divisori.append(int(n/j))
        if (len(divisori)>k):
            break
    if len(divisori)==0:
        primi.append(ls[i])
        ls.remove(ls[i])
        return -1
    elif len(divisori)!=k:
        ls.remove(ls[i])
        return -1
    else:
        return 1