def decod(pfile, codice):
    cifre=[]
    testfin=[]
    testfinmod=[]
    for cf in codice:
        if cf not in cifre:
           cifre+=cf
    with open(pfile,'r') as t:
        lettlin=t.readlines()
        for par in lettlin:
            if len(par)==len(codice)+1:
                prova=''
                parlett=[]
                for l in par:
                    if l not in parlett:
                        parlett+=l
                parlett.pop()
                count=0
                diz1={}
                for l2 in parlett:
                    if len(parlett)<=len(cifre):
                        if l2 not in diz1:
                            diz1[l2]=cifre[count]
                            count+=1
                for l in par:
                    if l in diz1:
                        l=l.replace(l,diz1[l])
                        prova=prova+l
                if prova==codice:
                    testfin=testfin+[par]
                    for v in testfin:
                        v=v.rstrip("\n")
                    testfinmod=testfinmod+[v]
                testfinmod2=set(testfinmod)
        return testfinmod2
        
                    
    
    





