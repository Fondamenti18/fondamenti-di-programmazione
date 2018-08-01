'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[441,16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def conta_divisori(n):
    c=0 
    a=2
    Dmax=n//2
    while a<=Dmax :
        if (n%a)==0:
#            print(a)
            c=c+1
        a= a +1
    return c
#    if c==0:
#        print ('il numero è primo')
#    else:
#        print('il numero non è primo')


def modi(ls,k):
    lp=[]
    lt=[]
    if k>=0:
        for el in ls:
            if conta_divisori(el)==k:
                lp.append(el)
            if conta_divisori(el)==0:
                lt.append(el)
        print(lp)
        print(lt)
    else:
        print('Non accettabile poichè k non è maggiore o uguale a zero')
        
    
    
    
    
   
    
    
        
        


            
            
            
            
            
            
    
