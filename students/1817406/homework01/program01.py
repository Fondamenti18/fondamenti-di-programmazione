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


"inserite qui il vostro codice"
ls = [121, 4, 37, 441, 7, 16]
k=3
def x_primo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def modi(ls, k):
    lista_k = modi_2(ls)
    #crea la lista vuota per mettere i numeri primi
    lista_primi = []
    for x in ls:
        i = x - 1
        acc = 0
        #definiamo la condizione per i numeri primi:
        while i > 1 and acc <= k:
            resto = x % i
            i -= 1
            if resto == 0:
                acc += 1
        if acc == k:
            lista_primi = lista_primi + [x]
    return lista_primi, lista_k


def modi_2(ls):
    lista_k = []
    #crea un'altra lista vuota per mettere i numeri con k divisori
    for x in ls:
        if x_primo(x):
            lista_k = lista_k + [x]
    return lista_k


ls, lista_k = modi(ls, k)
print(ls)
print(lista_k)
