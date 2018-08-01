def modi(ls,k):
    nls=[]
    ld=[]
    for i in ls:
        u=2
        count=0
        primo=True
        while u*u<i+1:
            if i%u==0:
                count+=1
            if (i%u==0):
                primo=False
            u+=1
        if (int(count*2))==k:
            nls.append(i)
        if primo:
            ld.append(i)
    ls[:]=nls[:]    
    return ld