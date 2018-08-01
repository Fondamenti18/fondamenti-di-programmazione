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
    finale = []
    
    
    for n in ls.copy():
        dvs_prop = 0
        divisori = []
        
        m = int(math.sqrt(n))
        
        while m > 1:
            
            if n%m == 0:
                dvs_prop += 1
                divisori.append(m)
                
                if dvs_prop > k:
                    break;
            m -= 1
        for el in divisori.copy():
            for num in divisori.copy():
                prod = el*num
                if n%prod == 0:
                    if prod not in divisori and prod != n:
                        divisori.append(prod)
                        dvs_prop += 1
                
        if dvs_prop!= k:
            if dvs_prop == 0:
                finale.append(n)
            ls.remove(n)
            
    return finale