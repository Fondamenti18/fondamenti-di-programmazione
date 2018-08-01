import json
import copy

def getFatherTree(dic):
    fDic = {}
    for k in dic:
        val = dic[k]
        for vK in val:
            fDic[vK] = [k]
    return fDic

def loadJson(fnome):
    with open(fnome, 'r') as fi:
        dic = json.load(fi)
    return dic
    
def saveJson(fout, dic):
    with open(fout, 'w') as fo:
        json.dump(dic, fo)

def createSubTree(dic, nDic, sKey):
    lsSub = dic[sKey]
    nDic[sKey] = lsSub
    for sb in lsSub:
        createSubTree(dic, nDic, sb)
        
def delSubTree(dic, sKey):
    lsSub = dic.pop(sKey, None)
    if lsSub != None:
        for sb in lsSub:
            delSubTree(dic, sb)
            
def createLevelTree(dic, nDic, xNode, level):
    lsSub = dic[xNode]
    
    try:
        nDic[level] += [xNode]
    except KeyError:
        nDic[level] = [xNode]
        
    for sb in lsSub:
        createLevelTree(dic, nDic, sb, level + 1)
        

def ancestorsTree(fDic, aDic, sKey, fKey):
    try:
        fVal = fDic[fKey]
        aDic[sKey] += fVal
        ancestorsTree(fDic, aDic, sKey, fVal[0])
    except KeyError:
        pass


def genera_sottoalbero(fnome,x,fout):
    
    dic = loadJson(fnome)
    nDic = {}
    createSubTree(dic, nDic, x)
    for k in nDic:
        sorted(nDic[k])
    saveJson(fout, nDic)

    
def cancella_sottoalbero(fnome,x,fout):
    
    dic = loadJson(fnome)
    for k in dic:
        val = dic[k]
        if x in val:
            val.remove(x)
            break
    delSubTree(dic, x)
    saveJson(fout, dic)
    

def dizionario_livelli(fnome,fout):
    dic = loadJson(fnome)
    fDic = getFatherTree(dic)
    fNode = list(dic.keys() - fDic.keys())
    nDic = {}
    createLevelTree(dic, nDic, fNode[0], 0)
    for k in nDic:
        nDic[k] = sorted(nDic[k])
    saveJson(fout, nDic)
    

def dizionario_gradi_antenati(fnome,y,fout):
    dic = loadJson(fnome)
    fDic = getFatherTree(dic)
    aDic = copy.deepcopy(fDic)
    nDic = {}
    for k in dic:
        nDic[k] = 0
    for k in fDic:
        fth = fDic[k]
        ancestorsTree(fDic, aDic, k, fth[0])
    for k in aDic:
        for fth in aDic[k]:
            if len(dic[fth]) == y:
                nDic[k] += 1
    saveJson(fout, nDic)