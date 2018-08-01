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
    "inserite qui il vostro codice"
    ls2 = []
    lista_primi =[]
    for intero in ls:
    # con questo ciclo for calcolo i divisori dei numeri presi in input
        divisori = 0
        for x in range(2,int(intero**0.5)+1):
        # calcolo i divisori da 2 alla parte intera della radice dell'intero + 1
            if intero%x == 0:
                divisori += 2
                # considerando il range fino alla parte intera della radice quadrata dell'intero + 1 considero solo metà dei divisori,
                # percui incremento i divisori non di 1, ma di 2
            elif divisori >= (k+1):
            # esce direttamente se ha più di k divisori
                break
        if divisori == k:
        # se l'intero ha esattamente k divisori (esclusi l'unità e se stesso), li aggiungo alla lista di appoggio
            ls2.append(intero)
        elif divisori == 0:
        # se l'intero ha esattamente 0 divisori allora è primo (in quanto i numeri primi sono divisibili solo per 1 e per se stessi)
            lista_primi.append(intero)
    ls[:] = ls2
    return lista_primi
