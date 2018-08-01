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
    primi=[] # lista che contiene i numeri primi
    for indice in range(len(ls)-1,-1,-1):
        divisori=0 # numero dei divisori del numero estratto dalla lista
        l=math.ceil(math.sqrt(ls[indice]))+1
        for val in range(2,l): # i divisori li cerco da 2 a n/2
            if ls[indice]%val==0:
                divisori+=2 #se è divisore
                if ls[indice]/val==val: divisori-=1 #scarto le coppie
        if divisori==0: primi.append(ls[indice]) # se ha 0 divisori propri allora è primo
        if divisori!=k: del(ls[indice]) # se il numero non ha esattamente k divisori propri
    primi.reverse()
    return primi
