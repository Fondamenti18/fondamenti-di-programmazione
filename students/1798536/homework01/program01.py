def NumeroDivisori(x):
    n = 1
    numero_divisori = []
    numero_non_divisori = []
    while n <= x:
        if x % n != 0:
            numero_non_divisori += [n]
        else numero_divisori += [n]
        n+1
    return numero_divisori


def modi(ls, k):
    numeri_primi = []
    numeri_con_k_divisori = []
    for n in ls:
        if len(NumeroDivisori(n)) == 2:
            numeri_primi += [n]
        elif len(NumeroDivisori(n)) == k+2:
            numeri_con_k_divisori += [n]
    ls[:] = numeri_con_k_divisori
    return numeri_primi
