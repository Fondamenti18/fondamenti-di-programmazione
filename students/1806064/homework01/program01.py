def divisori(n):
    i=2
    primi=[]
    while i*i<=n:
        if n % i == 0:
            n//=i
            primi.append(i)
        else:
            i+=1
    if n>1:
        primi.append(n)
        
    c=0
    d=1
    while c<len(primi):
        esponente=primi.count(primi[c])
        d*=(esponente+1)
        c+=esponente
    return (d-2)

def modi(ls,k):
    primi=[]
    l2=[]
    for i in ls:
        if divisori(i)==0:
            primi.append(i)
        if divisori(i)==k:
            l2.append(i)
    ls[:]=l2[:]
    return(primi)
