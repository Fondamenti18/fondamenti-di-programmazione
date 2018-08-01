'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne
l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della
funzione si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.'''

from math import sqrt


def modi(ls,k):
        lsp=[]
        x=0
        if k>0:
                while x<=len(ls)-1:
                        if numerodivisori(ls[x])==0:
                                lsp.append(ls[x])
                                del ls[x]
                        if numerodivisori(ls[x])!=k:
                                del ls[x]
                                x-=1
                        x+=1
                return lsp


def numerodivisori(x):
        return len(set([x//i for i in range(2, round(sqrt(x))+1) if x%i==0]+[i for i in range(2, round(sqrt(x))+1) if x%i==0]))

                
                
        
