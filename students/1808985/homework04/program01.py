import json


def dizionario_gradi_antenati(fnome,y,fout):

    dR={}
    dAlbero=apri_json(fnome)

    for chiave in dAlbero.keys():
        dR[chiave]=numero_antenati_grado(dAlbero,chiave,y)

    salva_json(dR,fout)


def numero_antenati_grado(diz,elem,grado,n=0):

    for chiave in diz.keys():
        if elem in diz[chiave]:
            if len(diz[chiave])==grado:
                n+=1
            n=numero_antenati_grado(diz,chiave,grado,n)
            break

    return n


def genera_sottoalbero(fnome,x,fout):

    dAlbero=apri_json(fnome)

    if x not in dAlbero.keys():
        salva_json({},fout)
        return

    salva_json(sottoalbero(dAlbero,x,{}),fout)


def cancella_sottoalbero(fnome,x,fout):

    dAlbero=apri_json(fnome)

    if x not in dAlbero.keys():
        salva_json(dAlbero,fout)
        return

    salva_json(sottrai_alberi(dAlbero,x,sottoalbero(dAlbero,x,{})),fout)


def dizionario_livelli(fnome,fout):

    salva_json(ordina_albero(albero_livelli(apri_json(fnome),0,{},'a')),fout)


def salva_json(d,path):
    with open(path,'w') as f:
        json.dump(d,f)

def apri_json(path):
    with open(path) as f:
        x=json.load(f)
    return x

def sottoalbero(d,x,d2):
    d2[x]=d[x]
    for y in d2[x]:
        sottoalbero(d,y,d2)
    return d2


def sottrai_alberi(d1,x,d2):
    d3={}
    for i in d1.keys():
        if i not in d2.keys():
            d3[i]=d1[i]
            if x in d3[i]:
                d3[i].remove(x)
    return d3

def ordina_albero(d):
    for key in d.keys():
        d[key]=sorted(d[key])
    return d

def albero_livelli(d,l,dL,r):
    if l==0:
        r=list(d.keys())[0]
    if l in dL.keys():
        dL[l]=dL[l]+[r]
    else:
        dL[l]=[r]

    for i in d[r]:
        albero_livelli(d,l+1,dL,i)
    return dL
