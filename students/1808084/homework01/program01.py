# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:53:53 2017

@author: Lorenzo
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
    from math import sqrt
    primi=[]
    fatt= 0
    rad = []
    con =  []
    for x in range(len(ls)-1,-1,-1):
        fatt = 0
        rad = int(sqrt(int(ls[x])))+1
        for z in range(2,rad):
            con = int(ls[x]) % int(z)
            if con == 0:  
                fatt+=1
            else:
                pass
        fatt = fatt *2
        if fatt == 0:
            primi.append(ls[x])
        if fatt != k:
            del ls[x]
    primi.reverse()    
    return(primi)


