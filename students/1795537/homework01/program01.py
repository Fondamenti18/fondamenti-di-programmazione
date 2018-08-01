import math

def n_primi(num):
    '''controllo se il valore è primo'''
    for div in range(2,int(math.sqrt(num))+1):
        if num % div == 0:
            return (False)
    return (True)
    
def c_primi(ls):
    '''passo uno alla volta i valori della lista per vedere quali sono primi'''
    primi = []
    for num in ls:
        if n_primi(num):
            primi = primi +[num]
    return (primi)

def aggiorna_lista(ls, primi):
    '''elimino dalla lista originale i valori primi'''
    ls = [el for el in ls if el not in primi]
    return (ls)

def divisori(n):
    '''calcolo i divisori di un numero dato'''
    fattori = []
    n_ = int(math.sqrt(n))
    for div in range(2, n_+1):
        if n % div == 0:
            fattori += [div] + [n//div]
    for num in fattori:
        espo = fattori.count(num)
        for j in range(1,espo):
            fattori.remove(num)
    return (len(fattori))

def controllo(ls, k):
    '''esamino i vari numeri della lista per vedere chi ha il numero di divisori dato'''
    lista_nuova = []
    for el in ls:
        n_div = divisori(el)
        if n_div == k:
            lista_nuova += [el]
    return (lista_nuova)

def modi(ls, k):
    '''funzione principale'''
    primi = c_primi(ls)
    ls_n = aggiorna_lista(ls, primi)
    lista = controllo(ls_n,k)
    ls.clear()
    ls.extend(lista)
    return (primi)
