# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 10:54:03 2017

@author: Admin_2
"""
#L=[6,([1,2,3,4,6,9],(3,2))]
#L=[7,([1,2,3,4,6,9,8],(4,2))]
#L=[8,([1,2,3,4,6,7,8,5],(4,4))]

from itertools import permutations, combinations
import random
from random import sample
from time import time

X=[1,2,3,4,5,6,7,8,9,0]
XX=set([1,2,3,4,5,6,7,8,9,0]) 


def decodificatore(L):
    N=L[0]
    if len(L)==1:
        global tested
        tested=set()
        scelta=sample(X,N)
        return scelta
    if not tested:
        prova=L[-1][0]
        tupla=L[-1][1]
        tested=set([el for el in prova])
        not_tested=XX.difference(tested)
        n=tupla[0]
        m=tupla[1]
        good=m+n
        missing=N-good
        avanti=list(combinations(tested,good)) #creo la prima parte della prossima prova mantenendo good elementi fra quelli già provati
        popolo=list(combinations(not_tested, missing))
        sets=[av+pop for av in avanti for pop in popolo]
        global consistents
        consistents=[]
        for el in sets:
            perms=list(permutations(el,N))
            consistents+=[e for e in perms]
        scelta=list(random.choice(consistents))
        return scelta
    else:
        prova=L[-1][0]
        tupla=L[-1][1]
        n=tupla[0]
        m=tupla[1]
        consistents= [x for x in consistents if check(prova,x)==(m,n) or check(prova,x)==(n,m)]
        scelta=list(random.choice(consistents))
        return scelta
        
##### funzioni di confronto fra sequenze ####
        
#def compare(a, b):
#    '''let's use this, 'cause is the faster function that can calculate b/w of two iterables'''
#    count1 = [0] * 10
#    count2 = [0] * 10
#    blacks = 0
#    for dig1, dig2 in zip(a,b):
#        if dig1 == dig2:
#            blacks += 1
#        count1[dig1] += 1
#        count2[dig2] += 1
#    whites= sum(map(min, count1, count2)) - blacks
#    return (blacks, whites)

def check(p1, template):
    """ check() calculates the number of bulls (blacks) and cows (whites)
    of two permutations """ 
    blacks = 0
    whites = 0
    for dig1, dig2 in zip(p1, template):
        if dig1 == dig2:
            blacks += 1
        else:
            if dig1 in template:
                whites += 1
    return (blacks, whites)

#def confronta(lista,y):
#    start=time()
#    for el in lista:
#        check(y, el)
#    end=time()-start
#    print(end)
#    return

######## strategie  ########
#
#def gen_next_try(consistents, strategy):
#    return strategy(consistents)

#def s_samplebest(i, possibles):
#    if i == 0:
#        return s_trynodup(i, possibles)
#    if len(possibles) > 150:
#        possibles = random.sample(possibles, 150)
#        plays = possibles[:20]
#    elif len(possibles) > 20:
#        plays = random.sample(possibles, 20)
#    else:
#        plays = possibles
#    _, play = max([(utility(play, possibles), play) for play in plays])
#    return play
#
#def by_chance(poss):
#    scelta=list(random.choice(poss))
#    return scelta 

# =============================================================================
#  N=4
# 
# L=[4,([1,2,3,4],(3,0))]
# 
# XX=set(1,2,3,4,5,6)    
# =============================================================================
