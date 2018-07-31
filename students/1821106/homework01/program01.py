import math

def action4(n):
    test = []
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            test.append(i)
            test.append(int(n/i))
    return len(set(test))

def action3(ls):
    prime = []
    for j in range(0,len(ls)):
        if action4(ls[j])==0:
            prime.append(ls[j])
    return prime

def action(ls,k):
    remove = []
    for j in range(0,len(ls)):
        if action4(ls[j])!=k:
            remove.append(ls[j])
    return remove

def action2(ls, k):
    list = action(ls,k)
    for x in range(0,len(list)):
        ls.remove(list[x])

def deleteAndAdd(ls, k):
    list = action3(ls)
    for x in range(0,len(list)):
        ls.remove(list[x])
    return list

def modi(ls,k):
    listaprimi = deleteAndAdd(ls,0)
    action2(ls,k)
    return listaprimi