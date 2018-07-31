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
def div(h,k):
    x=2
    l_divisori=[]
    met=int(math.sqrt(h)+1)
    while x<=met:
        if h%x==0:
            l_divisori+=[x]
            l_divisori+=[x]
            if(len(l_divisori)>k):
                break;
        x+=1
    return l_divisori

def modi(ls, k):
    i=0
    listaprimi=[]
    while i<len(ls):
        ndiv=div(ls[i],k)
        if len(ndiv)==0:
            listaprimi+=[ls[i]]
            del(ls[i])
            i=i-1
        elif len(ndiv)!=k:
            del(ls[i])
            i= i-1
        i=i+1
    return listaprimi