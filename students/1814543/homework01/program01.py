def modi(ls,k): 
    primi=[]
    result = []   
    for item in ls:
        resto = item
        exp=[]
        lastdiv=2
        myExp = 0
        top = int( item / 2 )
        while(resto != 1 and lastdiv <= top):
            if(resto % lastdiv ==0):
                myExp = myExp +1
                resto = resto / lastdiv
            else:
                lastdiv = lastdiv +1               
                if(myExp != 0):
                    exp.append(myExp)
                    myExp = 0
            if(resto == 1):
                exp.append(myExp)
        if(len(exp) == 0):
            primi.append(item)
        else:
            sumDivisori = 1
            for esponente in exp:
                sumDivisori = sumDivisori *(esponente + 1)
            sumDivisori = sumDivisori - 2
            if(sumDivisori == k):      
                result.append(item)
    del ls[:]
    for item in result:
        ls.append(item)
    return primi
