import json

def genera_sottoalbero(fnome,x,fout):
    global ck1
    with open(fnome) as t:
        d1_l=json.load(t)
        global d1
        d1=d1_l.copy()
        global lista1
        lista1=[x]
        global dizfin
        dizfin={}
        if len(dizfin)==0:
            ric_genera_sottoalbero()
        else:
            pass
        
    with open(fout, 'w') as f:
            scritt=json.dumps(dizfin)
            f.write(scritt)

def ric_genera_sottoalbero():
    global lista1
    global dizfin
    if lista1[0] in d1:
        dizfin[lista1[0]]=d1[lista1[0]]
        lista1=lista1+d1[lista1[0]]
    else:
        pass
    lista1.remove(lista1[0])
    if len(lista1)!=0:
        return ric_genera_sottoalbero()
    else:
        return genera_sottoalbero


def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as t:
        d1=json.load(t)
        global lista1
        lista1=[x]
        global dizfin
        dizfin={}
        
        if len(dizfin)==0:
            ric_cancella_sottoalbero()
        else:
            pass
        
        lista3=[]
        for l2 in d1:
            if x in d1[l2]:
                lista3=lista3+[l2]
        for l3 in d1[lista3[0]]:
            d1[lista3[0]].remove(x)
        for l in dizfin:
            del d1[l]
    with open(fout, 'w') as f:
            scritt=json.dumps(d1)
            f.write(scritt)

def ric_cancella_sottoalbero():
    global lista1
    global dizfin
    if lista1[0] in d1:
        dizfin[lista1[0]]=d1[lista1[0]]
        lista1=lista1+d1[lista1[0]]
    else:
        pass
    lista1.remove(lista1[0])
    if len(lista1)!=0:
        return ric_cancella_sottoalbero()
    else:
        return cancella_sottoalbero

       
def dizionario_livelli(fnome,fout):
    with open(fnome) as t:
        lett=json.load(t)
        d1=lett.copy()
        global d1_l
        d1_l=list(d1)
        global lista1
        lista1=[]
        global dizfin
        dizfin={}
        global counter
        counter=0
        
        for v in d1.keys():
            dizfin['0']=[v]
            lista1=[v]
            break
        
        global val_l
        val_l=0
        
        if len(dizfin)==1:
            ric_diz_livelli()
        
        listafin=[]
        for val in dizfin:
            if len(dizfin[val])==0:
                listafin=listafin+[val]
        for val2 in listafin:
            if val2 in dizfin:
                dizfin.pop(val2)
        
    with open(fout, 'w') as f:
            scritt=json.dumps(dizfin)
            f.write(scritt)

def ric_diz_livelli():
    lista2=[]
    global val_l
    global lista1
    for v in lista1:
        if v in d1_l:
            lista2=lista2+d1[v]
            if str(val_l+1) in dizfin:
                dizfin[str(val_l+1)] += d1[v]
                dizfin[str(val_l+1)] = sorted(dizfin[str(val_l+1)])
            else:
                dizfin[str(val_l+1)]=d1[v]
    lista1.remove(v)
    lista1=lista2
    val_l=val_l+1
            
    if len(lista1)!=0:
        return ric_diz_livelli()
    else:
        return dizionario_livelli


def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as t:
        lett=json.load(t)
        global d1
        d1=lett.copy()
        d1_l=list(d1)
        global lista1
        lista1=[]
        global dizfin
        dizfin={}
        global counter
        counter=0
        
        if len(d1_l)>20001:
            dizfin[d1_l[len(d1_l)-1]]=0
            lista1=[[d1_l[len(d1_l)-1],0]]
        else:
            for v in d1.keys():
                dizfin[v]=0
                lista1=[[v,0]]
                break

        if len(dizfin)==1:
            ric_diz_gradi_antenati(y)
        else:
            pass
        
        with open(fout, 'w') as f:
                scritt=json.dumps(dizfin)
                f.write(scritt)

def ric_diz_gradi_antenati(y):
    lista2=[]
    global val_l
    global lista1
    for v in lista1:
        if v[0] in d1:
            dizfin[v[0]] = v[1]
            for x in d1[v[0]]:
                if len(d1[v[0]])==y:
                    lista2=lista2+[[x,v[1]+1]]
                else:
                    lista2=lista2+[[x,v[1]]]
    lista1.remove(v)
    lista1=lista2
    if len(lista1)!=0:
        return ric_diz_gradi_antenati(y)
    else:
        return dizionario_gradi_antenati



