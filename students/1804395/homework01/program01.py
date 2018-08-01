from math import sqrt
def modi(ls,k):
    risultato = []
    for indice in range (len(ls)-1,-1,-1):
        contatore=0
        for divisore in range(2,int((sqrt(ls[indice])+1))): 
            if ls[indice]%divisore == 0:
                contatore += 2
            if contatore > k:
                break
        if contatore == 0:
            risultato = [ls[indice]] + risultato
        if contatore != k:
            ls.remove(ls[indice])
    return risultato
