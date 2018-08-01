
'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 441, 37, 16]
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione
si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def num_divisori(n):
    rad= int(n**0.5)
    divisori=0
    if n%(rad)==0: divisori=1
    for d in range(2,rad):
        if n%d==0:
            divisori+=2
    return divisori

def primo(n):
    rn = int(n**0.5)+1
    if n==2: return n
    for i in range(2,rn):
        if (n%i==0): return False
    return n

def rimuovi_primi(ls1,ls_primi):
    for n in ls_primi:
        ls1.remove(n)

def modi(ls,k):
    lista_primi = list(filter(primo,ls))
    rimuovi_primi(ls,lista_primi)
    ls2 = ls.copy()
    for num in ls2:
            n_div=num_divisori(num)
            if n_div!=k: 
                ls.remove(num)
    return lista_primi











