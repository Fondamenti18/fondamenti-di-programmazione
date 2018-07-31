from json import load, dump

def json_decoder(fin):
    
    with open(fin) as data:
        myDict = load(data)
    return myDict

def json_writer(fout,data):

    with open(fout, 'w') as fp:
        dump(data,fp)
  
def generate_subtree(myDict,subDict,x):

    subDict[x] = myDict[x]
    for key in myDict[x]:
        generate_subtree(myDict,subDict,key)
    return subDict
    
def genera_sottoalbero(fnome,x,fout):
    
    myDict = json_decoder(fnome)
    subDict = {}
    if x not in myDict: return subDict
    subDict = generate_subtree(myDict,subDict,x)
    json_writer(fout,subDict)
    
def delete_subtree(myDict,subDict,x):

    for key in subDict:
        del myDict[key]

    return myDict

def element_deleter(myDict,key,x):
    
    if x in myDict[key]:
            newList = myDict[key]
            newList.remove(x)
            myDict[key] = newList

    return myDict

def check_in_son(myDict,subDict,x):

    for key in myDict:
        myDict = element_deleter(myDict,key,x)
        

    return myDict


def cancella_sottoalbero(fnome,x,fout):
    
    myDict = json_decoder(fnome)
    subDict = {}
    if x not in myDict: return subDict
    subDict = generate_subtree(myDict,subDict,x)
    myDict = delete_subtree(myDict,subDict,x)
    myDict = check_in_son(myDict,subDict,x)
    json_writer(fout,myDict) 

def root_finder(myDict):

    root = []
    for element in myDict:
        for key, value in myDict.items():
            if element in value:
                root.append(key)
                return root

    return root

def level_finder(myDict,levelDict,level,root):

    level += 1
    
    for el in myDict[root]:
        if level not in levelDict: levelDict[level] = [] 
        levelDict[level].append(el)
        levelDict[level].sort()
        level_finder(myDict,levelDict,level,el)       
     
    return levelDict
    
def dizionario_livelli(fnome,fout):

    myDict = json_decoder(fnome)
    root = root_finder(myDict)
    
    levelDict = {}
    level = 0
    levelDict[level] = root
    levelDict = level_finder(myDict,levelDict,level,root[0])
    json_writer(fout,levelDict) 
    
def grade_finder(myDict,subDict,root,grade):
      
   
    for el in myDict[root]:
        grade = len(myDict[el])
        if grade not in subDict: subDict[grade] = []         
        subDict[grade].append(el)
        grade_finder(myDict,subDict,el,grade)
    
        
    return subDict
    
def find_anc(myDict,ancientDict,y,grade,current,previous):
    
    ancientDict[current] = grade

    for value in myDict[current]:
        prima = myDict[current]
        if len(myDict[current]) == y and value == prima[0]: grade +=1
        
        find_anc(myDict,ancientDict,y,grade,value,previous)

        
    return ancientDict
        
              

def dizionario_gradi_antenati(fnome,y,fout):

    myDict = json_decoder(fnome)
    root = root_finder(myDict)
    
    grade = len(myDict[root[0]])
    ancientDict = {}
    ancientDict = find_anc(myDict,ancientDict,y,0,root[0],root[0])
    json_writer(fout,ancientDict)
           
    


#dizionario_gradi_antenati("Alb10.json",2,"ciao.json")

