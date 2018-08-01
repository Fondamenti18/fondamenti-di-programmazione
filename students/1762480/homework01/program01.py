'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso,
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls,
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri,

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[441,16]

Per altri  esempi vedere il file grade,txt

ATTENZIONE: NON USATE LETTERE ACCENTATE,
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero,
'''

def modi(ls, k):
    numeriprimi= []
    cont = 0
    i = 0
    check = 0
    
    while True:
        num = ls[cont]
  
        divisore = num-1
        while divisore >= 2 :
            if num%divisore == 0:
                break
            else:
                divisore = divisore-1
            if divisore == 2:
                numeriprimi[i] = num
                i = i+1

        if cont<=6:
            cont = cont+1
        else:
            break
            


