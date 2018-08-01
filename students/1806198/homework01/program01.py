from math import sqrt

#funzione principale del programma
def modi(ls,k):
    ls2=[]
    for num in reversed(ls):
        cntdiv=elabora(num,k)
        if cntdiv==0:
            ls2+=[num]
        if cntdiv!=k:
            ls.remove(num)
    ls2.reverse()
    return ls2

#calcola i divisori del numero dato fino a radice quad. o divisori>k
def elabora(num,k):
    cntdiv=0
    limite=int(sqrt(num))
    
    for div in range(2,limite):
        if (num%div)==0:
            cntdiv+=2
            if cntdiv>k:
                return cntdiv
            
    if (num%limite)==0:
        cntdiv+=1
    return cntdiv

    


