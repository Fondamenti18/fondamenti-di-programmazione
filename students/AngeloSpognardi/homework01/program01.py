import math
import logging

ch = logging.StreamHandler()
formatter = logging.Formatter('%(name)s | %(message)s')
ch.setFormatter(formatter)
log = logging.getLogger(__name__)
log.addHandler(ch)
log.propagate = False
log.setLevel(logging.WARNING)

def prod(l):
    if len(l)>1:
        return l[0]*prod(l[1:])
    else:
        return l[0]

def decompose(val):
    if val == 1:
        return [1]
    elif val ==2:
        return [2]
    divlist=[]
    q=val
    while q % 2 == 0:
        divlist += [2]
        q = q/2
        log.info('q: {0}'.format(q))
    d=3
    log.info('q: {0}, sqrt(q): {1}'.format(q,math.ceil(math.sqrt(val))+1))
    while q != 1 and d <= math.ceil(math.sqrt(val))+2:
        if q % d == 0:
            divlist += [d]
            q = q/d
            log.info('q: {0}'.format(q))
        else:
            d+=2
    if q !=val and  d > math.ceil(math.sqrt(val))+2:
        divlist += [q]
    log.info('d: {0}'.format(d))
    log.info('decompose({0}): {1}'.format(val, divlist))
    return divlist
            
def to_tuple(l):
    s=set(l)
    return [(i,l.count(i)) for i in s]
        
def modi(n,k):
    m=max(n)
    primes=[]
    divisori=[]
    for i in range(len(n)-1,-1,-1): # scorriamo al contrario per
                                    # evitare cambi di indici
        val=n[i]                # il mio valore
        scomposizione=decompose(val)
        divisori=to_tuple(scomposizione)
        log.info('scomposizione[{0}]: {1}'.format(val,divisori))
        if len(divisori)==0: # val e' primo e va in primes
            if k>0:    # non vogliamo tenere i primi
                primes+=[n.pop(i)]
            log.info('{0}: divisori propri: 0'.format(val))
            log.info('primes: {0}'.format(primes))
        elif len(divisori)==1:     # val ha un solo primo che lo divide
            if k != divisori[0][1]-1: # e lo divide un numero di volte != k
                n.pop(i)                # allora lo elimino dalla lista
                log.info('divisori propri: {0}'.format(divisori[0][1]-1))
        else:                           # val ha piu' primi che lo dividono
            divprop = prod([j[1]+1 for j in divisori])-2
            if k != divprop: # k != numero di div.
                n.pop(i)
                log.info('divisori propri: {0}'.format(divprop))
    primes.reverse()
    return primes

if __name__=='__main__':
#    ls=[121, 4, 37, 441, 7, 16]
    ls=[10000000116, 10000000431, 10000000469, 10000000548, 10000000697, 10000000711, 10000000768, 10000000924]
    print( modi(ls, 16))
    print (ls)
