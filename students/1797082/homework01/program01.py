def factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result
    
#print(factors(4))
def modi(ls,k):
    ls2=[]
    ls1=ls[:]
    for  el in ls1:
        costante=len(factors(el))-2
        if costante == 0:
            ls2.append(el)
            
        if costante != k:
            ls.remove(el)
    
    print (ls)
    return(ls2)
    
#a = [340887623,26237927,2491,777923,5311430407,6437635961,82284023]
#print(modi(a,4))
