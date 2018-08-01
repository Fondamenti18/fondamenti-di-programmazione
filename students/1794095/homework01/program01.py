from math import *
def modi(ls,k):
    ls2=ls
    Nprimi=[]
    Kdiv=[]
    for n in ls2:
        y=2
        diviList=[]
        while y<=(sqrt(n)+1):
            if n%y==0:
                diviList.append(y)
                diviList.append(n/y)
            y+=1
        if len(diviList)==0:
            Nprimi.append(n)
            ls.remove(n)
    for n in ls2:
        y=2
        diviList=[]
        while y<=(sqrt(n)+1):
            if n%y==0:
                diviList.append(y)
                diviList.append(n/y)
            y+=1
        if len(diviList)!=k:
            Kdiv.append(n)
    for e in Kdiv:
        ls.remove(e)
    return Nprimi
            
