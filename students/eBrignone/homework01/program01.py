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
def divisori(number,k):
    i = 2
    potenza = 0
    radice = int(math.sqrt(number))
    divisori = []
    while i<=radice:
        if(number%i==0):
            number /=i
            potenza = potenza + 1
        else:
            if potenza>=1:
                divisori += [(i, potenza)]
            kParziale = numeroDivisori(divisori)
            # tolgo due elementi perche non devo contare 1 e se stesso
            if kParziale-2>k :
                return divisori
            i = i + 1
            potenza = 0
    if number>1:
        divisori += [(number,1)]
    return divisori

def numeroDivisori(divisori):
    #il caso in cui la lista dei divisori e vuota ritorno 2 perche primo
    if len(divisori)==0: return 2

    #applico la formula (a+1)*(b+1)..... dove a,b sono
    #le potenze dei fattori primi che dividono il numero
    nDivisori = 1
    for fattore in divisori:
        nDivisori *= (fattore[1]+1)
    return nDivisori

def modi(ls, k):
    daRimuovere = []
    ret = []
    for x in ls:
        divisoriDiX = divisori(x,k)
        #controllo se number e un numero primo
        if len(divisoriDiX)==1 and divisoriDiX[0][0]==x:
            ret += [x]
        if numeroDivisori(divisoriDiX)-2!=k:
            daRimuovere.append(x)
    for dr in daRimuovere:
        ls.remove(dr)
    return ret

