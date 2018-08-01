from math import sqrt
def divisori(n):  
    divisori = 0
    divisore = 2 
    while divisore<=sqrt(n):
        if (n%divisore) == 0: 
            divisori+=2
        divisore+=1  
    return divisori
def modi(ls,k):          
    numeriprimi = []
    listScan = 0
    lenLista = len(ls)  
    while listScan < lenLista: 
        if divisori(ls[listScan])==0: 
            numeriprimi.append(ls[listScan])
        if divisori(ls[listScan])!=k: 
            ls.remove(ls[listScan])
            lenLista-=1
        else:
            listScan+=1 
    return numeriprimi