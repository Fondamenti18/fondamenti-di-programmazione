import json
d = {}
d1 = {}
cm = 0
def genera_sottoalbero(fnome,x,fout):
    global d1,cm,d
    if cm == 0:
        x = [x]
        cm = 1
    d2 = {}
    a = (open(fnome,'r').read())
    d = json.loads(a)
    t = len(x)
    r = []
    for i in range(t):
        d2[x[i]] = d[x[i]]
        r+= d[x[i]]
    d2.update(d1)
    d1 = d2
    if r == []:
        with open(fout, "w") as f:
            json.dump(d1, f)
            d1 = {}
            cm = 0
        return 
    x = r
    return genera_sottoalbero(fnome,x,fout)
cm = 0
def cancella_sottoalbero(fnome,x,fout):
    global d
    global cm
    if cm == 0:
        d = list(d.items())
        u = len(d)
        for i in range (u):
            if x in d[i][1]:
                b8 = d[i][1]
                del b8[d[i][1].index(x)]
                d = dict(d)
                cm+=1
                x = [x]
                break        
    t = len(x)
    r = []
    for i in range(t):
        r+= d[x[i]]
        del d[x[i]]    
    if r == []:
        with open(fout, "w") as f:
            json.dump(d, f)
            cm = 0
        return
    x = r
    return cancella_sottoalbero(fnome,x,fout)
mc = 0
dm = {}
cr = 0

def dizionario_livelli(fnome,fout):
    global mc,dm,cr,dga
    if len(fout) > 2:
        fout = [fout]
        a = (open(fnome,'r').read())
        dga = json.loads(a)
        d = ricerca_chiave(dga)
        m = list(d.items())
        fout+= [m[0][1]]
        dm[str(mc)] = [m[0][0]]
        return dizionario_livelli(fnome,fout)
    cr+=1
    a = (open(fnome,'r').read())
    d = json.loads(a)
    x = fout[1]
    r = []
    if type(x) == str:
        x = [x]
    dm[str(cr)] = sorted(x)
    for i in range(len(x)):
        mc+=1
        x1 = x[i]
        r += d[x1]
    if r == []:
        fout = fout[0]
        with open(fout, "w") as f:
            json.dump(dm, f)
        mc = 0
        dm = {}
        cr = 0
        return 
    del fout[1]
    fout+=[r]
    return dizionario_livelli(fnome,fout)
diz1 = {} 
dga = ''
cga = 0
def dizionario_gradi_antenati(fnome,y,fout):
    global diz1,cga,dga
    import collections
    if cga == 0:
        a = (open(fnome,'r').read())
        dga = json.loads(a)
        cga+=1
        dga = ricerca_chiave(dga)
        m = list(dga.items())
        diz1[m[0][0]] = 0
        return(dizionario_gradi_antenati(fnome,y,fout))
    d = dga
    m = list(d.items())
    for i in range(0,len(d)):
        u = m[i][1]
        u1 = m[i][0]
        lu = len(u)
        for i1 in range(lu):
            u2 = u[i1]
            if lu == y:
                r = diz1[u1] + 1
                diz1[u2] = r
            else:
                r = diz1[u1]
                diz1[u2] = r
    diz1 = dict(collections.OrderedDict(sorted(diz1.items())))
    with open(fout, "w") as f:
            json.dump(diz1, f) 
    diz1 = {} 
    dga = ''
    cga = 0
    return ()
                        
                
  
def ricerca_chiave(dga):
    m = list(dga.values())
    m = [item for sublist in m for item in sublist] 
    m1 = list(dga.keys())
    for i in range(len(m1)):
        if m1[i] not in m:
            if i > 0:
                dga = list(dga.items())
                m3 = dga[i]
                del dga[i]
                dga = [m3] + dga
                dga = dict(dga)
    return(dga)
