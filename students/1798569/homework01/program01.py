from math import sqrt
def modi(ls,k):
    lsprimi=[]
    for x in range(0,len(ls)):
        cnt=2
        contadiv=0
        while cnt <int(sqrt(ls[x]))+1 and contadiv<k+1:
            if ls[x]%cnt==0:
                contadiv+=1
                if ls[x]/cnt!=cnt:
                    contadiv+=1
            cnt+=1
            
        if contadiv==0:
            lsprimi+=[ls[x]]
        if contadiv!=k:
            ls[x]=''
        
    while'' in ls:
        ls.remove('')
    return lsprimi
