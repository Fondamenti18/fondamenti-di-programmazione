'''
                             'a'
                              |
                _____________'b'____________             
               |                            |            
              'c'                  ________'d'_______   
               |                  |                  |  
              'i'         _______'e'_______         'l'
                         |        |        |               
                        'f'      'g'      'h'
'''




import json

############################## FUNZIONI GENERICHE

def apri(fnome):
    with open(fnome, encoding = "utf-8") as f:
        return json.load(f)

def salva(d1, fout):
    with open(fout, "w", encoding = "utf-8") as f:
        json.dump(d1, f)
        
def trova_radice(dizionario):
    lista = []
    for chiave in dizionario:
        lista += dizionario[chiave]
    insieme = set(lista)
    for chiave in dizionario:
        if chiave not in insieme:
            return chiave
        
############################## PRIMA FUNZIONE

def genera_sottoalbero(fnome,x,fout):
    d = apri(fnome)
    d1 = dict()
    gen_ricorsione_sottoalbero(d1, d, x)
    salva(d1, fout)
    
def gen_ricorsione_sottoalbero(d1, d, x):
    if x not in d:
        d1[x] += []
    else:
        d1[x] = []
        for a in d[x]:
            d1[x] += [a]
            gen_ricorsione_sottoalbero(d1, d, a)
        
############################## SECONDA FUNZIONE

def cancella_sottoalbero(fnome,x,fout):
    d = apri(fnome)
    radice = trova_radice(d)
    if x != radice:
        d1 = dict()
        gen_tree(d, d1, radice, x)
    else:
        d1 = dict()
    salva(d1, fout)
    
def gen_tree(d, d1, key, x):
    d1[key] = []
    for k in d[key]:
        if k != x:
            d1[key] += [k]
            gen_tree(d, d1, k, x)

################################ TERZA FUNZIONE

def dizionario_livelli(fnome,fout):
    d = apri(fnome)
    radice = trova_radice(d)
    d1 = {0 : [radice]}
    gen_lv_tree(d, radice, 1, d1)
    salva(d1, fout)
    
def gen_lv_tree(d, key, lv, d1):
    if lv not in d1 and d[key] != []:
        d1[lv] = []
    for k in d[key]:
        d1[lv] += [k]
        gen_lv_tree(d, k, lv + 1, d1)
        d1[lv].sort()
		
################################# QUARTA FUNZIONE

def dizionario_gradi_antenati(fnome,y,fout):
    d = apri(fnome)
    radice = trova_radice(d)
    d1 = dict()
    gen_gradi(d, d1, y, 0, radice)
    salva(d1, fout)
    
def gen_gradi(d, d1, y, num, att):
    d1[att] = num
    if len(d[att]) == y:
        for k in d[att]:
            gen_gradi(d, d1, y, num + 1, k)
    else:
        for k in d[att]:
            gen_gradi(d, d1, y, num, k)
    
        
    