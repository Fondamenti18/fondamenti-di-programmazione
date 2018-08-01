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
    lstPrimo = []  # lista di numeri primi
    for n in reversed(ls):   
        Div = Divisori(n,k)
        if Div == 0 :
            lstPrimo.insert(0,n)
            
        if Div != k: # rimuovo chi non ha k divisori
            ls.remove(n)
            
    return lstPrimo
    
def Divisori(num,maxDiv):
    # funzione che calcola i divisori di un numero 
    fattx = 2  # inizializzo al primo fattore 
    import math
    rd = int(math.sqrt(num)) 
    div=0
    while (fattx <= rd and (div*2)<=maxDiv):   
        if num % fattx == 0:
            div+=1 
        fattx+=1
        
    return div *2