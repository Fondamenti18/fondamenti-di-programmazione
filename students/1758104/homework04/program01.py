
import os, json


test_files = []
for file in os.listdir():
    if file.startswith('Alb') and file.endswith('.json'):
        test_files.append(file)

trees_caricati = dict()
for path in test_files:
    file = open(path)
    albero = json.load(file)
    trees_caricati[path] = albero
    file.close()


def genera_sottoalbero_tmp(data, chiave):
    generato = list()
    generato.append((chiave, data[chiave]))
    for figlio in data[chiave]: generato += genera_sottoalbero_tmp(data, figlio)
    return generato

def genera_sottoalbero(fnome, chiave, fout):
    
    generato = list()
    with open(fnome, encoding='utf-8') as f: originale = json.load(f)

    generato.append( (chiave, originale[chiave]) )
    
    for figlio in originale[chiave]:
        generato += genera_sottoalbero(fnome, figlio, fout)
    
    

    with open(fout, 'w', encoding='utf8') as save: json.dump(dict(generato), save)
    

    return generato

def cancella_sottoalbero(fname, chiave, fout):

    subtraction = {key: trees_caricati[fname][key] for key in
                   set(list(trees_caricati[fname].keys())) - set(
                       list(dict(genera_sottoalbero_tmp(trees_caricati[fname], chiave)).keys()))}
    
    for ls in subtraction.values():
        if chiave in ls: ls.remove(chiave)
    
    with open(fout, 'w', encoding= 'utf8') as f:
        json.dump(subtraction, f)
    
def gen_lev(originale, chiave, gen = {}, lev = 0):
    
    if str(lev) not in gen.keys():
        gen[str(lev)] = [chiave]
    else:
        if chiave not in gen[str(lev)]:
            gen[str(lev)] += [chiave]
    
    for figlio in originale[chiave]:
        gen = gen_lev(originale, figlio, gen = gen, lev = lev + 1)
        
    return gen


def dizionario_livelli(fnome, fout):
    
    diz = trees_caricati[fnome]
    tree = gen_lev(diz, list(diz.keys())[0])
    for nodo in tree: tree[nodo] = sorted(tree[nodo])
    with open(fout, 'w', encoding= 'utf8') as file:
        json.dump(tree, file)
    



def dizionario_gradi_antenati(fnome, y, fout):
    '''inserire qui il vostro codice'''

