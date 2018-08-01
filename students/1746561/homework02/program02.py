import re, json

def lista(fin):
    #Crea una lista di stringhe separate a partire dal file
    with open(fin, 'r') as f:
        return [re.findall(r"[^\W\d_]+|\d+", i) for i in [l.replace(' ', '')[:-1] for l in f]]  

def ID(fin, insi): 
    return {i[1] for i in lista(fin) if i[1] in insi}



def ordine(fin, n): 
    ls = lista(fin)
    try:
        for l,ln in zip(ls, ls[1:] + [ls[0]]):
            if l[1] == str(n) and l[0] == 'comp': 
                    if ln[0] == 'comp': return []
                    elif ln[0] == 'sub':
                        return ordine(fin, ln[1]) + [ln[1]]
    except (UnboundLocalError, TypeError): pass

def pianifica(fcompiti, insi, fout):
    with open(fout, 'w') as f:
        f.write(str(json.dumps({n: ordine(fcompiti, int(n)) for n in ID(fcompiti, insi)})))