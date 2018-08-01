import json
def genera_sottoalbero(fnome,x,fout):
    d_izi=open(fnome)
    diz=d_izi.readline()
    d_izi=json.loads(diz)
    dic={}
    if x in d_izi:
        dic=sub_tree(d_izi,x,dic)
    json.dump(dic,open(fout,'w'))
def sub_tree(d_izi,x,dic):
     for chiave in d_izi:
         if chiave==x:
             dic[chiave]=d_izi[chiave]
             for i in d_izi[chiave]:
                 sub_tree(d_izi,i,dic)
     return dic
def cancella_sottoalbero(fnome,x,fout):
    d_izi=open(fnome)
    diz=d_izi.readline()
    d_izi=json.loads(diz)
    c=0
    dic={}
    diz={}
    if x in d_izi:
        dic=sub_tree(d_izi,x,dic)
        diz=canc(diz,dic,d_izi)
    json.dump(diz,open(fout,'w'))
def canc(diz,dic,d_izi):
    c=0
    sup_list=[]
    for chiave in d_izi:
        if chiave not in dic:
            sup_list=d_izi[chiave]
            diz[chiave]=d_izi[chiave]
            for x in sup_list:
                if x not in dic:
                    diz[chiave]=d_izi[chiave]
                else:
                    c=sup_list.index(x)
                    del sup_list[c]
                    d_izi[chiave]=sup_list
                    diz[chiave]=d_izi[chiave]
    return diz
def dizionario_livelli(fnome,fout):
    d_izi=open(fnome)
    diz=d_izi.readline()
    d_izi=json.loads(diz)
    dictionary={}
    son=next(iter(d_izi.keys()))
    root=find_root_father(d_izi,son)
    dictionary=make_list_ancestors(d_izi,dictionary,0,root)
    json.dump(dictionary,open(fout,'w'))
def find_root_father(d_izi,son):
    var_ret=son
    for p_cont,f_cont in d_izi.items():
        if son in f_cont:
            var_ret=find_root_father(d_izi,p_cont)
    return var_ret
def make_list_ancestors(d_izi,dictionary,level_tree,grandson):
    sup_list=[]
    sup_list.append(grandson)
    if level_tree not in dictionary:
        dictionary[level_tree]=sup_list
    else:
        sup_list+=dictionary[level_tree]
        sup_list.sort()
        dictionary[level_tree]=sup_list
    sons=d_izi[grandson]
    if sons!='[]':
        for son in sons:
            dictionary=make_list_ancestors(d_izi,dictionary,level_tree+1,son)
    return dictionary
def find_father(d_izi,dictionary,counter,val,radi):
    dictionary[radi]=counter
    sons=d_izi[radi]
    if len(sons)==val:
        counter+=1
    for son in sons:
        dictionary=find_father(d_izi,dictionary,counter,val,son)
    return dictionary
def dizionario_gradi_antenati(fnome,y,fout):
    d_izi=open(fnome)
    diz=d_izi.readline()
    d_izi=json.loads(diz)
    dictionary={}
    son=next(iter(d_izi.keys()))    
    root=find_root_father(d_izi,son)   
    dictionary=find_father(d_izi,dictionary,0,y,root)
    json.dump(dictionary,open(fout,'w'))





