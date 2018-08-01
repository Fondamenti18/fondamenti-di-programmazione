from math import sqrt

def modi(ls,k):
    numeriPrimi=[]
    nuovaLista=[]
    for n in ls:
        divisori=set()
        i=2
        while 2<=i<=sqrt(n):
            if n%i==0:
                divisori.add(i)
                divisori.add(n//i)
            i+=1
        if len(divisori)==0:
            numeriPrimi.append(n)
        elif len(divisori)==k: 
            nuovaLista+=[n]
    ls[:]=nuovaLista
    return numeriPrimi