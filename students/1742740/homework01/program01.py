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


import math


def divisori(numero):   #funzione che torna il numero di divisori di un numero
    lista_divisori = []
    massimo = int(math.sqrt(numero)) + 1   #il range e' la radice quadrata del numero in input
    divisore = 2
    while divisore <= massimo:
        if numero % divisore == 0:
            lista_divisori.append(divisore)
            if (numero / divisore) != divisore:  #se il numero non e' quadrato del divisore aggiunge sia il divisore che il quoziente
                lista_divisori.append(int(numero / divisore))
        divisore += 1
    return len(lista_divisori)


def modi(ls, k):
    primi = []
    i = 0
    while i < len(ls):
        conta = divisori(ls[i]) #richiama la funzione divisori(numero)
        if conta == k:  #se il valore e' da tenere lo lascia in ls
            i += 1
        elif conta != k and conta == 0: #se e' primo lo aggiunge a primi e lo toglie dalla lista
            primi.append(ls[i])
            ls.remove(ls[i])
        else:
            ls.remove(ls[i]) #se non ha esattamente k divisori lo toglie da ls
    return primi
