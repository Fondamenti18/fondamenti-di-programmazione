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
    count=0
    lp=[]
    #index=0
    for x in range(len(ls) - 1, -1, -1):
        for y in range(2,int(math.sqrt(ls[x])+1)):
            if(ls[x]%y==0):
                count+=2
        #print(count)        
        if(count==0):
            lp.append(ls[x])
        if(count!=k):
            
            del ls[x]
            
        count=0
        #x+=1
    return lp[::-1]

#ls=[340887623,26237927,2491,777923,5311430407,6437635961,82284023]
#print (modi(ls,4))
#print (ls)