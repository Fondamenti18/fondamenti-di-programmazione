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


import math

''' verifica x ogni 'e' di ls:'''
''' se e.divisori == 0 allora e e' primo, else viene rimosso se non ha k divisori'''
def modi(ls,k):
    primeNumbers = []
    tempLs = []
    for num in ls:
        divisors = nDividers(num,k)
        if (divisors == 0):
            primeNumbers.append(num)
        if (divisors != k):
            tempLs.append(num)
    for n in tempLs:
        ls.remove(n)
    return primeNumbers

'''ottiene tutti i divisori di un dato numero'''
def nDividers(num,k):
    i = 2
    divisori = []
    temp = 0
    while(i <= math.sqrt(num)):
        if(num % i == 0):
            divisori.append(i)
            temp = num / i
            if(i != temp):
                divisori.append(temp)
        i+=1
    return len(divisori)
