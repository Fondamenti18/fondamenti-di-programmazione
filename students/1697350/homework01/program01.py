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

'''
caro prof, se uso nella versione python3 xrange() è diventato range() e gestisce lui la memoria. se esegui il gradle con range funziona tutto bene, il problema lo da sul server suo quando esegue questo script python. forse dovrebbe fare python3 program01.py
In locale se eseguo python program01.py il pc mi si blocca completamente, problema di memory. se eseguo python3 no. buonaserata.
'''

def divisori(x, k):
    num = 0
    for i in range(2,x):
        if x % i == 0:
            num += 1
            if num > k:
                return False
    if num == k:
        return True
    return False

def isNumeroPrimo(x):
    if x == 2:
        return True
    
    if x % 2 == 0:
        return False
    
    for i in range(3, int(x**0.5)+1,2):
        if x % i == 0:
            return False
    return True
    
def modi(ls,k):
    ls_primi = [x for x in ls if isNumeroPrimo(x)]
    ls2 = [x for x in ls if divisori(x,k)]
    ls[:] = [x for x in ls2]
    return ls_primi
