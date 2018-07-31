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
    "inserite qui il vostro codice"
    primi=[]
    listacopia=[]
    for el in ls:
        risultato=check(el)
        if risultato:
           primi.append(el) 
    for el in ls:
        if not (el in primi):
            risultato=conta(el)
            if risultato==k:
                listacopia.append(el)
    ls[:]=listacopia[:]
    return primi
    
def check(el):
    risultato=True
    from math import sqrt
    radice=int(sqrt(el))
    for x in range(2,radice+1):
        if el%x==0:
            risultato=False
            break
    return risultato    
            
def conta(el):
    risultato=1
    x=2
    while el>1:
        esponente=1
        while el%x==0:
            esponente+=1
            el=el/x
        x+=1
        risultato=risultato*esponente
    risultato=risultato-2
    return risultato
        

