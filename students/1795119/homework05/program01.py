import random
from copy import deepcopy

def score(codice, proposta):
    if codice == proposta:
        return len(codice), 0
    a = 0
    ins = set(codice)
    for i in range(len(codice)):
        if codice[i] == proposta[i]:
            a += 1
    b = len(ins & set(proposta)) - a
    return a, b

def randCode(n):
    x='0123456789'
    risposta=[]
    for _ in range(n):
        y=random.choice(x)
        risposta+=[int(y)]
        x=x.replace(y,'')
    return risposta

def f1(p, conf):
    p = [int(x) for x in p]
    for c in conf:
        t = c[0]
        r = c[1]
        coppia = r[1],r[0]
        if score(p, t) != r and score(p, t) != coppia:
            return False
    return True

def nextCode(poss, conf):
    temp = set()
    for p in poss:
        if f1(p, conf):
            temp.add(p)
            poss.difference_update(temp)
            return [int(x) for x in p], poss
        else:
            temp.add(p)

def cartesianProduct(seq, n, prec=None):
    res = set()
    if n == 1:
        return [(x) for x in seq]
    for x in seq:
        if prec == None:
            for t in cartesianProduct(seq, n-1):
                if x not in t:
                    res.add(x+t)
        else:
            for t in prec:
                if x not in t:
                    res.add(x+t)
    return res

def decodificatore(configurazione):
    n = configurazione[0]
    global poss, poss6, poss7, poss8
    seq = "0123456789"
    if len(configurazione) == 1:
        if poss == set():
            poss = cartesianProduct(seq, 5)
            poss6 = cartesianProduct(seq, 6, poss)
            poss7 = cartesianProduct(seq, 7, poss6)
            poss8 = cartesianProduct(seq, 8, poss7)
        if n==6:
            poss = deepcopy(poss6)
        elif n==7:
            poss = deepcopy(poss7)
        elif n==8:
            poss = deepcopy(poss8)
        else:
            poss = cartesianProduct(seq, n)
        return randCode(n)
    c, poss = nextCode(poss, configurazione[1:])
    return c


poss = set()
poss6 = set()
poss7 = set()
poss8 = set()
