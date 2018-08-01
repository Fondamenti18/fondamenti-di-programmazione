def verifica(struttura,parola):
    v=True
    d={}
    c=0
    if len(struttura)==len(parola):
        for x in struttura:
            if x in d:
                if d[x]==parola[c]:
                    pass
                else:
                    v=False
            else:
                if parola[c] in d.values():
                    v=False
                else:
                    d[x]=parola[c]
            c+=1
    else:
        v=False
    return v

def lista(struttura,insieme):
    l=[]
    for k in insieme:
        if verifica(struttura,k)==True:
            l=l+[k]
    return set(l)
    
def decod(pfile,codice):
    file=open(pfile,'r')
    a=set()
    for x in file:
        a.add(x[:-1])
    return lista(codice,a)