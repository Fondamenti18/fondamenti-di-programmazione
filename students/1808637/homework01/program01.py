# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:25:59 2017

@author: utente
"""

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
    ls2=[]
    ls3=[]
    from math import sqrt
    for i in ls:
        cont=0
        for x in range (2, int(sqrt(i))+1):
            if (i%x)==0:
                if (i%(i/x)==0) and i/x!=x:
                    cont=cont+1
                cont=cont+1
        if (cont==0):
            ls2.append(i)
        if (cont==k):
            ls3.append(i)
    ls.clear()
    ls+=ls3
    return ls2