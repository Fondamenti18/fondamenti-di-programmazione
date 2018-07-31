from json import dump        
def pianifica(fcompiti,insi,fout):
    f=open(fcompiti,encoding='utf-8')
    diz=cread(f)    
    inter=set(diz.keys())&insi
    dout=creado(inter,diz)
    f.close()
    f=open(fout,'w')
    dump(dout,f)
    f.close()

def cread(f):
    riga=f.readline()
    diz={}
    while riga!='':
        if 'comp' in riga:
            idcomp=indicizza(riga)
            diz[idcomp]=''
        else:
            idsub=indicizza(riga)
            diz[idcomp]=idsub
        riga=f.readline()
    return diz


def indicizza(riga):
    indice=''
    for x in riga:
        if x.isdigit():
            indice+=x
    return indice

def creado(inter,diz):
    dout={}
    for x in inter:
        if diz[x]=='':
            dout[x]=[]
        else:
            l=creal(x,diz)
            lr=crealr(l)
            dout[x]=lr
    return dout

def creal(k,diz):
    l=[]
    while diz[k]!='':
        l+=[diz[k]]
        k=diz[k]
    return l

def crealr(l):
    lr=[]
    for i in range(len(l)-1,-1,-1):
        lr+=[l[i]]
    return lr
    