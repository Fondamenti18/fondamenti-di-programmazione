
import json
def pianifica(fcompiti,insi,fout):
    op_file=open(fcompiti,"r")
    diz=creazionediz(op_file)
    dizp={}
    for i in insi:
        bho=controllo(i,diz)
        if bho!='errore':
            dizp[i]=bho
    opfout=open(fout,mode="w")
    json.dump(dizp,opfout)
    opfout.close()
    op_file.close()
                
def creazionediz(op_file):
    diz={}
    riga_file=op_file.readline()
    while riga_file != '':     
        ns=0
        if ('comp' in riga_file):
            nm=[]
            for i in riga_file:
                if i.isnumeric():
                    nm+=[i]
            nc=''.join(nm)
            nc=int(nc)
        if ('sub' in riga_file):
            nm=[]
            for i in riga_file:
                if i.isnumeric():
                    nm+=[i]
            ns=''.join(nm)
            ns=int(ns)
        diz[nc]=ns
        riga_file=op_file.readline()
    return(diz)

def controllo(i,diz):
        i=int(i)
        a=diz.get(i,'')
        if a=='':
            return('errore')
        if a==0:
            return([])
        retur=[str(a)]
        while a!='':
            a=diz.get(a,'')
            if a!=0 and a!='':
                 retur+=[str(a)]  
        retur.reverse()
        return(retur)

