# coding=utf-8
# Si definiscono divisori propri di un numero tutti i suoi divisori tranne
# l'uno e il numero stesso.
# Scrivere una funzione "modif(ls, k)" che, presa una lista "ls" di interi ed un
# intero non negativo k:
#   1) Cancella dalla lista gli interi che non hanno esattamente k divisori
#      propri;
#   2) Restituisce una seconda lista che contiene i soli numeri primi di ls.
# Nota: un numero maggiore di 1 è primo se ha 0 divisori propri.
#
# Ad esempio per ls = [121, 4, 37, 441, 7, 16], modi(ls, 3) restituisce la lista
# con i numeri primi [37, 7] mentre al termine della funzione si avrà che la
# lista ls = [16].
#
# Per altri esempi vedere il file grade.txt.
#
# Attenzione: non usate lettere accentate e se il grader non termina entro 30
# secondo il punteggio dell'esercizio è zero.
#
# Esercizio svolto da Emanuele Petriglia.

from math import sqrt, ceil

def divisors_of(number):
    '''Ritorna una istanza di 'set' contenente i divisori propri di 'number'.'''
    divisors = set() # Il set evita la presenza di doppioni.

    # Classica implementazione dell'algoritmo "Trial division", leggermente
    # ottimizzato.
    for divisor in range(2, int(sqrt(number)) + 1):
        if not number % divisor:
            divisors.add(divisor)
            divisors.add(number // divisor)

    return divisors

def analyze_number(number, prime_numbers, numbers, value):
    '''Analizza un singolo numero, aggiungendo nella lista 'prime_numbers' se
    primo, rimuovendolo dalla lista numbers se invece non ha 'value' divisori.
    '''
    divisors = len(divisors_of(number))

    if not divisors:
        prime_numbers += [number]

    if divisors != value:
        numbers.remove(number)

def modi(ls,k):
    prime_numbers = []
    ls_range = ls.copy()

    for number in ls_range:
        analyze_number(number, prime_numbers, ls, k)

    return prime_numbers
