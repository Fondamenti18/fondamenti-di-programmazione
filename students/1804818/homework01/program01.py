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
    ls_primi=[]
    ls_non_primi=ls[:]
    for N in ls_non_primi:
        contatore=0
        if N>1000:
            alcuni_primi=[2, 3, 5, 7, 11, 13, 17, 19]
            N_1=N
            for el in alcuni_primi:
                if N_1%el==0:
                    while N_1%el!=0:
                        N_1=N_1//el
                        contatore+=1
                        break
            for i in range(2, (N_1//2)+1):
                if N%i==0:
                   contatore+=1
        else:
            for i in range(2, (N//2)+1):
                if N%i==0:
                    contatore+=1
        if contatore==0:
            ls_primi+=[N]
        if contatore!=k:
            ls.remove(N)
            
            
    return ls_primi




