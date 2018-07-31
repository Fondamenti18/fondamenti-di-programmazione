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

ls=[]    
def n_p(a):
    b = 2
    while b < a and (a % b) != 0:
        b += 1
    return b == a
    ls.remove(i)
def modi(ls,k):
    ls_primi = []
    for i in reversed(ls):
        if n_p(i):
            ls_primi.append(i)
            ls.remove(i)
        else:
            contadivisori = 0
            for j in range(2,i):
                if i%j==0:
                    contadivisori+=1
                if contadivisori > k:
                  break
            if contadivisori != k:
                ls.remove(i)
    ls_primi.reverse()
    return ls_primi
