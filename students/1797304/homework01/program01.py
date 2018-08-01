import math

def modi(ls,k):
        divisori=set()
        primi=[]
        contls=0
        for n in range(len(ls)):
                r=int(math.sqrt(ls[n-contls]))
                for i in range(1,r+1):
                                if ls [n-contls]%i==0:
                                     divisori.add(ls[n-contls]//i)
                                     divisori.add(i)
                if len(divisori)==2 :
                    primi.append(ls[n-contls])
                    ls.pop(n-contls)
                    contls+=1
                elif len(divisori)!=k+2:
                    ls.pop(n-contls)
                    contls+=1
                divisori=set()
        return primi
       
                
                    
                    
    
