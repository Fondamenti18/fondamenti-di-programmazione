def codifica (chiave,testo):
    chiave_f = []
    chiave_ordinata = []
    chiave_n = ""
    for i in chiave :
        if i >= "a" and i <= "z" :
            chiave_n += i
    for x,y in enumerate(chiave_n) :
        if chiave_n.count(y,x) == 1 :
            chiave_f.append(y)
    chiave_ordinata = sorted(chiave_f)
    c = 0
    d = {}
    while c < len(chiave_f):
        d[chiave_ordinata[c]] = chiave_f[c]
        c = c + 1
    s = ""
    for k in testo:
        if (k in d.keys()):
            s+=d[k]
        else:
            s+=k
                
    
    return s

def decodifica (chiave,testo) :
    chiave_f = []
    chiave_ordinata = []
    chiave_n = ""
    for i in chiave :
        if i >= "a" and i <= "z" :
            chiave_n += i
    for x,y in enumerate(chiave_n) :
        if chiave_n.count(y,x) == 1 :
            chiave_f.append(y)
    chiave_ordinata = sorted(chiave_f)
    c = 0
    d = {}
    while c < len(chiave_f):
        d[chiave_f[c]] = chiave_ordinata[c]
        c = c + 1
    s = ""
    for k in testo:
        if (k in d.keys()):
            s+=d[k]
        else:
            s+=k
                
    
    return s
    
    





