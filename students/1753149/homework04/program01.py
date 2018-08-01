




import json

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        f=json.load(f)
        diz={}
        diz=genera(diz, x, f)
    with open(fout,'w') as ris:
        json.dump(diz,ris)
        
        
def genera(diz, x, f):
    if f[x]==[]:
        diz[x]=[]
    else:
        for i in f[x]:
            diz[x]=f[x]
            genera(diz,i,f)
    return diz
       
    

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        f=json.load(f)
        val_input=f.values()
        diz={}
        diz_ridotto=cancella(diz,x,f)
        val_ridotti=diz_ridotto.values()
        chiavi_ridotte=set(diz_ridotto)
        chiavi_file=set(f)
        chiavi=(chiavi_file-chiavi_ridotte)
        diz_nuovo={}
        print(chiavi)
        for i in chiavi:
            diz_nuovo[i]=f[i]
        for j in diz_nuovo.copy().keys():
            if x in diz_nuovo[j]:
                del(diz_nuovo[j][diz_nuovo[j].index(x)])
        print(diz_nuovo)
    with open(fout,'w') as ris:
        json.dump(diz_nuovo,ris)
        
def cancella(diz, x, f):
    if f[x]==[]:
        diz[x]=[]
    else:
        for i in f[x]:
            diz[x]=f[x]
            genera(diz,i,f)
    return diz

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        f=json.load(f)
        diz={}
        leaf=foglia(f)
        root=radice(f,leaf)
        levels=livelli(diz,0,f,[root])
        print(levels)
    with open(fout,'w') as ris:
        json.dump(levels,ris)

def livelli(diz,cont,f,lista):
    lista1=[]
    if lista!=[]:
        lista2=sorted(lista)
        diz[cont]=lista2
        cont+=1
    if lista==[]:
        return
    else:
        for i in lista:
            figlio=f[i]
            lista1=lista1+figlio
        livelli(diz,cont,f,lista1)
    return diz
    
    
    
def foglia(f):
    for i in f.keys():
        if f[i]==[]:
            foglia=i
            break
    return foglia
    
    
def radice(f, foglia):
    cont=0
    for x,y in f.items():
        if foglia in y:
            return radice(f,x)
        else:cont+=1
    if cont==len(f):
        return foglia

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        f=json.load(f)
        diz={}
        leaf=foglia(f)
        root=radice(f,leaf)
        diz_nuovo={}
        diz_nuovo=dizionario(diz,f,y,[root],0)
    with open(fout,'w') as ris:
        json.dump(diz_nuovo,ris)
        
        
def dizionario(diz,f,a,radice,cont):
    lista=[]
    if radice==[]:
        return
    else:
        for i in radice:
            figlio=f[i]
            diz[i]=cont
            if len(figlio)==a:
                cont+=1
            lista=figlio
            dizionario(diz,f,a,lista,cont)
           
    return dict(sorted(diz.items()))