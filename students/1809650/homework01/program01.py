import math
def cont_div(n):
    cd=0
    for a in range(2, int(math.sqrt(n))+1):
        if n%a==0:
            cd+=2
    if math.sqrt(n)==int(math.sqrt(n)):
        cd-=1
    return cd

def modi(ls,k):
    num_pr=[]
    y=0
    for y in ls:
        if cont_div(y)==0:
            num_pr.append(y)
        if cont_div(y)!=k:
            ls.remove(y)
    return num_pr


