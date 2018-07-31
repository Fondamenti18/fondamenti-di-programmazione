import math

def modi(ls,k):
    lista_primi=[]
    x=0
    while x<len(ls):
        if divisori(ls[x])==0:
            lista_primi.append(ls[x])
            ls.pop(x)
        elif divisori(ls[x])!=k:
            ls.pop(x)
        else:
            x+=1
    return lista_primi

def  divisori(x):
    c=0
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            c+=2
        if x/i==i:
            c+=1
    return c
    
    
            