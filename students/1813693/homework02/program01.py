def lettura(fpost):
    f=open(fpost, "r")
    s=f.read()
    return s.split('<POST>')

def elimina(q):
    w=''
    for x in q:
        if x.isnumeric()==False and x.isalpha()==False:
            w=w+' '
        else:
            w=w+x
    return w.lower()

def listap(fpost):
    l=lettura(fpost)
    l1=[]
    for x in l:
        l1=l1+[elimina(x).split()]
    return l1      

def post(fposts ,insieme):
    b=listap(fposts)
    r=set()
    for x in b:
        for y in insieme:
            if y.lower() in x:
                r.add(x[0])
    return r
