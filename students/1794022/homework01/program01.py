 from math import sqrt
 def modi(ls,k):
    primi=[]
    divisori=0
    radice=0
    a=0
    for cfr in range(len(ls)-1,-1,-1):
        divisori=0
        radice=int(sqrt(int(ls[cfr])))+1
        for i in range(2,radice):
            a=int(ls[cfr])%int(i)
            if a==0:
                divisori+=1
            else:
                pass
        divisori=(divisori*2)
        print(divisori)
        if divisori==0:
            primi.append(ls[cfr])
        if divisori!=k:
            del ls[cfr]
    primi.reverse()
    return(primi)
