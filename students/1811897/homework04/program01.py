import json



def genera_sottoalbero(fnome,x,fout):
    file=json.load(open(fnome))
    diz={}
    a=trova(file,diz,x)
    ff=open(fout, mode='w')
    json.dump(a,ff)
    ff.close

def trova(file,diz,x):
    for f in file:
        if f==x:
            diz[f]=file[f]
            if file[f]==[]:
                return None
            else:
                for c in file[f][::-1]:
                    trova(file,diz,c)
    return diz

def cancella_sottoalbero(fnome,x,fout):
    h=json.load(open(fnome))
    diz={}
    a=trova(h,diz,x)
    diz=h
    s=0
    for c in a:
        del diz[c]
    for y in diz:
        if x in diz[y]:
            for cc in diz[y]:
                s+=1
                if x==cc:
                    s=s-1
                    a=diz[y]
                    del a[s]
    ff=open(fout, mode='w')
    json.dump(diz,ff)
    ff.close    
    

def dizionario_livelli(fnome,fout):
    aaa=json.load(open(fnome))
    a=pr(aaa)
    aa=a.split()
    ris=ll(aa,aaa,i=0)
    ff=open(fout, mode='w')
    json.dump(ris,ff)
    ff.close

def pr(file):
    for x in file:
        con=True
        con=pr_p(x,file)
        if con:
            return x
def pr_p(y,file):
    t=y
    for x in file.items():
        for a in x:
            if t in x[1]:
                return False
    return True

def ll(e,lis,i):
    new=[]
    ris={}
    if not e:
        return {}
    for el in e:
        ris.setdefault(i,[]).append(el)
        new.extend(lis.get(el,[]))
        new.sort()
    i=i+1
    ris.update(ll(new,lis,i))
    return ris



def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''


#n1=genera_sottoalbero('Alb10_1.json','d','risAlb10_1.json')
#n1=cancella_sottoalbero('Alb10_2.json','d','risAlb10_1.json')
#n2=dizionario_livelli('Alb10.json','tAlb10_3.json')


