def numeroprimo (n):
    i=2
    while n%i!=0:
        i+=1
    return i==n

def modi (ls,k):
    ls1=[]
    for i in ls:
        if numeroprimo(i):
            ls1+=[i]
    ls2=[]
    conta=0
    for x in ls:
        for y in range(2,x//2+2):
            if x%y==0:
                conta+=1
        if conta==k:
            ls2+=[x]
            conta=0
        if conta!=k:
            conta=0
    ls[:]=ls2

    return ls1, ls
