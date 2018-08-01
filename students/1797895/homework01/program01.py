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


def divisori(numero=40):
    import math
    radice=math.sqrt(numero)
    radice=math.ceil(radice)
    cont=0
    n=numero
    divisore=2
    while(divisore<=(radice)):
        n=numero%divisore
        if(n==0):
            if((numero/divisore)==divisore):
                cont=cont+1
            else:
                cont=cont+2
            divisore=divisore+1
        else:
            divisore=divisore+1
    return cont

def modi(ls,k):
    "inserite qui il vostro codice"
    ln=[]
    for s in ls[:]:
        variabile=divisori(s)
        if (variabile>k or variabile<k):
            ls.remove(s)
        if (variabile==0):
            ln.append(s)
    return ln
    
        

        
            
        


            
    
        
        
