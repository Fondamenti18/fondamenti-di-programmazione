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

def modi(ls,k):
        
    
    lista1=[]
    lista2=[]
    
    
    for i in ls:
        var_conta=0
        for n in range (2,int(sqrt(i)) + 1):
            
            if i%n==0:
                var_conta=var_conta+2
                
            else:
                if i==n:
                    var_conta=var_conta+1
           

        if var_conta==0:
            lista1=lista1+[i]
        
        
        
        if var_conta==k:
            lista2=lista2+[i]
        
        

    for index in ls[::1]:
        if (index not in lista2):
            ls.remove(index)
    

    
    for indice in ls[::-1]:
        if (indice in lista1):
            ls.remove(indice)
            
            
    return lista1






     
