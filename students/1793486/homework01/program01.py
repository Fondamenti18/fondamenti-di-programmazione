def modi(ls,k):
    lprimi=[]
    for el in range(len(ls)-1,-1,-1):
        c=0
        for x in range(2, int(ls[el]**0.5)+1):
            if ls[el]%x==0:
                c+=1
                if ls[el]%(ls[el]/x)==0:
                    if ls[el]/x!=x:
                        c+=1
        if c==0:
            lprimi+=[ls[el]]
        if c!=k:
            ls.remove(ls[el])
    return lprimi[::-1]
