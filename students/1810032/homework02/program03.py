def decod(pfile, codice):
    ls=[]
    ls2=[]
    ls3=[]
    ls5=[]
    ls4=list(codice)
    for x in ls4:
        ls5.append(int(x))    
    f = open(pfile)
    ins=set()
    for riga in f:
        if len(riga) - 1 == len(codice):
            ls.append(riga)
    for x in ls:
        ls3=[]
        ls6=[]
        ls2 = list(x[:-1])
        for c in range(len(ls2)):  
            ls3.append(ls2.index(ls2[c]))
            ls6.append(ls5.index(ls5[c]))      
        if ls3==ls6:
            ins.add(x[:-1])
    f.close()    
    return ins