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
    c = [] + ls
    contatore = -1
    lunghezza_ls= len(c) -1
    contatore2 = -1
    import math
    primi = []
    while contatore < lunghezza_ls:
        contatore2 = contatore2 +1
        contatore = contatore + 1
        lista2 = c[contatore]
        b = int(math.sqrt(lista2)) + 1
        lista = []
        lista3 = []
        lista4 = []
        for i in range (2,b):
            if lista2 % i == 0:
                lista3 = lista3 + [i]
                lista4 = lista4 + [int(lista2 / i)]
        lista = lista3 + lista4
        soluzione = len(lista)
        if soluzione == 0:
            primi = primi + [lista2]
            del ls[contatore2]
            contatore2 = contatore2 -1
        elif soluzione != k:
            del ls[contatore2]
            contatore2 = contatore2 -1
    return (primi)
