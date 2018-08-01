import json

def genera_sottoalbero(fnome,x,fout):
    with open(fnome) as json_file:
        entrydict=json.load(json_file)
    outd={}
    diz1=sub_genera(entrydict,x,outd)
    with open(fout,'w') as outfile:
        json.dump(diz1,outfile)
    
def sub_genera(ind,x,outd):
    y=ind[x]
    outd[x]=y
    if len(y)>0:
        for el in y:
            sub_genera(ind,el,outd)
    return outd
    

def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as json_file:
        entrydict=json.load(json_file)
    removelist=[]
    sub_cancella(entrydict,x,removelist)
    removelist.append(x)
    for el in removelist:
        del entrydict[el]
    for v in entrydict:
        j=entrydict[v]
        if x in j:
            j.remove(x)
            entrydict[v]=j
            break
    with open(fout,'w') as outfile:
        json.dump(entrydict,outfile)
        
def sub_cancella(ind,x,removelist):
    y=ind[x]
    if len(y)>0:
        for el in y:
            removelist.append(el)
            sub_cancella(ind,el,removelist)

def dizionario_livelli(fnome,fout):
    with open(fnome) as json_file:
        entrydict=json.load(json_file)
    delset=set()
    for el in entrydict:
        for i in entrydict[el]:
            delset.add(i)
    for el in entrydict:
        if el not in delset:
            k=el
            break
    outd={0:[k]}
    sub_livelli(entrydict,0,outd)
    removelist=[]
    for el in outd:
        if outd[el]==[]:
            removelist.append(el)
        else:
            outd[el]=sorted(outd[el])
    for i in removelist:
        del outd[i]
    with open(fout,'w') as outfile:
        json.dump(outd,outfile)

def sub_livelli(ind,x,outd):
    outd[x+1]=[]
    if len(outd[x])>0:
        for el in outd[x]:
            for i in ind[el]:
                outd[x+1].append(i)
        sub_livelli(ind,x+1,outd)
    
    

def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as json_file:
        entrydict=json.load(json_file)
    antdiretto=antenato_diretto(entrydict)
    outd={}
    for el in entrydict:
        gcounter=0
        sub_antenati(antdiretto,el,antdiretto[el],entrydict,y,gcounter,outd)
    with open(fout,'w') as outfile:
        json.dump(outd,outfile)
        
        
def calc_antenato(ind,q):
    k=len(ind[q])
    return k

def antenato_diretto(ind):
    outd={}
    for i in ind:
        for el in ind[i]:
            outd[el]=i
    for k in ind:
        if k not in outd:
            outd[k]=[]
    return outd

def sub_antenati(antdiretto,x,newx,ind,y,gcounter,outd):
    if newx!=[]:
        if calc_antenato(ind,newx)==y:
            gcounter+=1
        sub_antenati(antdiretto,x,antdiretto[newx],ind,y,gcounter,outd)
    else:
        outd[x]=gcounter