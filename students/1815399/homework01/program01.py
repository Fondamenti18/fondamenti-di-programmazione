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
    
    
    primi=[]
    j=0
    while j < len(ls):
        
        i=2
        contadivisori=0
        while i <= math.sqrt(ls[j]) :
            if ls[j] % i == 0:
                contadivisori+=1
            i+=1
        if math.sqrt(ls[j])% 1 == 0.0:
           contadivisori= (contadivisori*2)+1
        else: 
            contadivisori= contadivisori*2
        
        
        if contadivisori != k:
           if contadivisori == 0:
               primi.append(ls[j])
           ls.pop(j)
           
        
        else:
            j+=1
        
            
       
               
    
    return primi
    
   
    
            
    

            
        



                
