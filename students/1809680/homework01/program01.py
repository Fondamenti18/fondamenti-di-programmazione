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

from math import sqrt
def modi(ls,k):
    lista_primi=[]
    for i in range(len(ls)):
        n_div=divisori_propri(ls[i]) #assegnamento numero di divisori propri degli elementi di ls con indice i
        if n_div==0:
            lista_primi.append(ls[i])  #aggiunta numeri primi
    for i in range(len(ls)-1,-1,-1):
        if divisori_propri(ls[i])!=k:
            del ls[i]
    return lista_primi
    
def divisori_propri(num):
    num_divisori=0
    for i in range(2, int(sqrt(num))+1):
        if num%i==0:
            num_divisori+=2
    return num_divisori
    
        
        
           
           
        