import random 
from heapq import nlargest
from itertools import permutations,tee,filterfalse

ansList = None
lenght = 0
guess = []
firstGuess = True
pattern = [1,2,3,4,5,6,7,8]
tried = set()
step = 0

def decodificatore(configurazione):

    global codeList,guess,lenght,firstGuess,tried,step,ansList
    
    if len(configurazione) == 1:
    
        lenght = configurazione[0]
        firstGuess = True
        step = 0
        guess = pattern[:lenght]
        tried = set([  tuple(guess)])
        return guess
    else:
        
        step += 1
        
        if step > 15:
            return
        
        answer = configurazione[-1][1]
        
        if firstGuess:
            firstGuess = False
            
            ans = answer[0] + answer[1]
            
            if ans == 0:
                startSet = [i for i in range(10)]
                
                for n in set(guess):
                    startSet.remove(n)
                ansList = permutations(startSet,lenght)
            
            else:
                
                ansList = permutations(range(10),lenght)
                
        
        ansList = filterfalse( lambda x : x in tried or not Score(x,guess,answer),ansList )
        
        
        ansList,tt = tee(ansList,2)
        list(tt)
        
        if step > lenght - 3:
            ansList,tt = tee(ansList,2)
            guess = BreadthSearch(tt)
        else:
        
            for i in ansList:
                if i not in tried:
                    guess = i
                    break
                    
        tried.add(guess)
        return guess


    
def BreadthSearch(codes):

    bestCode,maxAnswers = 0,-1

    codes,testCodes = tee(codes,2)
    backup = list(testCodes)
    
    for code in codes:
        #print(code)
    
        testCodes = iter(backup)
        #codes,testCodes = tee(codes,2)
        answerSet = set()
        
        for testCode in testCodes:
        
            b,w = 0,0
            
            for i in range(lenght):
                if code[i] == testCode[i]:
                    b += 1
                else:
                    if code[i] in testCode:
                        w += 1
                        
            answerSet.add((b,w))
            answerSet.add((w,b))
            
        answers = len(answerSet)

        if answers > maxAnswers or bestCode == 0:
            bestCode = code
            maxAnswers = answers

    return bestCode
        
        
def GetScore(code,testCode):
    
    b,w = 0,0
            
    for i in range(lenght):
        if code[i] == testCode[i]:
            b += 1
        else:
            if code[i] in testCode:
                w += 1
        
    return(b,w)
    
    
def Score(code,testCode,answer):
    
    b,w = 0,0
            
    for i in range(lenght):
        if code[i] == testCode[i]:
            b += 1
        else:
            if code[i] in testCode:
                w += 1
            
    return (b,w) == answer or (w,b) == answer 
    
    
    
def BestInitialConfig(lenght):
    
    perms = permutations(range(10),lenght)
    bestGuess = BreadthSearch(perms)
    
    print(bestGuess)
    
#BestInitialConfig(6)
#BestInitialConfig(7)
#BestInitialConfig(8)
    
   