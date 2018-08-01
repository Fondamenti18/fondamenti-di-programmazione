# v02 - improved reduction by reducing from previous exclusion results (e.g. 011222, 233444 etc.)

# v03 - Implemented multithreading - 2.4x performance boost

# v04 - Removed support for multithreading (st. sampling is now used to compute big sets)
#       using stochastic sampling from full permutation set  (https://lirias.kuleuven.be/bitstream/123456789/184247/2)
#       sample size of 10000 dispositions, if one fails another is immediately computed
#       Stochastic sampling **IS NOT USED** if the number of digits to crack is equal to 6

# v05 - Allowing 7 digits configurations to be computed at most 1-2 times without stochastic sampling

# v06 - Implemented guess eligibility by similiarity reduction (Lotte Berghman et Al. - Efficient solutions for Mastermind using genetic algorithms) 
#       From the paper:                                         
#               " As a second alternative, we adopt this global viewpoint as follows: the quality
#                 of an eligible code c in E is evaluated by means of an estimate of the number 
#                 of remaining eligible codes if c is the next guess "                                                   

import random
import itertools
import threading

numthreads = 8
perm = []
permWasReduced = False
sampleperm = []
samplefailed = False
samplepermcreated = False
computingSample  = True
firstTripletTest = True
gN = 0
gN7computedWithoutSampling = 0

def computeResult(guess, secret):
    global gN 

    perfectmatch   = set()
    somewherematch = set()

    for i in range(gN):
        if guess[i] == secret[i]:
            perfectmatch.add(guess[i])
    
    lpm = len(perfectmatch)

    for i in range(gN):
        if (guess[i] in secret) and (guess[i] not in perfectmatch):
            somewherematch.add(guess[i])

    lsm = len(somewherematch)

    return (lpm, lsm)
        
def resultMatches(t1, t2, res):
    global gN 

    perfectmatch   = set()
    somewherematch = set()

    for i in range(gN):
        if t1[i] == t2[i]:
            perfectmatch.add(t1[i])
    

    lpm = len(perfectmatch)
    # if (res[0] != lpm) and (res[1] != lpm):
    #     return False


    for i in range(gN):
        if (t1[i] in t2) and (t1[i] not in perfectmatch):
            somewherematch.add(t1[i])

    lsm = len(somewherematch)


    if (lpm == res[0]) and (lsm == res[1]):
        return True

    return False

def sampleResultEligible(t1, t2, res):
    global gN 
    global sampleperm 

    perfectmatch   = set()
    somewherematch = set()

    for i in range(gN):
        if t1[i] == t2[i]:
            perfectmatch.add(t1[i])
    
    lpm = len(perfectmatch)

    for i in range(gN):
        if (t1[i] in t2) and (t1[i] not in perfectmatch):
            somewherematch.add(t1[i])

    lsm = len(somewherematch)



    # if len(sampleperm) > 0:
    if ((lpm == res[0]) and (lsm == res[1])): #      or       ((lpm + lsm) > (res[0] + res[1])):
        return True
    # else:
    #     if (lpm + lsm) >= (res[0] + res[1]):
    #         return True

    return False

def checkPrevTriplet(configurazione):
    global perm

    previousTriplet = configurazione[-1][0]
    previousResult  = configurazione[-1][1]
    previousResultReversed  = previousResult[::-1]

    perfectMatch = False
    if previousResult[0] == previousResult[1]:
        perfectMatch = True

    if not perfectMatch:
        perm = [x for x in perm if (resultMatches(previousTriplet, x, previousResult)) or (resultMatches(previousTriplet, x, previousResultReversed))]
    else:
        perm = [x for x in perm if (resultMatches(previousTriplet, x, previousResult))]


def checkPrevSampleTriplet(configurazione):
    global sampleperm
    global firstTripletTest

    if firstTripletTest:
        firstTripletTest = False
        return

    previousTriplet = configurazione[-1][0]
    previousResult  = configurazione[-1][1]
    previousResultReversed  = previousResult[::-1]

    perfectMatch = False
    if previousResult[0] == previousResult[1]:
        perfectMatch = True


    # sampleperm = [x for x in sampleperm if (sampleResultEligible(previousTriplet, x, previousResult)) ]

    if not perfectMatch:
        sampleperm = [x for x in sampleperm if (sampleResultEligible(previousTriplet, x, previousResult)) or (sampleResultEligible(previousTriplet, x, previousResultReversed))]
    else:
        sampleperm = [x for x in sampleperm if (sampleResultEligible(previousTriplet, x, previousResult))]




def reducePermFromSampleResults(configurazione):
    global perm

    for i in range(1, len(configurazione)):
        previousTriplet = configurazione[i][0]
        previousResult  = configurazione[i][1]
        previousResultReversed  = previousResult[::-1]

        perfectMatch = False
        if previousResult[0] == previousResult[1]:
            perfectMatch = True

        if not perfectMatch:
            perm = [x for x in perm if (resultMatches(previousTriplet, x, previousResult)) or (resultMatches(previousTriplet, x, previousResultReversed))]
        else:
            perm = [x for x in perm if (resultMatches(previousTriplet, x, previousResult))]



