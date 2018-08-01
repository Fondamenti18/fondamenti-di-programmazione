import json

def pianifica(fcompiti,insi,fout):
    taon=filetolist(fcompiti)
    clean=compsubdict(taon)
    f=finaldictionary(clean,insi)
    with open(fout,'w') as outfile:
        json.dump(f,outfile)



def filetolist(file):
    r=open(file,'r')
    s=r.readlines()
    newlist=[]
    for t in s:
        t=t[:-1]
        t=t.split()
        newlist.append(''.join(t))
    newlist.append(' ')
    return newlist


def compsubdict(newlist):
    dizio={}
    iddict=indexdict(newlist)
    for i in newlist:
        if i[0]!='c':
            continue
        elif newlist[iddict[i]+1][0]!='s':
            dizio[i[4:]]=''
        else:
            dizio[i[4:]]=newlist[iddict[i]+1][3:]
    return dizio


def indexdict(newlist):
    iddict={}
    for i in range(0,len(newlist)):
        iddict[newlist[i]]=i
    return iddict


def finaldictionary(s,insi):
    finald={}
    for j in insi:
        i=str(j)
        check=i in s
        if check==False:
            continue
        a=s[i]
        finald[i]=a.split()
        while a!='':
            b=s[a]
            if b!='':
                finald[i]=b.split()+finald[i]
            a=b
    return finald
