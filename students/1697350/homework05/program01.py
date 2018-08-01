import random 
from itertools import permutations

#perms = [''.join(p) for p in permutations('0123456789')]
#print(perms)
# ESEMPIO di strategia che tira a caso una combinazione di N valori anche ripetuti
import sys

numbers = list()
i = 0
perms = list()


# mantengo solo le permutazioni che hanno distanza identica a quella dell'ultima risposta
def eliminatePermWithDistance(scelta, perms, tupla):
    perms2 = []
    for elem in perms:
        r = [int(x) for x in elem]
        dist = risposta(scelta,r)
        if dist == (tupla[0], tupla[1]) or dist == (tupla[1], tupla[0]):
            perms2.append(elem)
    return perms2


def risposta(codice, proposta):
    ''' restituisce per ogni proposta quanti indovinati al posto giusto (a) e quanti al posto sbagliato (b)'''
    a=0
    ins=set(codice)
    for i in range(len(codice)):
        if codice[i]==proposta[i]: a+=1
    b=len(ins & set(proposta))-a    # cifre del codice in comune con il tentativo, meno quelle azzeccate esattamente
    return a,b


def decodificatore(configurazione):

    n=configurazione[0]
    global i
    global numbers
    global perms
    if len(configurazione) == 1:
        numbers = list()
        i = 0
        perms = list()
    # verifico quali numeri sono presenti nel codice
    if i <= 10:
        risposta = [i] * n
        if len(configurazione) > 1:
            tupla = configurazione[len(configurazione) - 1][1]
            if tupla[0] > 0 or tupla[1] > 0:
                numbers.append(i - 1)
        i += 1
    # successivamente genero le permutazioni
    else:
        if len(perms) == 0:
            numbers_string = ''.join(str(x) for x in numbers)
            perms = [''.join(p) for p in permutations(numbers_string)]
        scelta = random.choice(perms)
        risposta = [int(x) for x in scelta]
        last_risposta = configurazione[len(configurazione) - 1][0]
        tupla = configurazione[len(configurazione) - 1][1]
        # elimino le permutazioni che hanno distanza diversa dall'ultimo feedback (non sono item candidati)
        perms = eliminatePermWithDistance(last_risposta, perms, tupla)
    return risposta
