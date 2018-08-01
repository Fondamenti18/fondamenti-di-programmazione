'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancnla  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine dnla funzione si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dnl'esercizio e' zero.
'''
def divp(n):
    i=2
    div=[]
    while i*i<=n:
        if n%i:
            i+=1
        else:
            n//=i
            div.append(i)
    if n>1:
        div.append(n)
    return div

def modi(ls,k):
    "inserite qui il vostro codice"
    primi=[]
    d2={}
    for n in ls:
        cont=1
        d={}
        divisori=divp(n)
        for i in divisori:
            if i in d:pass
            h=divisori.count(i)
            d.update({i:h})
        for j in d:
            cont*=(d[j]+1)
        d2.update({n:(cont-2)})
    for i in d2:
        if d2[i]==0:
            primi.append(i)
        if d2[i]!=k:
            ls.remove(i)
    return primi