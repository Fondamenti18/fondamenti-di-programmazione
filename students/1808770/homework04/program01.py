import json

def genera_sottoalbero(fnome,x,fout):
    d,k=openjson(fnome),x
    d1={k:d[k]}
    rec12(k,d,d1)
    save(d1,fout)

def cancella_sottoalbero(fnome,x,fout):
    d,k=openjson(fnome),x
    d1={k:d[k]}
    rec12(k,d,d1)
    d2={}
    for item in d.items():
        if item not in d1.items():
            if k in item[1]:
                item[1].remove(k)
            d2.update({item[0]:item[1]})
    save(d2,fout)

def dizionario_livelli(fnome,fout):
    d=openjson(fnome)
    d3={}
    for item in d.items():
        if len(d3)==0:
            d3.update({"0":[item[0]]})
        if len(item[1])==1:
            d3.update({str(len(d3)):item[1]})
        elif len(item[1])>1:
            d3.update({str(len(d3)):sorted(item[1])})
            rec3(item[1],len(d3),d,d3)
            break
    save(d3,fout)

def dizionario_gradi_antenati(fnome,y,fout):
    d=openjson(fnome)
    d4={}
    for item in d.items():
        rec4(item[0],0,d,d4,y,item[0])
    save(d4,fout)


def rec12(k,d,d1):
    for v in d[k]:
        d1.update({v:d[v]})
        rec12(v,d,d1)

def rec3(values,c,d,d3):
    lista=[]
    for v in values:
        if v in d.keys() and len(d[v])!=0:
            lista.append(d[v])
    rec33(lista,c,d,d3)
def rec33(lista,c,d,d3):
    lista=[x for y in lista for x in y]
    if len(lista)!=0:
        d3.update({str(c):sorted(lista)})
        rec3(lista,c+1,d,d3)

def rec4(k,c,d,d4,y,kk):
    for item in d.items():
        if k in item[1]:
            if len(item[1])==y:
                c+=1
            rec4(item[0],c,d,d4,y,kk)
    if kk not in d4.keys():
        d4.update({kk:c})

def openjson(fnome):
    with open(fnome) as infile:
        return json.load(infile)
def save(dictionario,fout):
    with open(fout,"w") as outfile:
        json.dump(dictionario,outfile)