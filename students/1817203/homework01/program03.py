def codifica(chiave, testo):
    dkey,lkey=disordinata(chiave)
    okey=ordinata(lkey)
    diz={}
    for x in range(len(okey)):
        diz[okey[x]]=dkey[x]
    ctxt=trasforma(testo,diz)
    
    return ctxt

def disordinata(key):
    lkey=[]
    for x in range(len(key)-1,-1,-1):
        if not key[x] in lkey:
            lkey+=key[x]
    lkey.reverse()        
    for i in range (len(lkey)-1,-1,-1):
        if lkey[i]<'a' or lkey[i]>'z':
            del(lkey[i])
    dkey=''.join(lkey)
         
    return dkey,lkey

def ordinata(lkey):
    okey=''.join(sorted(lkey)) 
    return okey

def trasforma(testo,diz):
    ltxt=list(testo)
    for x in range(len(ltxt)):
        if ltxt[x] in diz:
            ltxt[x]=diz[ltxt[x]]
    ctxt=''.join(ltxt)
        
    return ctxt        

def decodifica(chiave, testo):
    dkey,lkey=disordinata(chiave)
    okey=ordinata(lkey)
    diz={}
    for x in range(len(okey)):
        diz[dkey[x]]=okey[x]
    dtxt=trasforma(testo,diz)
    
    return dtxt
    
    
