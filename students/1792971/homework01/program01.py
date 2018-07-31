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
import math
from math import sqrt,trunc 

def modi(ls,k):
    primi=verifica_primi(ls)
    elimina_elementi(ls,k,primi)
    
    return primi
    
def verifica_primi(ls):
    primi=[]
    for num in ls:
        div=2
        primo=True
        limite=trunc(sqrt(num))
        while div<=limite:
            if num%div==0:
                primo=False
                div=num
            else:
                div+=1
        if primo==True:
            primi+=[num]
    return primi

def elimina_elementi(ls,k,primi=[]):
    i=0
    while i<len(ls):
        if k!=0 and ls[i] in primi:
            ls.pop(i)
        elif divisori(ls[i],k)!=k:
            ls.pop(i)
        else:
            i+=1
        
def divisori(num,k):
    div=2
    num_div=0
    limite=trunc(sqrt(num))
    while div!=limite and num_div<=k:
        if num%div==0 and num%(num//div)==0:
            num_div+=2
        div+=1
    return num_div