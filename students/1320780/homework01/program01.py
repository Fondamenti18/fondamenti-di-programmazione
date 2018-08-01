def getNumDivisori(num):
    numDivisori = 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            numDivisori += 2
    return numDivisori

def modi(ls, k):

    tmpLs = ls.copy()
    lsPrimi = []
    
    for num in tmpLs:
        numDivisori = getNumDivisori(num)
        if numDivisori == 0:
            lsPrimi.append(num)
        if numDivisori != k:
            ls.remove(num)
    return lsPrimi