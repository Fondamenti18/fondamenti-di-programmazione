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
    
        listaNumeriPrimi = []
        variabile = 0

        if k > 0:
                while variabile <= len(ls) - 1:
                    
                        if numerodivisori(ls[variabile]) == 0:
                                listaNumeriPrimi.append(ls[variabile])
                                del ls[variabile]

                        if numerodivisori(ls[variabile]) != k:
                                del ls[variabile]
                                variabile -= 1

                        variabile += 1

                return listaNumeriPrimi

def numerodivisori(variabile):

        a = []
        n = round(sqrt(variabile)) + 1

        for i in range(2, n):
                if variabile % i== 0:
                        a.append(i)
                        a.append(variabile//i)
        return len(a)
        


        
        

        
    

            

            


            
            
                
                    
            
                    

        
                
                



        
        
        
        
        
        
   
   

    
    
