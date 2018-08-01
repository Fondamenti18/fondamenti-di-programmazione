import json

def genera_sottoalbero(fnome,x,fout):
    'Funzione main per generare'
    f = apri_file(fnome)
    diz = dict()
    diz = search(f, x, diz)
    salva_file(diz, fout)
    
def search(file, x, diz):
    'Funzione che cerca ricorsivamente per genera_sottoalbero'
    for el in file[x]:
        diz[el] = []
        diz[x] = file[x]
        search(file, el, diz)
    return diz

def cancella_sottoalbero(fnome,x,fout):
    'Funzione main per cancellare'
    f = apri_file(fnome)
    f = remove(f, x)
    # Trova il nodo precedente e rimuove la x dallo stesso
    for k,v in f.items():
        if x in v:
            f[k] = [''.join(v).replace(x, '')]
            break
    salva_file(f, fout)
    
def remove(file, x):
    'Funzione ricorsiva usata per rimuovere i rami a partire da x'
    ls = file[x]
    del file[x]
    for el in ls:
        remove(file, el)
    return file

def dizionario_livelli(fnome,fout):
    'Funzione main per livelli'
    f = apri_file(fnome)
    ins = set()
    ins2 = set()
    diz = dict()
    for val in f.values():
        for el in val:
            ins.add(el)
    ins2.update(f.keys())
    k = ''.join(ins2 - ins)
    diz['0'] = [k]
    diz = level(f, 0 , k, diz)
    for val in diz.values():
        val = val.sort()
    salva_file(diz, fout)
 
def level(file, node, k, diz):
    'Funzione ricorsiva per dizionario_livelli'
    nodo = str(node+1)
    if nodo not in diz and file[k]:
        diz[nodo] = []
    for el in file[k]:
        diz[nodo].append(el)
        level(file, node+1, el, diz)
    return diz
    
def dizionario_gradi_antenati(fnome,y,fout):
    'Funzione main per gli antenati con grado y'
    f = apri_file(fnome)
    ris = dict()
    ins = set()
    ins2 = set()
    for val in f.values():
        for el in val:
            ins.add(el)
    ins2.update(f.keys())
    k = ''.join(ins2 - ins)
    ris[k] = 0
    ris = look_for_ancestors(k, y, ris, f)
    salva_file(ris, fout)
        
def look_for_ancestors(key, y, ris, f):
    'Funzione ricorsiva per dizionario_gradi_antenati'
    if len(f[key]) == y: val = ris[key]+1
    else: val = ris[key]
    for child in f[key]:
        ris[child] = val
        ris = look_for_ancestors(child, y, ris, f)
    return ris

def apri_file(fnome):
    'Funzione usata per aprire i file'
    with open(fnome, 'r') as f_json:
        f = json.load(f_json)
    return f

def salva_file(diz, fout):
    'Funzione usata per salvare i file'
    with open(fout, 'w') as f_data:
        json.dump(diz, f_data)