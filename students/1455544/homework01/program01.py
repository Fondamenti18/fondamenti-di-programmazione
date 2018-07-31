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


def modi(ls, k):
    "inserite qui il vostro codice"
    lista_divisori = []
    lista_primi = []
    lista_rimozione = []
    for i in range(0, len(ls)):
        divisori = check_divisori(ls[i], k)
        if not divisori == k:
            lista_divisori.append(ls[i])
        if check_primo(ls[i]):
            lista_primi.append(ls[i])
    for i in range(0, len(lista_divisori)):
        ls.remove(lista_divisori[i])
    return lista_primi


def check_divisori(num, k):
    divisori = 0
    for i in range(2, int(num/2+1)):
        if num % i == 0:
            divisori += 1
        if divisori > k:
            break
    return divisori


def check_primo(num):
    if num > 2 and num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True
