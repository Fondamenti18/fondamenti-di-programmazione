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
    if k < 0:
        return('''Non è possibile eseguire l'operazione con k negativo''')
    primi = []
    lista = []
    for x in ls:
        lista += divisori(x,k)
        primi += [primo(x)]
        primi = [x for x in primi if x != 0]
    ls[:] = lista
    #print(ls)
    return primi

def divisori(x,k):
    '''Funzione per calcolare il numero di divisori propri, esclusi l'uno e il numero stesso'''
    contatore = 0
    lista_finale = []
    y = x
    if len(str(x)) > 7:
        y = int(x**0.5)+1
    for i in range(2,y):
        if x % i == 0:
            contatore += 1
        if k < contatore:
            pass
    if contatore == k :
        lista_finale += [x]
    return lista_finale

def primo(x):
    '''Funzione per calcolare se un numero è primo'''
    for i in range(2,x//2+1):
        if x % i == 0:
             return 0
    return x


