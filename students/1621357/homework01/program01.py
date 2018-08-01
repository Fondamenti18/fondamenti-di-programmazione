import math

def divisori2(n) :
    i = 1
    k = 0
    while i <= math.sqrt(n) + 1:
        if (n % i == 0) :
            if n/i == i:
                k = k + 1
            else:
                k = k + 2
        i = i + 1
    return k

def modi(ls,k):
    i = 0
    lista = []
    for i in list(ls):
        if divisori2(i) == 2:
            lista.append(i)
            ls.remove(i)
        elif divisori2(i)-2 != k:
            ls.remove(i)
    return lista
