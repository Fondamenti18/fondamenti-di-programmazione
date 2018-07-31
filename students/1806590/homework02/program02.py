        
def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    import json
    comp={}
    ris={}
    
    f = open(fcompiti, "r")
    f = f.read().split('comp')
    f[:]=[x.strip() for x in f if x!='']
    for x in f:
        x=x.split('sub')
        x[:]=[a.strip() for a in x]
        comp[x[0]]=x[1:]

    for n in comp:
        sub=[]
        if n in insi:
           
           sub+=comp[n]
           for a in sub:
                sub[:]+=comp[a]
           sub.reverse()
           ris[n]=sub

    r=open(fout,"w", encoding='utf-8')
    json.dump(ris, r)
    r.close()

    


    
