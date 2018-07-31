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
    "inserite qui il vostro codice"
    
    ndiv=0
    lspr=[]
    from math import sqrt
    
    for y in ls[:]:

        if y%2==0:
            ndiv=controllo(2,y,ndiv,k,sqrt)
        else:
            ndiv=controllo(3,y,ndiv,k,sqrt)
        
        if ndiv==0: lspr.append(y)
        if ndiv!=int(k): ls.remove(y)
        
        ndiv=0
        
    return lspr
    
def controllo(x,y,ndiv,k,sqrt):
    
    for i in range(x,int(sqrt(y)+1),x-1):
        
        if y%i==0:
            ndiv+=2
            if ndiv>int(k): break
    
    if sqrt(y).is_integer(): ndiv=+1
   
    return ndiv
