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
import copy
def modi(ls,k):
    "inserite qui il vostro codice"
    nradqu=0
    lsprimi=[]
    ls2= copy.deepcopy(ls)
    
    for i in ls2:
        
        nradqu=sqrt(i)
        nradqu=round(nradqu)
        ultimodi=False
        divisori=0
        for x in range (2,nradqu+1):
            if i%x==0:
                divisori+=1
            if x==nradqu and x%i==0:
                ultimodi=True
                
        if divisori==0:
            lsprimi+=[i]
       
        elif ultimodi==True:
             divisori=(divisori*2)-1
        elif ultimodi==False:
             divisori=(divisori*2)
               
        if divisori!=k:
            ls.remove(i)
            
        
    return(lsprimi)
