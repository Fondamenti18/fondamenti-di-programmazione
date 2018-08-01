'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno
 e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un 
intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k 
    divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine 
della funzione si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio 
dell'esercizio e' zero.
'''



def modi(ls,k):
    from math import sqrt
    listaNP=[]  #lista numeri primi
    listaNDP=[]  #lista dei non divisori propri
       
    def FattoriPrimi(n):
    #restituisce i fattori primi di un numero n con ripetizioni
      i = 2
      while i<=sqrt(n):
        if n%i==0:
            l = FattoriPrimi(n/i)
            l.append(i)
            return l
        i+=1
      return [n] 

    #inizio ciclo per ogni elemento di ls
    for z in range(0, len(ls)):
         lista=FattoriPrimi(ls[z])
         lista_no_rip= list(set(lista))
         #restituisce fattori primi senza ripetizioni
         if len(lista)==1:
             listaNP=listaNP+[ls[z]]
         #ha trovato numeri primi e li aggiunge a listaNP
     
         esp=[0]*len(lista_no_rip)
         num_div=1
         for j in range(0,len(lista_no_rip)):
             esp[j]=lista.count(lista_no_rip[j])+1
             num_div=num_div*esp[j]
         num_div=num_div-2
#         per trovare quanti fattori ha un elemento ls[j] ho usato una formula
#         che si basa sugli esponenti dei fattori primi
         
         if num_div != k:
             listaNDP=listaNDP+[ls[z]]
         
    #fine ciclo per ogni elemento di ls
    
    #elimino dalla lista ls i numeri con il numero fattori diversi da k
    for m in range(0,len(listaNDP)):   
        dd=listaNDP[m]
        ls.remove(dd)
    
    return listaNP   
    




       
    
        
    
    






    
      
    
    
    
    
        
        
    
        
   
