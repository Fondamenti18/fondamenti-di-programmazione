
def modi(ls, k):
    div=[]
    primi=[]
    for i in ls:
        ndiv=0
        for x in range(2,i):
            if i%x==0:
                ndiv+=1
                if ndiv== k+1:
                    break
        if ndiv ==0:
            primi.append(i)
        if ndiv ==k:
            div.append(i)
    list.clear(ls)
    for i in div:
        ls.append(i)
    return(primi)
    return(ls)