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

import random

def modi(ls,k):
    primels = []
    iterablels = ls[:]
    
    for number in iterablels:
        counter = 0
        if is_prime(number):        #controllo numero primo
            primels.append(number)
        else:   #else calcolo divisori
            counter = 1
            div = 0
            divpow = {}
            ntoprime = number
            
            while ntoprime > 1:
                
                if is_prime(ntoprime):
                    div = ntoprime
                else:
                    div = next_prime(div)
                    
                divpow[div] = 0
                
                while not ntoprime % div:
                    ntoprime //= div
                    divpow[div] += 1
                    
                divpow[div] += 1
                counter *= divpow[div]
                
                if counter-2 > k: #trovati piu' divisori di quanto indicati
                    break
                
        if counter-2 != k:  #divisori pari a quanto indicati
            ls.remove(number)
    return primels


def next_prime(n):
    if n < 2:
        return 2
 
    if n & 1:
        n += 2
    else:
        n += 1
        
    while not is_prime(n):
        n += 2
        
    return n

#*********************************************************************************************
#primes between 1 and 1000
primeList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
             103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,
             181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,
             271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,
             373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,
             463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,
             577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,
             673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,
             787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,
             887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]


#prime test
def is_prime(number):
    if number == 2:
        return True
    elif number > 2:
        if number & 1: #test divisibilita per 2
            for prime in primeList: #divisibilita altri primi
                if number == prime:
                    return True
                if not number % prime:
                    return False
                if number > prime//2+1:
                    break
        else:
            return False
    return rabin_miller(number)


#-------------------------------------------------
#rabin miller test
def rabin_miller(n):
    if n < 3:
        return False
    
    d = n - 1
    while not d & 1:
        d = d >> 1
    

    r = random.randrange(2,n)
    p = modular_pow(r,d,n)

    if p == 1 or p == n-1:
        return True
        
    while d != n-1:
        p = modular_pow(p,2,n)
        if p == 1:
            return False
        elif p == n-1:
            return True
        d = d << 1
    
    return False
    
    

def modular_pow(x, y, m):
    res = 1
    x = x % m
    
    while y > 0:
        if y & 1:
            res = (res * x) % m
        y = y >> 1
        x = (x * x) % m
        
    return res
#-------------------------------------------------
#*********************************************************************************************