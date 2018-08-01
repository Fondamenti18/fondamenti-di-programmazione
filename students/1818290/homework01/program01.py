'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''
ls=[70,330,293,154,128,113,178]
k=6
def modi(ls,k):
    primi=[]
    i=0
    while i<len(ls):
        if contadivisori(ls[i], primi, k)!=k:
            del ls[i]
            i=-1
        i+=1
    return primi
        
            
def contadivisori(x, primi, k):
    i=1
    d=-1
    c=x//2
    while i<c:
        if x%i==0:
            d+=1
        if x%c==0:
            d+=1
        if d>k:
            i=c+1
        i+=1
        c-=1
    if d==0:
        primi+=[x]
    return d