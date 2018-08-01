import math


def n_divisori(numero,y):
    num_div=0
    if numero%2==0:
        divisore=2
        skip=1
    else:
        divisore=3
        skip=2
    max=(int(math.sqrt(numero)))
    while (divisore <= max and num_div <= y):
        if numero % divisore == 0:
            num_div += 1
            if numero / divisore != divisore:
                num_div += 1
        divisore += skip
    return num_div


def modi(ls, k):
    indice = 0
    ls_primi = []
    newls = ls.copy()
    # x <-- numero su cui effettuare la verifica
    for x in newls:
        ndivisori = n_divisori(x,k) 
        if ndivisori == 0:
            ls_primi.append(x)
            del ls[indice]
        # se diverso da k le elimino dalla lista
        elif ndivisori != k:
            del ls[indice]
        else:
            indice += 1
    return ls_primi