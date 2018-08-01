import math 
def modi(ls,k):
    i=0
    n_primi=[]
    while i<len(ls):
        c=2
        divisori=[]
        numero=int(math.sqrt(ls[i])+1)
        while c <= numero:
            if ls[i] % c == 0:
                divisori += [c]
                divisori += [c]
                if (len(divisori)>k):
                    break
            c += 1
        if len(divisori)==0:
            n_primi += [ls[i]]
            del(ls[i])
            i=i-1
        elif len(divisori)!=k:
            del(ls[i])
            i=i-1
        i += 1
    return n_primi
   
