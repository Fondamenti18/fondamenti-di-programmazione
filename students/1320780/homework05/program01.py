import random

from itertools import *

combinazioni = None

def getResult(comb1, comb2):
    same = 0
    equal = 0
    
    for i in range(len(comb1)):
        if comb1[i] == comb2[i]:
            same += 1
            
    equal = len(set(comb1) & set(comb2)) - same
    
    return same, equal

def cleanCombinazioni(attempt, result):
    toDelete = set()
    global combinazioni
    
    for comb in combinazioni:
        currRes = getResult(attempt, comb)
        if not (result == currRes or result == currRes[::-1]):
            toDelete.add(comb)
            
    combinazioni = combinazioni - toDelete

def decodificatore(configurazione):
    n=configurazione[0]
    
    global combinazioni
    
    if len(configurazione) == 1:
        combinazioni = set(permutations([0,1,2,3,4,5,6,7,8,9], n))
    
    if len(configurazione) >= 2:
        cleanCombinazioni(configurazione[-1][0],configurazione[-1][1])
        
    risposta = random.sample(combinazioni, 1)[0]
    
    return risposta