def post(fposts, insieme):
    f = open(fposts)
    q = f.read()
    n = q.split('<POST>')
    result=set()
    for post in n:
        for i in insieme:
            p = post.lower()+' '
            j = i.lower()
            while j in p:
                a = p.find(j)
                if p[a-1].isalpha()==False and p[a+len(j)].isalpha()==False:
                    k=assignid(post)
                    result.add(k)
                if p.count(j)>1:
                    p=purify(p,j)
                elif p.count(j)==1:
                    break
    return result


def assignid(x):
    n=0
    while x[0].isdigit()==False and len(x)>0:
        x=x[1:]
    while x[n].isdigit()==True:
        n+=1
    idpost=x[0:n]
    return idpost

def purify(c, d):
    c=c[:c.find(d)]+c[c.find(d)+len(d):]
    return c
