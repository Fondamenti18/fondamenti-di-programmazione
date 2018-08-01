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

def div_counter(n):
    
    div_count = 0
    for x in range(2,int(n**(1/2)+1)):
        if n%x == 0:
            if x == n**(1/2):
                div_count += 1
            else:
                div_count += 2
    return div_count

def isprimenumber(n):
    
    k = 2
    prime = True
    while k<=(int(n**(1/2))) and prime:
        if n%k == 0:
            prime = False
        else:
            k += 1
    return prime

def modi(ls,k):
    
    ls_prime = [x for x in ls if isprimenumber(x)]
    ls[:] = [x for x in ls if div_counter(x) == k]           
    return ls_prime
    return ls

