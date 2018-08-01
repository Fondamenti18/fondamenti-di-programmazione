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
    primo=[]
    for index,val in enumerate (ls):
        if int(math.sqrt(ls[index]))+1 >1000:
            for y in range(2,int(math.sqrt(ls[index])+1)): 
                if(ls[index]%y==0):
                    count+=2
        else:
            for y in range(2,ls[index]):            
                if(ls[index]%y==0):
                    count+=1 
                            
        if count == 0:
            primo.append(ls[index])
        if(count!=k):                        
            ls[index]=0
        #print(count)
        count=0        
    ls[:] = [x for x in ls if x != 0]
    return primo
        
#ls=[1234579,1234604,1234613,1234641,1234684,1234687,1234793,1234836,1234837,1234847]

#print(modi(ls,6))
#print (ls)

