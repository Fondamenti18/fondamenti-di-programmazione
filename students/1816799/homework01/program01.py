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
    lsprimi=[]
    for i in ls:
        if primi(i)!=k:
            ls1.append(i) 
        if primi(i)==0:
            lsprimi.append(i) 
    for i in ls1:
        if i in ls: 
            ls.remove(i)
    return lsprimi
    
def primi(n):
    j=2
    a=1
    h=n
    while j<radice(n):
        x=0
        while h%j==0:
            h/=j
            x+=1
        a*=x+1
        j+=1
    if h>1:
        a*=2
    return a-2 

def radice(n):
    n=(n**0.5)+1
    return n      
    

