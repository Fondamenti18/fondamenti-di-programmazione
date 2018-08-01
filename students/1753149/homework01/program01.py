'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[441,16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def modi(ls,k):
    "inserite qui il vostro codice"
    lista=[]
    lista_primi=[]
    for i in ls:
        if divisori(i)-2!=k:
            lista.append(i)
        if divisori(i)==2:
            lista_primi.append(i)
    for i in lista:
        if i in ls:
            ls.remove(i)
    return lista_primi

def divisori(m):
    l=2
    b=1
    g=m
    while l<(m**0.5)+1:
        x=0
        while g%l==0:
            g/=l
            x+=1
        b*=x+1
        l+=1
    if g>1:
        b*=2
    return b
