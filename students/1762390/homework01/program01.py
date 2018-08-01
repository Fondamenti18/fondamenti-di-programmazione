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


def modi(ls,k):
    lista_primi=[]                            # creo una lista vuota per i numeri primi
    for x in ls:
        if(x%2!=0):                           # verifico se l'elemento è divisibile per due
            isPrime=True
            for y in range(3,int(x/2)):       # verifico i numeri interi partendo da tre
                if(x%y==0):    
                    isPrime=False
                    break
            if(isPrime==True):                # se è primo si copia nella lista_primi
                lista_primi.append(x)

    for z in lista_primi:                     # ogni elemento copiato nella lista_primi viene rimosso 
        ls.remove(z)                          # dalla lista presa in input
    
    lista_temp=ls[:]
    
    
    for t in lista_temp:                      # creo un altra lista in cui mettere tutti i divisori degli   
        occorrenze=0                          # elementi della lista presa in input
      
        
        for y in range(2,int(t/2)+1):         # si contano tutti i divisori partendo dal numero due   
            if(t%y==0):                       #  fino alla metà, se il numero dei divisori supera o è 
                occorrenze+=1                 #  inferiore alla cifra k passata in input cancella l'elemento      
                                              # dalla lista.
            if(occorrenze>k):
             
                break
        if(occorrenze!=k):
            ls.remove(t)
    
    
    return lista_primi
