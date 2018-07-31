# -*- coding: utf-8 -*-
def modi(ls,k):
    lis = []
    rimoz = []
    for num in ls:
        c=0
        tabella = [ True ] * (num)
        for v in range(2, ((num//2)+1)):
            if tabella[v]:
                if num%v==0:
                    c+=1
                    if c>k:
                        break
                else:
                    for C in range(v * v, num, v):
                        tabella[C] = False
        if c!=k:
            rimoz.append(num)
        if c==0:
            lis.append(num)    
    for i in rimoz:
        ls.remove(i)        
    return lis



























