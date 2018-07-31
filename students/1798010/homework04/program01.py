import json

def genera_sottoalbero(fnome,x,fout):

    dic = {}
    
    with open(fnome) as f:
        dic = json.load(f)
    
    dic = get_tree([x],{},dic)
    
    with open(fout,"w") as f:
        json.dump(dic,f)
    
def get_tree(keys,newDic,dic):
    
    if keys == []:
        return []
    else:
         for key in keys:
            
            try:
                newDic[key] = dic[key]
                get_tree(dic[key],newDic,dic)
                
            except KeyError:
                return {}
                
    return newDic
    
def cancella_sottoalbero(fnome,x,fout):
    
    dic = {}
    
    with open(fnome) as f:
        dic = json.load(f)
    
    del_tree([x],dic)
        
    for key in dic:
        try:
            dic[key].remove(x)
            break
        except ValueError:
            continue
        
    with open(fout,"w") as f:
        json.dump(dic,f)
        
def del_tree(keys,dic):
    
     for key in keys:

        del_tree(dic[key],dic)        
        dic.pop(key,None)
        
def dizionario_livelli(fnome,fout):
    
    dic = {}
    
    with open(fnome) as f:
        dic = json.load(f)
        
    #for key in dic:
        #dic = get_level([key],0,dic,{}) 
        #break
    
    root = findRoot(dic)
    #print(root)
    
    dic = get_level([root],0,dic,{})
    
    for key in dic:
        dic[key].sort()
    
    #print (dic)
    with open(fout,"w") as f:
        json.dump(dic,f)

def findRoot(dic):
    
   
    for key in dic:
        
        for testKey in dic:
            
            if key in dic[testKey]:
                break
            
            return key
        
        
def get_level(keys,level,dic,newDic):
    
    #print("level:",level)
    #print("keys:",keys)
    
    if keys != []:
        try:
            newDic[level] += keys
        except KeyError:
            newDic[level] = keys
        
        level += 1
        
        for key in keys:
            #print("     key:",key)
            get_level(dic[key],level,dic,newDic)
        
        return newDic
    
def dizionario_gradi_antenati(fnome,y,fout):

    with open(fnome) as f:
        dic = json.load(f)
        
    for key in dic:
        dic = anchestors(dic,{},[key],y,0) 
        break
    
    with open(fout,"w") as f:
        json.dump(dic,f)
    
def anchestors(dic,newDic,keys,y,level):
    
    if keys != []:
        
        if len(keys) == y:
            level += 1
        
        for key in keys:
            newDic[key] = level
            anchestors(dic,newDic,dic[key],y,level)
        
        return newDic

#dizionario_gradi_antenati("Alb10.json",2,"")   
#dizionario_livelli("Alb10.json","f")
#cancella_sottoalbero("Alb10.json","d","cunt.json")