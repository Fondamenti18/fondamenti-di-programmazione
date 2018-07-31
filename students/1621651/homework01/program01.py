def fattori(n):  
    import math
    ins=set()
    for i in range(1, int(math.sqrt(n))+1):
        div, mod=divmod(n, i)
        if mod==0:
            ins|={i, div}
    return ins

def modi(ls, k):
    lsp=[]
    for y in ls:
        j=fattori(y)
        if len(j)==2:
            lsp.insert(y, y)
    for x in reversed(ls):
        j=fattori(x)
        print(j)
        if len(j)-2!=k:
            ls.remove(x)
    return lsp

