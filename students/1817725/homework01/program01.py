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

ls=[16,40,8,17,19,30,20]
k=3
from math import *
def d(n):
        divisori = []
        x=ceil(sqrt(n)+1)
        for div in range(2,x):
                if n % div == 0:
                        divisione= n//div
                        divisori.append(div)
                        divisori.append(divisione)
                        for c in divisori:
                                if divisori.count(c)>1:
                                        divisori.remove(c)
        return divisori
	
def modi(ls,k):
        pl=[]
        for i in ls:
                y=d(i)
                if len(y) == 0:
                        pl+=[i]
	
        kDivisori = []
        for i in ls:
                y = d(i)
                if len(y) == k:
                        kDivisori += [i]
                        
        ls[:]=kDivisori
        return pl


print(modi(ls,k))
