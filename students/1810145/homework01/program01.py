def modi(ls,k):
    lp = []
    app=[]
    for i in ls:        
        cont = 0
        for j in range ( 2, int ( i ** 0.5 ) + 1 ):           
            if i % j == 0:
                cont += 2
                if j == ( i ** 0.5 ):
                    cont += 1
                    if cont > k:
                        break                               
        if cont == k:
            app += [i]
        elif cont == 0:
            lp += [i] 
    
    ls.clear()
    ls += app
            
                    
    return lp
