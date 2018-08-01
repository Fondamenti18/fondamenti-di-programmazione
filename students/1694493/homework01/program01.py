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


def numero_primo(n):
    limite = math.floor(math.sqrt(n)+1)
    for i in range(2,limite):
        if n%i==0:
            return False
    return True

def divisori_propri(n):
    divisori = []
    limite = math.floor(math.sqrt(n)+1)
    
    for x in range(2,limite):
        if n%x==0:
            if x not in divisori:
                divisori.append(x)
                if (int(n/x)) not in divisori:
                    divisori.append(int(n/x))
        
    return divisori

def modi(ls,k):
    numeriprimi = [] 
    for n in ls[:]:
        divisori = divisori_propri(n)
        if numero_primo(n) == True:
            numeriprimi.append(n)
            
        if len(divisori)!=k:
            ls.remove(n)
    return numeriprimi

    


            