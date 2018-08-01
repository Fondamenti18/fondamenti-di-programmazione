'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls =[121, 4, 37, 441, 7, 16]   
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''
def divisori(l,b):
    conta=0
    c=2
    import math
    a=math.sqrt(l)
    while conta<=b and c<=math.ceil(a):
        if l%c==0:
            if l/c==c:
                conta+=1
                return conta
            conta+=2
        c+=1
    return conta
def modi(ls,k):
    listaprimi=[]
    listak=[]
    for i in ls:
        if divisori(i,k)==0:
            listaprimi+=[i]
        if divisori(i,k)==k:
            listak+=[i]
    ls[:]=listak
    return listaprimi

    
            
        
            
        
    
