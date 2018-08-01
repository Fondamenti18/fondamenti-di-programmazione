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
import math

def ownDivisors(n):
    s = []
    l = []
    e = math.floor(math.sqrt(n))
    for i in range(1, e+1):
        if (n % i) == 0:
            s.append(i)
            if(i*i != n):
                l.append(int(n/i))
    l.reverse()
    return s+l

def modi(ls,k):
    nwkd = list(ls)
    pn = []
    for iLs in range(0, len(nwkd)):				#accedo a tutti i numeri di ls
        od = len(ownDivisors(nwkd[iLs]))		#lista di tutti i divisori di ls[iLs] (compresi 1 e se stesso)
        if (od - 2) != k:						#verifico se ci sono divisori propri, ad eccezione di 1 e se stesso (ovvero sono 2)
            ls.remove(nwkd[iLs])
        if od == 2:								#verifico che ci siano solo due divisori propri (1 e se stesso)
            pn.append(nwkd[iLs])
    return pn
