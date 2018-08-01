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
        ls1=[]
        ls2=[]


        for a in ls:
                stri=factors(a)
                lung=len(stri)
                if lung==k:
                        ls2.append(a)
                elif lung==0:
                        ls1.append(a)
        ls[:]=ls2
        return ls1


from math import sqrt


def factors(b):
        factors= set()
        for c in range(2, int(sqrt(b))+1):
                if b%c==0:
                        factors.add(c)
                        factors.add(b//c)
        return sorted(factors)
                



    
