def codifica(chiave, testo):
    chiave_dis = pulisci(chiave)
    chiave_ord = pulisci(chiave)
    chiave_ord.sort()
    testo_l=list(testo)
    for posizione, carattere in enumerate(testo):
        for ordinata, disordinata in zip(chiave_ord, chiave_dis):
            if carattere == ordinata:
                testo_l[posizione]= disordinata
            else:
                continue
    testo_n= ''.join(testo_l)
    return testo_n


def decodifica(chiave, testo):
    chiave_dis = pulisci(chiave)
    chiave_ord = pulisci(chiave)
    chiave_ord.sort()
    testo_l=list(testo)
    for posizione, carattere in enumerate(testo_l):
        for ordinata, disordinata in zip(chiave_ord, chiave_dis):
            if carattere == disordinata:
                testo_l[posizione]= ordinata
            else:
                continue
    testo_n= ''.join(testo_l)
    return testo_n


def pulisci(chiave):
    chiave.lower()
    ls=[]
    for i in chiave:
        if (i < 'a') == False or (i < 'z') == False:
            if (i in ls) == False:
                ls.append(i)
            else:
                for c in range(len(ls)-1,-1,-1):
                    if ls[c]==i:
                        del ls[c]
                        ls.append(i)
    return ls