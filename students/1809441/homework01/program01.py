from math import sqrt
from copy import copy
def modi(ls,k):
    l2=[]
    l5=copy(ls)
    for x  in reversed(ls):
        for i in range(2, int(sqrt(x))+1):
            if x%i==0:
                l2+=[i]
                l2+=[int(x/i)]        
        if len(l2)!=k:
            ls.remove(x)
            l2=[]
        else:
            l2=[]
    return [x for x in l5 if not primo(x)]           
def primo(n):
    i=2;
    while i<n:
        if n==1 or n%i==0:
            return True
        else:
            i+=1  
