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
ls2=[] 
n_divisori=0
ls3=[]
ls4=[]
import copy
import math

def divisori(el):
    n_divisori=0
    radice = math.sqrt(el)
    if el in ls2:
        n_divisori=0
    if radice==int(radice):
        n_divisori+=1
        for y in range(2,int(math.sqrt(el))):
            if el%y==0:
                n_divisori+=2
    else:
        for x in range(2,int(math.sqrt(el))+1):
            if el % x == 0:
                n_divisori+=2
    return n_divisori        

def primo(el):
    for x in range(2,int(math.sqrt(el))+1):
        if (el % x == 0):
            return False
            break
    ls2.append(el)
                    
def modi(ls,k):
    if ls2!=[]:
        ls2.clear()
    ls3=copy.copy(ls)
    for el in ls3:
        n_divisori=divisori(el)
        primo(el)
        if n_divisori == k:
            ls4.append(el)
        else:
            del ls[ls.index(el)]
    return ls2



    

    
       
    
        
            
            
    


    

        

            
