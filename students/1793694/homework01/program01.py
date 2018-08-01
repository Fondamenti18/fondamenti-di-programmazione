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
    lsp=[]
    count=0
    
    for i in range(len(ls)-1, -1, -1):
        for h in range(2,int(math.sqrt(ls[i]))+1):
            if(ls[i]%h==0):
                count+=2
        #print(count)
        #print(ls[i])
        
        if(count==0):
            lsp.append(ls[i])
        if(k!=count):
            del ls[i]
        
            
        count=0
    return lsp[::-1] #reverse solo perche' il grader non dava giusto il risultato poiche' invertito

            
ls=[1234579,1234604,1234613,1234641,1234684,1234687,1234793,1234836,1234837,1234847]
print(modi(ls,6))
print(ls)