
import json

def genera_sottoalbero(fnome,x,fout):
    d = carica(fnome)
    lista = [b for b in d[x]]
    ris = {}
    sotalb(lista,d,ris)
    ris[x] = d[x]
    salva(fout,ris)
        
def sotalb(lista,d,ris):
    for i in lista:
        if i in d:
            l1 = [b for b in d[i]]
            ris[i] = l1
            if d[i] != []: sotalb(l1,d,ris)

def cancella_sottoalbero(fnome,x,fout):
    d = carica(fnome)
    ris = {}
    rad = trovarad(d)
    lista = [b for b in d[rad] if b != x]
    cst(lista,d,ris,x)
    ris[rad] = [b for b in d[rad] if b != x]
    salva(fout,ris)
    
def cst(lista,d,ris,x):
    for i in lista:
        if i in d:
            ris[i] = [b for b in d[i] if b != x]
            if d[i] != []: cst([b for b in d[i] if b != x],d,ris,x)
    

def dizionario_livelli(fnome,fout):
    d = carica(fnome)
    rad = trovarad(d)
    ris = {}
    h = 0
    ris = crealiv(rad,d,ris,h)
    salva(fout,ris)
    
def crealiv(n,d,ris,h):
    if h in ris:
        ris[h] += [n]
        ris[h].sort()
    else: ris[h] = [n]
    h += 1
    for i in d[n]:
        crealiv(i,d,ris,h)
    return ris
        

def dizionario_gradi_antenati(fnome,y,fout):
    d = carica(fnome)
    rad = trovarad(d)
    ris = {}
    ris[rad] = 0
    listak = list(d.keys())
    listak.remove(rad)
    ris[rad] = 0
    creaant(rad,y,ris,d)
    salva(fout,ris)


def creaant(k,y,ris,d):
    for i in d[k]:
        if len(d[k]) == y: 
            ris[i] = ris[k] +1
        else: ris[i] = ris[k]
        creaant(i,y,ris,d)
    return 


def carica(fnome):
    with open(fnome) as f:
        d = json.load(f)
    return d

def salva(fout,ris):
    with open(fout, "w") as f:
        json.dump(ris, f)
        
def trovarad(d):
    listak = d.keys()
    listav = d.values()
    v = set()
    for j in listav:
        for x in j:
            v.add(x)
    for i in listak:
        if i not in v: return i