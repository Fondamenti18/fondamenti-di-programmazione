import json
import copy

#blocco numero 1
def gen(diz,ndiz,x):
    for el in diz[x]: gen(diz,ndiz,el)
    ndiz[x]=diz[x]
    return ndiz
        
def genera_sottoalbero(fnome,x,fout):
    with open(fnome) as fin: diz = json.load(fin)
    if x in diz.keys(): ndiz= gen(diz,{},x)
    else: ndiz={}
    with open(fout, 'w') as fout: json.dump(ndiz, fout)



#blocco numero 2
def canc(diz,x):
    for el in diz[x]:canc(diz,el)   
    del diz[x]    
    return diz

def pulisci(diz,x):
    for chiave,valori in diz.items():
        for valore in valori:
            if valore == x:
                i=valori.index(valore)
                diz[chiave]=valori[:i]+valori[i+1:]
                return diz

def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as fin: diz = json.load(fin)
    if x in diz.keys(): ndiz=pulisci(canc(diz,x),x)
    else: ndiz=diz
    with open(fout, 'w') as fout: json.dump(ndiz, fout)
    


#blocco numero 3
def livelli(liv,val,diz,ndiz):
    if liv not in ndiz:ndiz[liv]=[val]
    else:ndiz[liv]+=[val]
    for nval in diz[val]:livelli(liv+1,nval,diz,ndiz)
    return ndiz

def pulisci2(ndiz):
    for chiave,valori in ndiz.items():
        if len(valori)>1: ndiz[chiave].sort()
    return ndiz

def get_insieme(diz):
    ins=set()
    for valori in diz.values():
        for valore in valori:
            ins.add(valore)
    return ins

def trova_radice(diz):
    ins=get_insieme(diz)  
    for chiave, valori in diz.items():
        if len(valori)>0:
            if chiave not in ins:
                return chiave

            
            
def dizionario_livelli(fnome,fout):
    with open(fnome) as fin: diz = json.load(fin)
    radice=trova_radice(diz)
    ndiz=pulisci2(livelli(0,radice,diz,{}))
    with open(fout, 'w') as fout: json.dump(ndiz, fout)



#blocco numero 4
def antenati(diz,ndiz,el,grado,y):
    for el1 in diz[el]:
        if len(diz[el])==y:antenati(diz,ndiz,el1,grado+1,y)
        else:antenati(diz,ndiz,el1,grado,y)
    ndiz[el]=grado
    return ndiz
            
def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as fin: diz = json.load(fin)
    radice=trova_radice(diz)
    ndiz=antenati(diz,{},radice,0,y)
    with open(fout, 'w') as fout: json.dump(ndiz, fout)
