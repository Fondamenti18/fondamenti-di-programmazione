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
    
    lso=[]
    elim=[]
    
    for c,n in enumerate(ls):
        d=0
        
        ''' numero primo '''
        p=1
        for i in range(2,int(math.sqrt(n)+1)): 
            if n%i==0:
                p=0
          
        ''' se è primo '''
        if p==1: 
            lso=lso+[n]
        
        else:
            ''' conta divisori '''
            for i in range(2,n//2+1): 
                if n%i==0:
                    d=d+1 
                if d>k:
                    break 
            
        ''' se il numero ha k divisori '''
        if d!=k: 
            elim=elim+[c]     

        
    
    for v,i in enumerate(elim):
        del ls[i-v]
      
        
            
    return lso

print(modi([70,330,293,154,128,113,178],6))