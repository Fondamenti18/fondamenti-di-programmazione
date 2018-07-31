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
    e=0
    lsp=[]
    
    for d in ls[:]:
        c=0
        x=2
        y=1
        if d%2!=0:
            x=3
            y=2

        fdiv=div(d,c,x,y,k)
            
        if fdiv==k:
            e+=1
        elif fdiv==0:
            lsp.append(ls[e])
            del(ls[e])
        else:
            del(ls[e])
            
    return lsp

def div(d,c,x,y,k):
    import math
    
    for i in range(x,int(math.sqrt(d)+1),y):
        if d%i==0:
            c+=2
        elif c>k:
            break
        if math.sqrt(d)%int(math.sqrt(d))==0:
            c-=1
            
    return c
