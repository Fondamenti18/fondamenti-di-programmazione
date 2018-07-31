def codifica(chiave, testo):
    chiave=[x for x in chiave if 'a'<=x<='z']
    codifica=''
    a=''
    ldis=[]
    lord=[]
    i=0
    for a in chiave:
        if a not in chiave[i+1:]:
            ldis+=[a]
        i+=1
        
    lord=sorted(ldis)

    i=0
    cifra=[]
    while i<len(ldis):
        cifra+=[[lord[i],ldis[i]]]
        i+=1

    
    for k in testo:
        r=False
        for index in range(len(cifra)):
            if k==cifra[index][0]:
                codifica+=cifra[index][1]
                r=True
                break
        if r==False:
            codifica+=k
       
    return codifica

def decodifica(chiave, testo):
    chiave=[x for x in chiave if 'a'<=x<='z']
    decodifica=''
    a=''
    lord=[]
    ldis=[]
    i=0
    for a in chiave:
        if a not in chiave[i+1:]:
            ldis+=[a]
        i+=1
    
    lord=sorted(ldis)
    i=0
    cifra=[]
    while i<len(ldis):
        cifra+=[[ldis[i],lord[i]]]
        i+=1
    
    for k in testo:
        r=False
        for index in range(len(cifra)):
            if k==cifra[index][0]:
                decodifica+=cifra[index][1]
                r=True
                break
        if r==False:
            decodifica+=k
        
    return decodifica
