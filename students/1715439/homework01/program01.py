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
"inserite qui il vostro codice"
from math import sqrt
def numdiv(n):
    divisori=[]
    for x in range(2,int(sqrt(n))+1):
        if n%x==0:
            divisori.append(x)
    return len(divisori*2)

def modi(ls,k):
    primi=[]
    for el in ls:
        a=numdiv(el)
        if a==0:
            primi.append(el)
    for el in ls[:]:
        a=numdiv(el)
        if a!=k:
            ls.remove(el)
    return primi

#ls=[70,330,293,154,128,113,178]
#print(modi(ls,6)) 



    



