def post(fposts,insieme):
    
    
    keyid=elaborapost2(fposts)
    postitem=elaborapost(fposts)
    lun=len(keyid)
    dizpost=dictionary(lun,postitem,keyid)
    return(trovato(dizpost,insieme))

def dictionary(lun,postitem,keyid):
    dizio={}
    for a in range(len(keyid)):
        dizio.update({str(postitem[a]):str(keyid[a])})
    return dizio

def trovato(dizpost,insieme):
    final=set()
    for b in dizpost:
       for c in dizpost[b]:
            if not c.isalpha():
                dizpost[b]=dizpost[b].replace(c,' ')
       for p in insieme:
           if p.upper() in dizpost[b].split():
               final.add(b)
               break
    return final

def elaborapost(file):
    
    keyid=[]
    file=open(file)
    for raw in file:
        if raw.find('<POST>')!= -1:
            b=raw.strip()
            a=list(b)
            a.insert(6,' ')
            c=''.join(a)
            keyid+=[int(n) for n in c.split() if n.isdigit()]
    return keyid 
        

def elaborapost2(file):
    
    file=open(file)
    testo=file.read()
    lista=[]
    testo1=testo.split('<POST>')
    for n in range(len(testo1)):
        lista+=[testo1[n].upper().strip()]
    return lista[1:]

def useless():
    '''questa funzione è inutile'''
    return

def useless2():
    '''questa funzione è inutile'''
    
def useless3():
    '''questa funzione è inutile '''
        
        