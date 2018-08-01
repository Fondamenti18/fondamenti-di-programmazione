'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno
e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori
    propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121,4,37,441,7,16]
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine
della funzione si avra' che la lista ls=[441,16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio
dell'esercizio e' zero.
'''


def modi(ls,k):
    "inserite qui il vostro codice"
    l=[]
    l1=[]
    for i in ls:
        if divisori(i,k)==0:
            l+=[i]
        if divisori(i,k)==k:
            l1+=[i]
    del ls[:]
    ls+=l1
    return l



def divisori (n,k):
    cont=0
    for x in range(2,int(n**0.5)):
        if n%x==0:
            cont+=2
            if cont==k+2:
                break
    if n%int(n**0.5)==0:
        cont+=1
    return cont





		






