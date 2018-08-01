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

def primi(ls):
    prim=[]
    for i in ls:
        cont=0
        for j in range(2,i):
            if i%j==0:
                cont+=1
                break
        if cont==0:
            prim+=[i]
    return prim
    

def modi(ls,k):
    "inserite qui il vostro codice"
    div=0
    primo=primi(ls)
    for i in ls:
        if i in primo:
            ls.remove(i)
    for t in ls:
        
        for j in range(2, t):
            if t%j==0:
                div+=1
                if div>k:
                    break
        if div!=k:
            ls.remove(t)
    return primo,ls