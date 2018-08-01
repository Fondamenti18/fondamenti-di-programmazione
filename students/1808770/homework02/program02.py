import json

def pianifica(fcompiti,insi,fout):
    dictionario={}
    with open(fcompiti,"r") as infile:
        lines=infile.read()
        lns="".join([y for y in lines if y.isalnum()])
        for x in sorted(insi,key=int,reverse=True):
            if "comp"+x in lns:
                lista=[]
                dictionario.update({x:loop(lns,x,lista)})
    save(dictionario,fout)

def loop(lns,x,lista):
    while lns.find("comp"+x+"sub")!=-1:
        n_sub=""
        for n in lns[lns.find(("comp"+x+"sub"))+len(("comp"+x+"sub")):]:
            if n.isdigit()==False:
                lista.append(n_sub)
                break
            n_sub+=n
        x=n_sub
    return lista[::-1]

def save(dictionario,fout):
    with open(fout,"w") as outfile:
        json.dump(dictionario,outfile)
