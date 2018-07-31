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
    "inserite qui il vostro codice"
    listaNumeriPrimi=[]
    ls2=ls[:]
    


    for indice in ls2:
            numeroDivisori=0
            contatore=2
            limite=int(math.sqrt(indice))+1
            while contatore<limite and numeroDivisori<k+1:
                
                if(indice%contatore==0):
                    numeroDivisori+=1
                    if(indice/contatore!=contatore):
                         numeroDivisori+=1
                contatore+=1
                    
            
    
            if(numeroDivisori==0):
                listaNumeriPrimi.append(int(indice))
            if(numeroDivisori!=k):
              
               ls.remove(indice)
               
    return listaNumeriPrimi        
    