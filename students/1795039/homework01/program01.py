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


    numerodivisori = []
    primi = list(ls)            
    indice = -1

    while indice != len(ls)-1:
        indice += 1
        numero = ls[indice]
        divisori = 0
        i = 1
        divisori = ciclo(i,numero,k,divisori)
        numerodivisori.append(divisori)

    return calcoladivisori(ls,k,numerodivisori,primi)

def ciclo(i,numero,k,divisori):

    while i*i <= int(numero):
        if divisori > k+2:
            break
        divisori= condizioni(divisori,k,numero,i)
        i += 1
        
    return divisori

def condizioni(divisori,k,numero,i):

    if numero % i == 0:
        divisori += 1
        if numero/i != i:
            divisori +=1
            
    return divisori

    
def calcoladivisori(ls,k,numerodivisori,primi):

    indice = len(ls)
    
    while indice != 0:
        indice -=1
        if numerodivisori[indice] != k+2:
            del(ls[indice])

    return calcolaprimi(ls,k,numerodivisori,primi)

def calcolaprimi(ls,k,numerodivisori,primi):

    indice = len(primi)
    while indice != 0:
        indice -= 1
        if numerodivisori[indice] > 2:
            del(primi[indice])

    return primi





