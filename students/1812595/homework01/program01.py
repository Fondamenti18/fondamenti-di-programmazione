from math import sqrt
def modi(ls,k):
    num_primi= []
    div= []
    for n in reversed(ls):
        conta= 0
        for i in range(2,int(sqrt(n)+1)):
            if(n%i==0):
                conta+= 2
        if k!=conta:
            lista.remove(n)
        if conta==0:
            num_primi= num_primi+[n]
    num_primi= list(reversed(num_primi))        

    return num_primi
