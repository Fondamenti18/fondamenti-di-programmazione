def modi(ls,k):
    ls_primi=[]
    conta = 0
    conta1 = 0
    ls1 = []
    ls1 = ls[:]
    for z in ls1:
        conta+=1
        i=z
        num_div=calcolo_divisori(i)
        if num_div==0 and z!=1:
            ls_primi.append(z)
        if  num_div!= k:
            del ls[conta-1 - conta1]
            conta1+= 1
    return(ls_primi)

def calcolo_divisori(i):
    from math import sqrt
    espo=0
    num=2
    divisori = 1
    j = i
    while i>=1:
        if num > sqrt(j) and i != 1:
            divisori = divisori*2
            break
        if i%num==0:
            espo+=1
            i/=num
        else:
            if espo>0:
                divisori= divisori*(espo+1)
            num =num+1
            espo=0
            if i==1:
                break
    divisori=divisori-2
    return divisori
