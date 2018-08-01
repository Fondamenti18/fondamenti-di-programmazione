def decod(pfile, codice):
    with open(pfile, encoding="UTF-8") as file:
        
        post = file.read()
        post = post.split('\n')
        finale=[]
        finale=set(finale)
        n=list(str(codice))
        for u,y in enumerate(post):
            elemento= 1
            if len(y) != len(n):
                elemento=0
            else:
                for VAL,VAL1 in enumerate(n):
                    for VAL2,VAL3 in enumerate(n):
                        if y[VAL]==y[VAL2]:
                            if n[VAL]==n[VAL2]:
                                break
                            else:
                                elemento = 0
                        if n[VAL]==n[VAL2]:
                            if y[VAL]==y[VAL2]:
                                break
                            else:
                                elemento=0
                if elemento==1:
                    finale.add(y)
                    
        return finale