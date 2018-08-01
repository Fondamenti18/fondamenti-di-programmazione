def chiave(s):
    lista=[]
    seq_dis=''
    i=len(s)-1
    while i>=0:
        if 'a'<=s[i]<='z':
            lista=[s[i]]+lista
            if s[i] in lista[1: ]:
                lista.remove(s[i])
        i-=1
    return seq_dis.join(lista)
def inverti(stringa):
    seq_ord=''
    a=chiave(stringa)
    return seq_ord.join(sorted(a))
def coppie(s):
    d={}
    p=0
    s1=chiave(s)
    s2=inverti(s)
    while p<len(s1):
        d[s2[p]]=s1[p]
        p+=1
    return d
def coppie_1(s):
    d={}
    p=0
    s1=chiave(s)
    s2=inverti(s)
    while p<len(s1):
        d[s1[p]]=s2[p]
        p+=1
    return d

def codifica(chiave, testo):
    cr=''
    d=coppie(chiave)
    for x in testo:
        if x in d.keys():
            cr=cr+str(d.get(x, ))
        else:
            cr=cr+x
    return cr
def decodifica(chiave, testo):
    dr=''
    d=coppie_1(chiave)
    for x in testo:
        if x in d.keys():
            dr=dr+str(d.get(x, ))
        else:
            dr=dr+x
    return dr
