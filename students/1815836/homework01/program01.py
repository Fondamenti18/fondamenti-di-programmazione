from math import sqrt
def modi(ls,k):
    listaprimi=[]
    lista=list(ls)
    for i in lista:
        kn=0
        ir=int(sqrt(i)+1)
        ira=range(2,ir)
        for div in ira:
            if (i%div==0):
                kn+=2
            if (kn>k):
                break
        if(kn==0):
            listaprimi+=[i]
        if(kn!=k):
            ls.remove(i)
    return(listaprimi)


 
