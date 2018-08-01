'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[441,16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def modi(ls,k):
    ls1=[]
    ls1=ls[:]
    lista2=[]
    for el in ls1:
        if numprimo(el)==True:
            lista2+=[el]
            if k==0:
                pass
            if k!=0:
                ls.remove(el)
    
        else:
            if divisori(el,k)==False:
                ls.remove(el)
    
    return lista2

from math import sqrt

def divisori(el,k):
    lista3=[]
    
    for i in range(2,int(sqrt(el))+1):
        
        if el%i==0:
            lista3.append(i)
            
            lista3.append(1)
           
        elif el/i==i:
            lista3.append(i)
                
    if len(lista3)==k:
        return True
    else:
        return False
    
        
        
def numprimo(x):
    if x==2 or x==3:
        return True
    if x%2==0:
        return False
    for i in range(3, int(sqrt(x)+1)):
        if x%i==0:
            return False
    return True


        
    
        
    
