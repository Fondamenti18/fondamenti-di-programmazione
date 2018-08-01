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
    
    "inserite qui il vostro codice" 
     
    listaNumeriPrimiRestituiti = []
      
    listanumeri = ls[:]
    
    k = k / 2
    
    for numero in listanumeri:
            
            divisore = 2
            
            numerodivisori = 0

            while divisore <= sqrt(numero):
               
                if (numero % divisore == 0):
                    
                    numerodivisori += 1
                                    
                if numerodivisori > k:
                    
                    break
                
                divisore += 1
                   
            #Se i divisori sono 0 (escludendo 1 ed il numero stesso) significa che il numero e primo
         
            if numerodivisori == 0:
                
                listaNumeriPrimiRestituiti.append(numero)
                
                ls.remove(numero)
                
            else:
                
                if numerodivisori != k:
                
                    ls.remove(numero)
    
   
    return listaNumeriPrimiRestituiti
