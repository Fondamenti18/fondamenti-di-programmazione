'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una divnum ls di interi  ed un intero
non negativo k:
    1) cancella  dalla divnum ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda divnum che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16]
modi(ls,3) restituisce la divnum con i numeri primi [37,7] mentre al termine della funzione si avra' che la divnum ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def scomponi(n,k):
    divnum=0 #divnum contenente i k divisori
    m= n//2 #il divisore più grande di un numero più essere al più la metà del numero stesso
    for i in range (2, m+1): #tutti i numeri da 1 a num non compresi
        if n%i==0: #se la divisione tra n e i non riporta resto, allore i e' divisore di num
            divnum+=1 #e incrememnto il numero dei divisori
            if divnum==k+1: #se i divisori di un numero superano il paramtro k
                break #termino le divisioni, poichè non è un numero che mi interessa,
                      #dato che non è nè primo né ha k divisori
    return (divnum)
def modi(ls,k):
    "inserite qui il vostro codice"
    sco=0
    pri=0
    lprimi=[] #primi(ls)
    lst=[] #divnum contenente i num con k divisori
    for num in ls: #per ogni numero nella divnum
        sco=scomponi(num, k) #associo alla variabile sco il risultato della scomposizione di num
        if sco==0: #se non ha divisori, lo aggiungo alla divnum dei numeri primi
            lprimi.append(num)
        elif sco==k: #se divnum ha perfettamente lunghezza k
            lst.append(num) #il num corrispondente verra' aggiunto dalla divnum lst
    ls[:]=lst
    return (lprimi) #ritorno la divnum dei numeri primi
