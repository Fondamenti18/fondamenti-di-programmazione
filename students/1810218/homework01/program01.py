from math import ceil
from math import sqrt
def genera_primi(n):
    
    pos=[True]*n    
    p=[]          
    for i in range(2, ceil(sqrt(n))):
        if pos[i]:
            p.append(i)
            for k in range(i*i,n,i):
                pos[k]=False
    for i in range(i+1,n):
        if pos[i]:
            p.append(i)
    return p

def modi(ls,k):
    primi=[]
    from copy import copy
    ls1=copy(ls)
    p=genera_primi(ceil(sqrt(max(ls))))
    
    
    
    for x in ls1:
        
        cont=0
        for i in p:
            if x%i==0:
                div=i
                while div<=sqrt(x):
                    if (x%div)==0:
                        cont+=1
                    div+=1
                if type(sqrt(x))==float:
                    cont=cont*2
                elif type(sqrt(x))==int:
                    cont=cont*2+1
                break
        
           
        if cont!=k and cont!=0:
            ls.remove(x)
        elif cont==0:
            primi.append(x)
            if k!=0:
                ls.remove(x)
    
    return(primi)
    
    