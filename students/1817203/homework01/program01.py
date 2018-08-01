from math import sqrt
def modi(ls,k):
    primi=[]
    c=0
    while c<len(ls):
        x=ls[c]
        fattori=fattorizzazione(x,k)
        div=calcolodiv(fattori) 
        if div-2==0:
            primi+=[ls[c]]      
        if div-2!=k:
            del ls[ls.index(ls[c])] 
        else:    
            c+=1    
    return primi

def fattorizzazione(x,k):
    d=2
    divp=1
    n=1
    fattori={}
    ex=round(sqrt(x))+1
    while d<=ex and divp-2<=k:
        if x%d==0:
            x=x/d
            if d in fattori:
                fattori[d]+=1
            else:
                fattori[d]=1
        else:
            d=2*n+1
            n+=1
            if d%5==0 and d!=5:
                d=2*n+1
                n+=1       
        divp=calcolodiv(fattori)  
    if not x in fattori and x!=1:
            fattori[x]=1
    return fattori

def calcolodiv(fattori):
    div=1
    for el in fattori:
            div=div*(fattori[el]+1)
    return div