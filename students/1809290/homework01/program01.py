from math import sqrt
#import copy

def modi(ls,k):
    ris=[]
    cls=[]
    for y in ls:
        i=2
        d=0
        while i<(int(sqrt(y))+1):
            if y%i==0:
                d+=2
            i+=1
        if int(sqrt(y))**2==y:
            d=d-1
        if d==0:
            ris.append(y)
        elif d==k:
            cls.append(y)
    ls[:]=cls
    print(ls)
    return ris