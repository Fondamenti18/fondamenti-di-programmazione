'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txtf

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''
from math import sqrt
def modi(ls,k):
    lista1=[]
    lista2=[]
    '''ciclo che permette lo scorrimento dei valori in ls'''
    for i in ls:
        C=0
        '''secondo ciclo che scorre il range di valori (i//2+1)
        per trovare i divisori di i '''
        for x in range(2,int(sqrt(i)+1)):
            if i%x==0:
                if i//x!=x:
                    C+=2
                if i//x==x:
                    C+=1
        if C==k:
            lista2+=[i]
        if C==0:
            lista1+=[i]
    ls.clear()
    ls+=lista2
    return lista1,ls

