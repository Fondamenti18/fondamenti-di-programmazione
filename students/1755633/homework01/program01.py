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



import math  #importo libreria math


#ls = [121, 4, 37, 441, 7, 16] 
#k=3 
def modi(ls,k):
    lsf=[] 
    lu=0

    while(lu<(len(ls))):   #finche non raggiungo l 'ultimo elento della lista      
         n=int(ls[lu])
         #d=2
         a=0                   
         af=1  
         
#############
         y=0
         primo=True
################dispari
         #rad=int(math
         if (ls[lu]%2)!=0:    #se numero dispari
             rad=int(math.sqrt(ls[lu]))                            
             for y in range(2,rad+1):
                 if(ls[lu]%y)==0:
                    primo=False 
                    break    #se non è primo esce
                
             if primo==False: #se non è primo controlla i divisori
                 
                 d=3                                                                            
                 while ((n>=d)or((af-2)==k)):      #scompongo il numeri con (d disparo)calcolando i divisori, af=divisori        
                       if(n%d==0):                                                                               
                          a=a+1 

                          if(n==d):
                             a=a+1
                             #d=d+1
                             af=((af*a)-2) 
             
                          n=int(n/d) 
               
                       else:
                          a=a+1
                          d=d+2
                          af=af*a
                          a=0                          
               



         print('af: di', ls[lu] ,af)               
         
         if(ls[lu]%2)==0:    #se num pari
             primo=False
             d=2                              
             while ((n>=d)or((af-2)==k)):            #ripeto scomposizione del numeri calcolando i divisori, af=divisori          
                       if(n%d==0):                                                                               
                          a=a+1 

                          if(n==d):
                             a=a+1
                             #d=d+1
                             af=((af*a)-2) 
             
                          n=int(n/d) 
               
                       else:
                          a=a+1
                          d=d+1
                          af=af*a
                          a=0

         
         if(af==0) or primo==True:  #se i divisori sono uguali a k oppure se ls[li] è primo
            lsf.append(ls[lu]) #aggiungiamo ai numeri primi ls[lu]
            ls.remove(ls[lu])  #rimuoviamo dalla lista il numero primo
            lu=lu-1               
            
         elif(af!=k):
            ls.remove(ls[lu])   #rimuoviamo dalla lista il numero primo
            lu=lu-1              #decremento indice, cause spostamento -1 per via del .remove
       
         lu=lu+1  #incremento il contatore indice
         
    print('La lista con i numeri primi e\'',(lsf))  
    print('Lista contenente solo gli interi che hanno esattamente ',k,' divisori propri',(ls))
    return lsf



#modi(ls,k)

