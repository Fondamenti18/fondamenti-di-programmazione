import json
valore = 0
def dizionario_gradi_antenati(fnome,y,fout):
    f = open(fnome,'r',encoding = 'UTF-8')
    out = open(fout,'w',encoding = 'UTF-8')
    dAl = json.load(f)
    d = {radice(fnome):0}
    aInv = inv(dAl)
    for k in aInv:
        ant(dAl, aInv, y, k, 0, fnome)
        d[k] = valore
    print(json.dumps(d),file = out)
    f.close()
    out.close()
    return d
def radice(f):
    f = open(f,'r',encoding = 'UTF-8')
    r = f.readline()[2:]
    r = r[0:r.find('"')]
    return r
def dizionario_livelli(fnome,fout):
    f = open(fnome,'r',encoding = 'UTF-8')
    out = open(fout,'w',encoding = 'UTF-8')
    dAl = json.load(f)
    d = {}
    o = radice(fnome)
    levels(dAl, o, d, 0)
    order(d)
    print(json.dumps(d),file = out)
    f.close()
    out.close()
    return d
def al(albero, k, out):
    if k in albero.keys():
        if albero[k] != []:
            out[k] = albero[k]
            for v in albero[k]:
                al(albero, v, out)
        else:
            out[k] = []
def cancella_sottoalbero(fnome,x,fout):
    f = open(fnome,'r',encoding = 'UTF-8')
    out = open(fout,'w',encoding = 'UTF-8')
    dAl = json.load(f)
    d = {}
    eraseAl(dAl, x, d)
    print(json.dumps(d),file = out)
    f.close()
    out.close()
    return d
def erase(albero, v):
    for k in albero.keys():
        if v in albero[k]:
            albero[k].remove(v)
def genera_sottoalbero(fnome,x,fout):
    f = open(fnome,'r',encoding = 'UTF-8')
    out = open(fout,'w',encoding = 'UTF-8')
    dAl = json.load(f)
    d = {}
    al(dAl, x, d)
    print(json.dumps(d),file = out)
    f.close()
    out.close()
    return d
def eraseAl(albero, k, out):
    canc = {}
    al(albero, k, canc)
    erase(albero, k)
    for k in albero:
        if k not in canc:
            out[k] = albero[k]
def ant(albero, inv, n, k, c, f):
    global valore
    o = radice(f)
    if k != o and albero[k]!=o:
        if len(albero[inv[k]]) == n:
            c+=1
        ant(albero, inv, n, inv[k], c, f)
    else:
        valore = c
def levels(albero, nodo, out, lv):
    if str(lv) not in out:
        out[str(lv)] = [nodo]
    else:
        out[str(lv)].append(nodo)
    if albero[nodo] != []:
        for k in albero[nodo]:
            levels(albero, k, out, lv + 1)
def inv(albero):
    d = {}
    for k in albero:
        for e in albero[k]:
            if albero[k]!=[]:
                d[e] = k
    return d
def order(d):
    for k in d:
        d[k].sort()
def fun(s):
    return s+' '+s







    






