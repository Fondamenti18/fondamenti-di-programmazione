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
    sbagliati = [] 
    primi = []
    for num in ls:
        fattori, fattori_nr = fattori_primi(num)
        divisori = 1
        for el in fattori_nr:
            divisori *= (fattori.count(el) + 1)
        if divisori == 2 or divisori == 1:
            primi += [num]
        if divisori - 2 != k:
            sbagliati += [num]
    for el in sbagliati:
        ls.remove(el)
    return primi

def fattori_primi(num):
    '''Restituisce una lista e un insieme: la lista (fattori) contiene
    i fattori primi del numero dato ripetuti un numero di volte 
    uguale all'esponente; l'insieme (fattori_nr) contiene i fattori primi non ripetuti'''
    fattori = []
    fattori_nr = set()
    ultimo = 1
    n = num
    f = 2
    stop = n
    while n > 1 and f <= stop:
        if n % f == 0:
            fattori_nr.add(f)
            fattori += [f]
            ultimo *= f
            n = n // f
        elif f == 2:
            f += 1
        else:
            stop = num // f
            f += 2
    ultimo = num // ultimo
    if ultimo != 1 and ultimo != num:
        fattori += [ultimo]
        fattori_nr.add(ultimo)
    return fattori, fattori_nr