def checkNewSampleFailure(configurazione):
    global sampleperm

    fakeconfig = [0]

    for i in range(1, len(configurazione)):
        fakeconfig += [configurazione[i]]
        # loading last result, or 0 if this is the first iteration of the program
        lastConfigResult = 0
        if len(fakeconfig) > 1:
            lastConfigResult = fakeconfig[-1][1][0] + fakeconfig[-1][1][1]

        if len(sampleperm) > 1 and (lastConfigResult < gN):
            checkPrevSampleTriplet(fakeconfig)
            
            if len(sampleperm) == 0 and lastConfigResult < gN:
                # this sample failed, report to caller
                return (True, fakeconfig)


    # this sample still had some members in it, report to caller
    return (False, fakeconfig)

def computeNextSampleFromMinimizationHeuristic(configurazione):
    global perm


    samplesize = 50
    if len(perm) < 50:
        samplesize = len(perm)

    if len(perm) < 8:
        # try randomly
        randindex = random.randint(0, len(perm) - 1)
        return perm[randindex]


    minimalSample = 9999
    minimalGuess  = None

    for i in range(samplesize):
        r  = random.sample(perm, 2)
        c  = r[0]
        cs = r[1]

        # if c was the next guess, and cs the secret code, compute the result
        result = computeResult(c, cs)
        resultreversed = (result[1], result[0])

        permsample = random.sample(perm, samplesize)
        # minimize sample from obtained result
        permsample = [x for x in permsample if (resultMatches(c, x, result)) or (resultMatches(c, x, resultreversed))]

        if len(permsample) < minimalSample:
            minimalSample = len(permsample)
            minimalGuess  = c

    return minimalGuess 
        


def decodificatore(configurazione):
    global firstTripletTest
    global perm
    global sampleperm
    global samplefailed
    global computingSample
    global permWasReduced
    global samplepermcreated
    global gN7computedWithoutSampling
    global gN


    n=configurazione[0]  
    x='0123456789'
    risposta=[]


    # reset state if beginning
    if len(configurazione) == 1:
        perm  = list()
        sampleperm = set()
        samplefailed = False
        samplepermcreated = False
        computingSample  = True
        permWasReduced = False
        firstTripletTest = True
        gN = n





    # let's create the permutation set if it doesn't exist
    if len(perm) == 0:
        perm = list(itertools.permutations([x for x in range(0, 10)],   gN))

    # let's create the sampled permutation set if it doesn't exist
    if len(sampleperm) == 0 and (not samplepermcreated):
        samplepermcreated = True
        sampleperm = random.sample(perm, 20000)







    # if still finding best of sample perm
    if computingSample:

        # we're not doing this for 6 figures configurations, randomly try one sample
        # for 7 digits configurations, allow at most 2 to be computed without sampling 
        if gN == 6 or (gN == 7 and gN7computedWithoutSampling < 1):
            if gN == 7:
                # print("gN7 computed without sampling")
                debug = 0

            computingSample = False
            return random.choice(sampleperm)



        # loading last result, or 0 if this is the first iteration of the program
        lastConfigResult = 0
        if len(configurazione) > 1:
            lastConfigResult = configurazione[-1][1][0] + configurazione[-1][1][1]

        if (lastConfigResult < gN):
            checkPrevSampleTriplet(configurazione)

            # check if this sample failed...        
            if len(sampleperm) == 0:
                # this sample failed, try with a new one
                # print("first sample failed")

                while True:
                    sampleperm = random.sample(perm, 20000)
    
                    newOneFails = checkNewSampleFailure(configurazione)
                    # this sample did not fail, go on and test one of it's result
                    if newOneFails[0] == False:
                        # print("new sample succeded, sample length: " + str(len(sampleperm)))
                        
                        randindex = random.randint(0, len(sampleperm) - 1)
                        return sampleperm[randindex]
                    else:
                        # try another random sample
                        # print("new sample failed")
                        continue
                        
                        


            debug = len(sampleperm)
            randindex = random.randint(0, len(sampleperm) - 1)
            return sampleperm[randindex]


        # we're done with the stochastic sample
        computingSample = False






    # at this point, found best sample OR last config has all the excluded pairs
    


    
    
    # all these digits are inside the secret key
    if not permWasReduced:
        appearingdigits = [ x for x in range(0, 10) if x in configurazione[-1][0] ]
        
        # not computing sampling for 6 digits configurations
        # allowing at most 2 plays with 7 digits without using sampling
        if gN == 6 or (gN == 7 and gN7computedWithoutSampling < 1):
            if gN == 7:
                gN7computedWithoutSampling += 1          

            appearingdigits = [ x for x in range(0, 10) ]




        perm = list(itertools.permutations([x for x in appearingdigits],   gN))

        # use previous results to reduce perm
        reducePermFromSampleResults(configurazione)

        permWasReduced = True





    # if we're small enough, just try randomly
    if len(perm) < 3:
        tryit = perm.pop()
        return tryit




    # check previous triplet and minimize perm
    checkPrevTriplet(configurazione)
    # randindex = random.randint(0, len(perm) - 1)
    # return perm[randindex]
    return computeNextSampleFromMinimizationHeuristic(configurazione)
