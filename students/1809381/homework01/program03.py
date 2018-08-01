def codifica(chiave, testo):
    C=""
    Q=""
    X=[]
    for i in chiave:
        if i>='a' and 'z'>=i:
            C+=i

    Y=list(C)
    for k in C:
        
        if Y.count(k)>=2:
            Y.remove(k)
    X=sorted(Y)
    for f in testo:
        if not f in X:
            Q=Q+f
        else:
            Q+=Y[X.index(f)]
    return Q
                                                                               
def decodifica(chiave, testo):
    C=""
    Q=""
    X=[]
    for i in chiave:
        if i>='a' and 'z'>=i:
            C+=i

    Y=list(C)
    for k in C:

        if Y.count(k)>=2:
            Y.remove(k)
    X=sorted(Y)
    for f in testo:
        if not f in X:
            Q=Q+f
        else:
            Q+=X[Y.index(f)]
    return Q
