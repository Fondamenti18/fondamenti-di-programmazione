from math import sqrt

def div_propri(n):
    l=[]
    for d in range(2,int(sqrt(n))+1): #considera i numeri da 2(saltando 1 perche voglio solo i divisori propri) fino a rad(n) compresa
        if n%d==0:
            l.append(d)
            if d**2!=n:
                l.append(int(n/d))
    return l #con return chiudo la funzione

def n_primi(ls):
    for n in ls[:]:
        l=div_propri(n) #eseguo la funzione divisori_propri precedentemente definita
        if l!=[]:
            ls.remove(n)
    return ls

def modi(ls,k):
    num_primi=n_primi(ls[:]) #nuova lista sulla quale agire corrispondente a quella ottenuta nella f.ne citata
    for n in ls[:]: #copia di lista per non modificare la lista di partenza
        l=div_propri(n) 
        if len(l)!=k:
            ls.remove(n)
    return num_primi

