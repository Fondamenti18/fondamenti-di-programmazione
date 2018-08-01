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
import copy
def modi(ls,k):
    lsnp=[]
    ls2=[]
   
    for n in ls:
        acc=0
        for div in range(2,int(sqrt(n))+1):
            if n%div==0:
                acc+=2
            if acc>k:
                break
        if acc==0:
            lsnp+=[n]
        if acc==k:
            ls2+=[n]
            
    ls.clear()
    ls[:]=copy.copy(ls2)
    return lsnp            

