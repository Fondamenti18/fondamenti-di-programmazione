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
    "inserite qui il vostro codice"
    lpri, ldiv, lcan = [], [], []
    nlen = len(ls)
    for i in range(nlen):
        nele, lran = 0, [3, 2]
        nlim1 = ls[i] // 2
        if ls[i] == 4:
            nlim1 += 1
        nlim2 = 0
        if ls[i] % 2 == 0:
            lran = [2, 1]
        while lran[0] < nlim1 and nele <= k:
            if  ls[i] % lran[0] == 0:
                nele += 1
                ndiv = ls[i] // lran[0]
                if nlim2 != ndiv:
                    nlim1 = nlim2 = ndiv
                if nlim1 >= ndiv and ndiv != lran[0]:
                    nele += 1
            else:
                nlim1 = ls[i] // lran[0]
            lran[0] += lran[1]
        if nele == k:
            ldiv.append(ls[i])
        elif nele == 0:
            lpri.append(ls[i])
            lcan.append(ls[i])
        else:
            lcan.append(ls[i])
    for i in lcan:
        ls.remove(i)
    return lpri
