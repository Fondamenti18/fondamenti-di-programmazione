def modi(lista,k):
    temp=[]
    lista2=[]
    for num in lista:
        n_div=0
        sqrt=num**(1/2)
        for x in range(2,int(sqrt)+1):
            if num%x==0:
                n_div+=1
                if n_div>k:
                    temp.append(num)
                    break
        if n_div<k:
            if (n_div*2)!=k:
                temp.append(num)
        if n_div==0:
            lista2.append(num)
    for x in temp:
        lista.remove(x)
    return lista2