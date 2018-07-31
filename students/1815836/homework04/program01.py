
import json
#prima funzione
def generate(fnome,x,fout,diz,diz_root):
    root = x
    if root == []:
        return diz_root
    diz_value=diz.get(x)
    diz_root[x]=diz_value
    for val in diz_value:
        diz_root.update(generate(fnome,val,fout,diz,diz_root))
    return(diz_root)
def genera_sottoalbero(fnome,x,fout):
    with open(fnome) as json_data:
        diz_root={}
        diz = json.load(json_data)
        diz_root.update(generate(fnome,x,fout,diz,diz_root))  
        opfout=open(fout,mode="w")
        json.dump(diz_root,opfout)
        opfout.close()
        json_data.close()
#seconda funzione
        
def remove(fnome,x,fout,diz,diz_root,root):
    if root == []:
        return diz_root
    diz_value=diz.get(root)
    if x in diz_value:
        diz_value.remove(x)
    diz_root[root]=diz_value
    for val in diz_value:
        if (val==x):return()
        root=val
        diz_root.update(remove(fnome,x,fout,diz,diz_root,root))
    return(diz_root)
def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as json_data:
        diz_root={}
        diz = json.load(json_data)
        key = list(diz.keys())
        test=[]
        for val in list(diz.values()):
            test+=val
        for sroot in key:
            if sroot not in test:
                root=sroot
        diz_root.update(remove(fnome,x,fout,diz,diz_root,root))  
        opfout=open(fout,mode="w")
        json.dump(diz_root,opfout)
        opfout.close()
        json_data.close()
#terza funzione
listaesterna=[]
def listafunz(diz,root,livelloattuale):
    global listaesterna
    if root==[]:return ()
    diz_value=diz.get(root)
    listaesterna+=[[livelloattuale]+[root]]
    livelloattuale+=1
    for val in diz_value:
        root=val   
        listafunz(diz,root,livelloattuale)
    listaesterna.sort()
    return()
    
def sistemazionelista(level):
    global listaesterna
    listauscita=[]
    test=False
    for a in listaesterna:
        if a[0]==level:
            listauscita+=[a[1]]
            test=True
        if a[0]!=level and test==True:
            listauscita.sort()
            return(listauscita)
    listauscita.sort()
    return(listauscita)

    
def find_levels(diz,diz_root,root,level,lista):
    if root==[]:return (diz_root)
    diz_value=diz.get(root)
    diz_root[level]=sistemazionelista(level)
    level+=1
    for val in diz_value:
        root=val   
        diz_root.update(find_levels(diz,diz_root,root,level,lista))
    return(diz_root)
    
def dizionario_livelli(fnome,fout):
    global listaesterna
    with open(fnome) as json_data:
        diz = json.load(json_data)
        diz_root={}
        lista=[]
        key = list(diz.keys())
        test=[]
        for val in list(diz.values()):
            test+=val
        for sroot in key:
            if sroot not in test:
                root=sroot
        level=0
        listafunz(diz,root,0)
        diz_root.update(find_levels(diz,diz_root,root,level,lista))
        listaesterna=[]
        opfout=open(fout,mode="w")
        json.dump(diz_root,opfout)
        opfout.close()


#quarta funzione
def find_ancients(diz,diz_root,root,y,grado):
    if root==[]:return (diz_root)
    diz_value=diz.get(root)
    diz_root[root]=grado
    if(len(diz_value)==y):
        grado+=1
    for val in diz_value:
        root=val   
        diz_root.update(find_ancients(diz,diz_root,root,y,grado))
    return(diz_root)
def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as json_data:
        diz = json.load(json_data)
        diz_root={}
        grado=0
        key = list(diz.keys())
        test=[]
        for val in list(diz.values()):
            test+=val
        for sroot in key:
            if sroot not in test:
                root=sroot
        diz_root.update(find_ancients(diz,diz_root,root,y,grado))
        opfout=open(fout,mode="w")
        json.dump(diz_root,opfout)
        opfout.close()
        json_data.close()
        
