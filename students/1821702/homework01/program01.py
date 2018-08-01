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

def divisori(i,k):
    x = 0
    n = 2
    while n<=int(i**(1/2)) and x<=k:
        if i%n == 0:
            if n == i**(1/2):
                x += 1
            else:
                x +=2 
        n +=1
    return x

def modi(ls,k):
    primi = []
    i = 0
    while i<len(ls):
        if ls[i] == 0 or ls[i] == 1:
            if k>0:
                del ls[i]
            else:
                i +=1
        else:
            x = divisori(ls[i],k)
            if x!=k:
                if x == 0:
                    primi.append(ls[i])
                del ls[i]
            else:
                i +=1
    return primi