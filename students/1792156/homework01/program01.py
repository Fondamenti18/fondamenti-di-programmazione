import functools

def modi(lst,k):
    res=[]
    res2=[]
    for i in lst:
        lista=[]
        lista=functools.reduce(list.__add__,([x, i//x] for x in range(1, int(i**0.5) + 1) if i % x == 0))
        lista.remove(1)
        lista.remove(i)
        if len(lista)==k:
            res.append(i)
        if len(lista)==0:    
            res2.append(i)
    list.clear(lst)
    for i in res: 
        lst.append(i)
    return(res2)   