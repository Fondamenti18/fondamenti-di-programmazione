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
def divisori(x):
    divisori = []
    y = 1
    while y <= math.sqrt(x):
        if x % y == 0:
            divisori.append(y)
            divisori.append(int(x / y))
        y += 1
    return len(divisori)-2

def primo(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def lista_primi(l):
    lst=[]
    for i in l:
        if primo(i)==True:
            lst.append(i)
    return lst

def modi(ls,k):
    lc=ls.copy()
    for i in lc[:]:
        if divisori(i)!=k:
            ls.remove(i)
    return lista_primi(lc)