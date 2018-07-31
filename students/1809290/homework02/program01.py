def post(fposts,insieme):
    risultato=set()
    for p in insieme: 
        ind=open(fposts)
        a=ind.readline()
        P=p.upper()
        while a!='':
            if '<POST>' in a:
                b=a.lstrip(' ')
                b=b.lstrip('<POST>')
                b=b.lstrip(' ')
                b=b.rstrip('\n')
                b=b.rstrip(' ')
            parole=a.split()            
            for x in parole: 
                X=x.upper()
                if P==X:
                    risultato.add(b)
                if P in X:
                    if len(P)+1==len(X):
                        if X.isalnum() is False:
                            #print(X)
                            risultato.add(b)
            a=ind.readline()
    return risultato
    ind.close()