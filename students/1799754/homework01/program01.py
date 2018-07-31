def NumFatt(n):
    index=2
    lista_primi=[]
    while index*index<=n:
        if n % index != 0:
            index+=1
        else:
            n//=index
            lista_primi.append(index)
    if n>1:
        lista_primi.append(n)
    return lista_primi

def CalcDiv(lista):
    divisoripropri=1
    esponente=0
    var=0
    for x,y in enumerate(lista):
        if y!=var:
            esponente=lista.count(y)
            divisoripropri*=(esponente+1)
            var=y
    return divisoripropri-2
        

def NumDivPro(n):
    return CalcDiv(NumFatt(n))
    
    
def modi(ls,k):
    l=[]
    nuovo=[]
    for e in ls:
        if(NumDivPro(e)==0):
            nuovo.append(e)
        if (NumDivPro(e)!=k):
            l.append(e) 
    for c in l:
        ls.remove(c)   
    return nuovo
